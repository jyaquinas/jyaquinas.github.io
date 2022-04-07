---
layout: post
title: CI/CD with Travis and AWS CodeDeploy
subtitle: ---
date: 2022-04-06 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "CICD"
tags: [cicd, travis, codedeploy]
---

### What is CI/CD?
--

### What is Travis?
--

### Setting Up Travis
Sign up with your github account and sync your repositories. It seems like Travis has new pricing plans, and you have to specifically select the Free Plan in order to start using it. This isn't done by default, so you'll have to sign up and select a plan in your account settings. 

You will then need to create a `.travis.yml` file in the same location as your `build.gradle` file. 

Here's an example:

```yaml
# File: .travis.yml 
language: java
jdk:
  - openjdk11

# Select branch for executing CI
branches:
  only:
    - master

# Travis CI server home
cache: # caching location for dependencies (avoid redownloading existing dependencies)
  directories:
    - '/$HOME/.m2/repository'
    - '$HOME/.gradle'

# command to be executed when branch is pushed
script: "./gradlew clean build"


# Email notification after CI execution
notifications:
  emails:
    recipients:
      - 'youremail@email.com'
```

Once you commit and push this to your master branch, you'll notice in your Travis dashboard that it will start building your project automatically. 

### What is CodeDeploy?
CodeDeploy is a service provided by AWS that is responsible for deploying your applications. It can actually perform both build and deployment processes, but it is recommended to keep them separate since there are times when we only want to perform only one of them. 

However, AWS CodeDeploy doesn't have storage function. So we will need to connect it with our S3 instance to store the jar files. So you'll need to also create an S3 bucket instance (the default settings should be fine).

### Linking Travis To Your AWS S3
You first need to create an IAM user to allow external services like Travis to have access to your AWS account. Use the following settings:

  * programmatic access (with access key)
  * attach existing policies
    * AWSCodeDeployFullAccess
    * AmazonS3FullAccess

Then using the newly generated Access Key ID and Secret Access Key, add them to the environment variables (under your repository settings in Travis). You can then access these on your `.travis.yml` file using then variable name you set. For instance, if your variable name is AWS_ACCESS_KEY, you can access it through $AWS_ACCESS_KEY.

We'll add the following to our `.travis.yml` file:

```yaml
# execute before deploy command
before_deploy:
  # zip (CodeDeploy doesn't recognize jar files)
  - zip -r webservice-springboot *
  - mkdir -p deploy
  - mv webservice-springboot.zip deploy/webservice-springboot.zip

deploy:
  - provider: s3
    access_key_id: $AWS_ACCESS_KEY
    secret_access_key: $AWS_SECRET_KEY
    # AWS S3 bucket
    bucket: webservice-springboot-build
    region: ap-northeast-2
    skip_cleanup: true
    acl: private
    # directory created under before_deploy
    # only files in this directory get sent to s3
    local_dir: deploy
    wait_until_deployed: true
```

After you push, you'll notice that Travis will start building your project and deploy the final build file to your S3 bucket.

### Linking CodeDeploy
Since EC2 is our target instance for code deployment, we will assign a new role to it. Create a new role under IAM, and look for the `AmazonEC2RoleforAWSCodeDeply` permission policy. 

Now go to your EC2 instance, right click and go to Security -> Modify IAM role. Select the newly created role and reboot.

#### Installing the CodeDeploy agent in your EC2 server
The linux instance doesn't come with ruby preinstalled. So let's install that first.
`sudo yum -y install ruby'

Then let's install the code deploy agent.
`aws s3 cp s3://aws-codedeploy-ap-northeast-2/latest/install to ./install`
`sudo ./install auto`

Check if CodeDeploy was properly installed. 
`sudo service codedeploy-agent status`

### Creating a Code Deploy Application
Create a new IAM role and select CodeDeploy as the service. Now let's create a new Code Deploy application (search for Code Deplooy in your AWS Console). Then create a new deployment group and select the newly created role. 

The configurations for CodeDeploy will be set on the `apspec.yml` file, so let's create this file on the same directory as the `.travis.yml` file. 

```yaml
# File: appspec.yml
# AWS CodeDeploy Settings
version: 0.0
os: linux
files:
    # specify files to send to destination (/ sends everything)
  - source: /
    # specify the location where deploy files will be received
    destination: /home/ec2-user/app/step2/zip/
    overwrite: yes
```

Let's add our CodeDeploy info to our travis file under `deploy`:
```yaml
deploy:
  ...
  - provider: codedeploy
    access_key_id: $AWS_ACCESS_KEY
    secret_access_key: $AWS_SECRET_KEY
    bucket: webservice-springboot-build
    key: webservice-springboot.zip
    bundle_type: zip
    # Name of AWS CodeDeploy application
    application: webservice-springboot
    # defined in AWS CodeDeploy deployment group
    deployment_group: webservice-springboot-group
    region: ap-northeast-2
    wait_until_deployed: true
```

Our final travis file now looks like:
```yaml
# File: .travis.yml
# Travis Settings
language: java
jdk:
  - openjdk11

# Select branch for executing CI
branches:
  only:
    - master

# Travis CI server home
cache: # caching location for dependencies (avoid redownloading existing dependencies)
  directories:
    - '/$HOME/.m2/repository'
    - '$HOME/.gradle'

# command to be executed when branch is pushed
script: "./gradlew clean bootJar"

# execute before deploy command
before_deploy:
  # zip (CodeDeploy doesn't recognize jar files)
  - zip -r webservice-springboot *
  - mkdir -p deploy
  - mv webservice-springboot.zip deploy/webservice-springboot.zip

deploy:
  - provider: s3
    access_key_id: $AWS_ACCESS_KEY
    secret_access_key: $AWS_SECRET_KEY
    # AWS S3 bucket
    bucket: webservice-springboot-build
    region: ap-northeast-2
    skip_cleanup: true
    acl: private
    # directory created under before_deploy
    # only files in this directory get sent to s3
    local_dir: deploy
    wait_until_deployed: true

  - provider: codedeploy
    access_key_id: $AWS_ACCESS_KEY
    secret_access_key: $AWS_SECRET_KEY
    bucket: webservice-springboot-build
    key: webservice-springboot.zip
    bundle_type: zip
    # Name of AWS CodeDeploy application
    application: webservice-springboot
    # defined in AWS CodeDeploy deployment group
    deployment_group: webservice-springboot-group
    region: ap-northeast-2
    wait_until_deployed: true

# Email notification after CI execution
notifications:
  email:
    recipients:
      - 'jythomaskim@gmail.com'

```

Now if you commit and push the newly added and modified files, you should see travis building your project. The final deployment files should be sent to your EC2 instance under the directory that we specified in our file, `/home/ec2-users/app/step2/zip/`.

### Automating the Deployment Process
In order to fully automate the deployment process, we will use bash script files. 

```bash
#!/bin/bash

REPOSITORY=/home/ec2-user/app/step2
PROJECT_NAME=webservice-springboot

echo "> Copying build files."

cp $REPOSITORY/zip/*.jar $REPOSITORY

echo "> Checking pid of current application running"

CURRENT_PID=$(pgrep -fl webservice-springboot | grep jar | awk '{print $1}')

echo "> pid of current application running: $CURRENT_PID"

if [ -z "$CURRENT_PID" ]; then
  echo "> No application running."
else
  echo "> kill -15 $CURRENT_PID"
  kill -15 $CURRENT_PID
  sleep 5
fi

echo "> Deploying new application"

JAR_NAME=$(ls -tr $REPOSITORY/*.jar | tail -n 1)

echo "> JAR Name: $JAR_NAME"

echo "> Adding execution permission to $JAR_NAME"

chmod +x $JAR_NAME

echo "> Executing $JAR_NAME"

nohup java -jar \
  -Dspring.config.location=classpath:/application.yml,classpath:/application-real.yml,/home/ec2-user/app/application-oauth.yml,/home/ec2-user/app/application-real-db.yml \
  -Dspring.profiles.active=real \
  $JAR_NAME > $REPOSITORY/nohup.out 2>&1 &
```
***Note:** adding line breaks between the config file paths will lead to errors. Make sure all the config locations are comma separated (without backslashes).*

Then we'll make some changes to our travis and appspec files.
```yaml
# File: .travis.yml
...
before_deploy:
    # directory for storing files that will be zipped
  - mkdir -p before-deploy
  - cp scripts/*.sh before-deploy/
  - cp appspect.yml before-deploy/
  - cp build/libs/*.jar before-deploy/
    # zip file and move to deploy folder
  - cd before-deploy && zip -r before-deploy *
  - cd ../ && mkdir -p deploy
  - mv before-deploy/before-deploy.zip deploy/webservice-springboot.zip
```

```yaml
# File: appspec.yml
...
# grant ec2-user permissions to all files sent by CodeDeploy (to EC2)
permissions:
  - object: /
    pattern: "**"
    owner: ec2-user
    group: ec2-user

# Specify action during deployment
hooks:
  # execute deploy.sh as ec2-user
  ApplicationStart:
    - location: deploy.sh
      timeout: 60
      runas: ec2-user
```

Let's now push this and see our project be deployed automatically.

Something wrong? Check your nohup.out file and make sure all your settings and file paths have been set correctly. 