---
layout: post
title: ---
subtitle: ---
date: 2022-02-22 22:03:00 +0900
background: '/img/bg-post.jpg'
category: ""
tags: []
---

## Questions & Concepts To Cover
* What does @builder do -> what is builder pattern
    * https://www.geeksforgeeks.org/builder-design-pattern/
    * https://refactoring.guru/design-patterns/builder
    * https://projectlombok.org/features/Builder
* memento design patttern

* @webmvctest vs @springboottest & testresttemplate
    * jpa doesnt work in webmvctest? only inits controller and controller advice
    * HttpEntity
    * ResponseEntity
    * How to test with spring security? creating mock users, etc

* Spring/JPA Annotations 
    * @Transactional
        * https://dzone.com/articles/how-does-spring-transactional
        * https://stackoverflow.com/questions/26387399/javax-transaction-transactional-vs-org-springframework-transaction-annotation-tr
        * Transactional (readOnly = true)
    * @Autowired
    * @Service, @Controller, @Repository
        * special types of @Component
        * @Repository -> implements JPA repository with basic read/write operations for entities to the DB
        * @Service -> hold business logic
        * @Controller -> class that implements REST endpoints
    * @Controller vs @RestController

* why pass .class
* look into index.js file (mustache)
    * ajax
    * CRUD -> html func (post, get, put, delete)

* how oauth2 works 
    * https://developers.google.com/identity/protocols/oauth2

* creating annotations in java?
    * https://docs.oracle.com/javase/tutorial/java/annotations/declaring.html

* yum install -> list available packages
    * `yum list available packagename\*`
* `2>&1` -> [post](https://superuser.com/questions/71428/what-does-21-do-in-command-line#:~:text=The%201%20denotes%20standard%20output,is%20being%20redirected%20as%20well.)
    * > The 1 denotes standard output (stdout). The 2 denotes standard error (stderr). So 2>&1 says to send standard error to where ever standard output is being redirected as well. Which since it's being sent to /dev/null is akin to ignoring any output at all.

* Crontab 
    * https://www.adminschoice.com/crontab-quick-reference
    * https://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/
    * https://opensource.com/article/17/11/how-use-cron-linux
    * files used to schedule the execution of programs 
    * 

* deploying project to server
    * git clone project to server
    * run tests using `./gradlew test` -> should successfully run
    * build using `./gradlew build` 
    * perform repetitive tasks through bash script
    ```shell
    #!/bin/bash

    REPOSITORY=/home/ec2-user/app/step1
    PROJECT_NAME=springboot-webservice

    cd $REPOSITORY/$PROJECT_NAME/

    echo "> Git Pull"

    git pull

    echo "> Start building project"

    ./gradlew build

    echo "> Copying build file"

    cp $REPOSITORY/$PROJECT_NAME/build/libs/*.jar $REPOSITORY/

    echo "> Checking pid of current application"

    CURRENT_PID=$(pgrep -f ${PROJECT_NAME}.*.jar)

    if [ -z "$CURRENT_PID" ]; then
            echo "> Cannot kill process. There is no application running. "
    else
            echo "> kill -15 $CURRENT_PID"
            kill -15 $CURRENT_PID
            sleep 5
    fi

    echo "> Deploying new application"

    JAR_NAME=$(ls -tr $REPOSITORY/ | grep jar | tail -n 1)

    echo "> Jar Name: $JAR_NAME"

    nohup java -jar -Dspring.config.location=classpath:/application.yml,/home/ec2-user/app/application-oauth.yml $REPOSITORY/$JAR_NAME 2>&1 &
    ```
    * must add oauth properties file 
        * edit deploy -> `nohum java -jar -Dspring.config.location=classpath:/application.properties,/home/ec2-user/app/application-oath.prooperties $REPOSITORY/$JAR_NAME 2>&1 &` 
        * absolute path is used for oauth becauase classpath points to the resources directory inside the jar file (and the oauth file is outside of the jar)

    * When you check nohup.out and you get the following error: `NoClassDefFoundError`, you need to define the main class in your `build.gradle` file
        ```groovy
        jar {
            manifest {
                attributes(
                        'Main-Class': 'com.example.springboot.Application'
                )
            }
        }
        ```
    * gradlew build vs bootJar -> [post](https://stackoverflow.com/questions/64747475/difference-between-gradle-build-and-gradle-bootjar)
        * build -> builds everything, including tests, generating documentation, etcs
        * bootJar -> custom jar task from spring boot gradle plugin, that produces a spring boot executable jar
    
    * application-real-db.yml
        ```groovy
        spring:
        jpa:
            hibernate:
                ddl-auto: none
        datasource:
            url: "jdbc:mariadb://springboot-webservice.c2vqrhmxmoa9.ap-northeast-2.rds.amazonaws.com:3306/springboot_webservice"
            username: admin
            password: ********
            driver-class-name: org.mariadb.jdbc.Driver
        ```
    

* session persistence methods
    * use tomcat sessions - but if multiple tomcat servers are used, extra configuration is required to synchronize user sessions across servers
    * saving sessions to DB - but high login rates may create performance issues (due to high request to db)
    * using caches (redis memcached) - mostly used in applications with large user base

* What is tomcat?
    * lightweight server - web server and servlet container (not a full application server) written in java -- is production ready
* Web server vs web application server 

* inheritance vs composition
    * inheritance: car is a vehicle 
    * composition: car has a steering wheel
    * inheritance - considered tightest form of coupling in OOP (changing base class can cause undesirable side effects on subclasses)
    * composition is more loose in coupling - achieved through dependency injection
    * https://betterprogramming.pub/inheritance-vs-composition-2fa0cdd2f939#:~:text=Composition%20is%20in%20contrast%20to,that%20implement%20the%20desired%20functionality.
    
* UML
    * Relationships:
        * generalization (class inheritance): shown by line with empty arrow head (bear inherits from animal class)
        * realization (interface implementation): shown by dashed line with empty arrow head (logger class implements ILogger interface)
        * dependency (through method parameter, return type, etc): shown by dashed line and flat arrow, change to an element will likely affect the other elements
        * association: shown by a simple line, relationship between classes (can show multiplicity)
        * aggregation: shown by a line with an empty diamond head, type of association, a "has a" relationship, but where each can exist on its own (car, tire)
        * composition: shown by a line with a filled diamond head, special type of aggregation but the 'parent' class will control the lifetime of the child class, meaning that if the parent is destroyed, so will the child class