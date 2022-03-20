---
layout: post
title: Creating Your First AWS EC2 Instance
subtitle: 
date: 2022-03-17 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "Server"
tags: [aws, server, ec2]
---

## AWS EC2
In order to run our applications continously, we have a few options:
* Run the application on our PC's and keeping it live for 24hrs
* Use a hosting service
* Use a cloud service

If we experience a lot of traffic at a certain period of time, or we expect to scale our application, it is better to go for a cloud service, where we can easily expand the server specs as we need. 

Types of cloud services:
* Infrastructure as a Service (Iaas)
    * computing resources along with other services, such as storage, networking capabilities, etc
    * AWS EC2, S3, google compute engine, microsoft azure
* Platform as a Service (PaaS)
    * complete development and deployment environment offered to customers
    * beanstalk, heroku, google app engine, windows azure
* Software as a Service (Saas)
    * service in the form of applications offered directly to customers
    * google drive, dropbox, docusign

### What is AWS EC2
EC2 stands for Elastic Compute Cloud. It is a general purpose computing resource with optimized computing performance, memory, storage, and networking. This can be automatically scaled up and down based on your application needs. Multiple operating systems are provided, but only the linux and windows instances (t2 or t3.micro) are available for the free tier.

Full list of EC2 instances can be found [here](https://aws.amazon.com/ec2/instance-types/).

#### Free Tier Limitations
* 1 year free trial period
* 750 hours/month of usage (so unlimited if you only use 1 micro instance)
* Linux or Windows operating systems

### Launching an EC2 Instance
1. Select your region on the top right corner (this is the AWS datacenter's physical locations).
2. Click on EC2, then launch an instance.
3. Select the Amazon Machine Image (AMI)[^ami]. You can tick the 'Free tier only' checkbox. 
4. Select the instance (only the t2.micro falls under the free tier category).
5. Configure the instance (VPCs[^vpc], subnets, shutdown behavior, etc). Use the default settings to start out. 
6. Set the storage to 30 GB (the maximum for the free tier).
7. Add tags to your instance. This is to help you manage your resources as you add more resources. Check out the tagging [best practices](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) recommended by Amazon.
8. Configure the security group, which controls your traffic through a set of firewall rules. It is recommended to only allow known IPs for security reasons (do not use the default 0.0.0.0/0). Check out this [security group guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules-reference.html).
9. Launch.
10. Create and download new key pair (.pem file) for your instance. You will need this to access the server.

### Using Elastic IP
A new IP will be allocated every time the instance is restarted. So in order to keep using a fixed IP address, we will use the Elastic IP. 

On the left sidebar, click on Network & Security -> Elastic IPs.

Then click on 'Associate Elastic IP Address' and select your instance and private IP. 

***Important**: Unassociated elastic IPs are billable. Make sure to associate it with your free tier instance to avoid getting billed.*

### Connecting To Your EC2 Instance
Since I'm a mac user, I'll explain how you can connect to your instance using the terminal. You can also find instructions on how to connect using ssh in your AWS console.

`ssh -i keyfile.pem ec2-user@[ec2 ip address]`

The default username is `ec2-user`.

If you don't want to keep typing in the ip address, we can easily connect to a server using an alias. First, move your pem file to the following location, `~/.ssh/`.

`cp [current pem file path] ~/.ssh/`

Then let's create a config file. You can use any editor you like, but I'll use nano.

`nano ~/.ssh/config`

Fill in the information.

```shell
# config
Host yourAlias
	HostName yourHostName
	User ec2-user
	IdentityFile ~/.ssh/keyfile.pem
```

Set the name you want to use in the `Host` and input your EC2 instance hostname/IP for the `HostName`. Don't forget to save.

You can now connect with the host name you set.

`ssh yourAlias`



---
[^ami]: AMIs are image containers that contain all the necessary components to launch the instances.  
[^vpc]: VPCs are virtual private networks, virtual version of a physical network within the larger network. 

