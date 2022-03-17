---
layout: post
title: scrap
subtitle: 
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

* spring.profiles.include -> application.properties 
* application.properties vs yaml
* how oauth2 works 
    * https://developers.google.com/identity/protocols/oauth2

* creating annotations in java?
    * https://docs.oracle.com/javase/tutorial/java/annotations/declaring.html


---
## Misc Subjects
* What is java bean?
    * objects that are managed by spring IoC container

* for large projects with more complex data, it may be required to perform complex join operations for obtaining/searching for data
    * it is common to use spring data jpa for CUD operations, and use other frameworks for read operations (querydsl, jooq, mybatis)

* Dirty checking - JPA entity
    * https://jojoldu.tistory.com/415
    * https://www.netsurfingzone.com/hibernate/dirty-checking-in-hibernate/
    * automatically checks if objects have been modified and will update regularly (when session flushed or transaction is commited)

* session persistence methods
    * use tomcat sessions - but if multiple tomcat servers are used, extra configuration is required to synchronize user sessions across servers
    * saving sessions to DB - but high login rates may create performance issues (due to high request to db)
    * using caches (redis memcached) - mostly used in applications with large user base

* What is tomcat?
    * lightweight server - web server and servlet container (not a full application server) written in java -- is production ready

* Crontab 
    * https://www.adminschoice.com/crontab-quick-reference
    * https://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/
    * https://opensource.com/article/17/11/how-use-cron-linux
    * files used to schedule the execution of programs 
    * 

* Failover and loadbalancing in oracle db
    * https://docs.oracle.com/cd/E15217_01/doc.1014/e12490/failover.htm
    * https://docs.oracle.com/cd/B28196_01/idmanage.1014/b25344/failover.htm

* Using sqlplus in cloud oracle with wallet
    * download wallet, then upload to cloud storage
    * unzip wallet to a directory
    * set TNS_ADMIN variable to the directory `export TNS_ADMIN=/dir/`
    * edit sqlnet.ora and set update the directory
    * `sqlplus admin@dbname` -> dbname from tnsnames.ora
    * input password and voila

* pass variable to sql script by using `&1 &2`
    * `insert into authors (firstname, lastname) values ('&1', '&2');`
    * then use `@script.sql var1 var2`
    
* Oracle sql
    * `:=` is used for assigning values to variables
    * oracle sql vs pl/sql 
        * https://www.tutorialspoint.com/difference-between-sql-and-pl-sql
        * oracle sql is oracles version of SQL
        * pl/sql -> procedural language SQL -- extension of oracle sql, has functionalities of functions, control structures, triggers, etc (a programming language that uses SQL, meant for DBs)
        * cannot use pl/sql in mysql
        * `;` ends sql statement, `/` executes whatever is in the buffer (usually for running plsql blocks defined by begin and end)
    * plsql loops
        * https://blogs.oracle.com/sql/post/better-loops-and-qualified-expressions-array-constructors-in-plsql
        * https://stackoverflow.com/questions/36325831/use-oracle-pl-sql-for-loop-to-iterate-through-comma-delimited-string
        * https://stackoverflow.com/questions/2242024/for-each-string-execute-a-function-procedure
        * https://livesql.oracle.com/apex/livesql/file/tutorial_KS0KNKP218J86THKN85XU37.html

```sql
DECLARE
    type nt_arr is table of varchar2(50);
    arr nt_arr := nt_arr ('1234','asdf','23g');
BEGIN
  FOR i IN 1..arr.count
  LOOP
    DBMS_OUTPUT.PUT_LINE( arr(i) );
  END LOOP;
END;
```

* test with spring security
    * test application.yml -> add mock settings
    ```
    # test oauth
    security:
        oauth2:
        client:
            registration:
            google:
                client-id: test
                client-secret: test
                scope: [profile, email]
    ```
    * add dependency to gradle -> `implementation 'org.springframework.security:spring-security-test'`
    * use `@WithMockUser(roles="USER")` to create mock user with user authorization
    * must also use MockMvc -> using only @SpringBootTest does not use MockMvc
    
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

---
[^ami]: AMIs are image containers that contain all the necessary components to launch the instances.  
[^vpc]: VPCs are virtual private networks, virtual version of a physical network within the larger network. 