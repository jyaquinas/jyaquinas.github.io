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

* spring.profiles.include -> application.properties 
* application.properties vs yaml
* how oauth2 works 
    * https://developers.google.com/identity/protocols/oauth2

* creating annotations in java?
    * https://docs.oracle.com/javase/tutorial/java/annotations/declaring.html


---
## Misc Subjects
* python is pass by object reference:
    * mutable objects (list, dic, set, etc) -> passed by ref
    * immutable objects (str, int, tuple, etc) -> passed by val
    ```python
    # pass by value or ref -> in python pass by obj ref
    def addMutable(obj):
        obj.append(1)
        obj[0]=0
    l = [1,2]
    addMutable(l)
    print(l)

    def addImmutable(obj):
        obj+=2
    a=5
    addImmutable(a)
    print(a)
    ```

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
    
* TCP (Transmission Control Protocol) vs UDP (User/Universal Datagram Protocol)
    * both are transport layer protocols of the TCP/IP protocol stack, both use IP protocol
    * https://www.diffen.com/difference/TCP_vs_UDP
    * TCP 
        * connection orientated protocol
        * typically used when requires guaranteed message delivery (high reliability)
        * has built it error recovery and retransmission
        * sets up connection using 3 way handshake 
            * 1. send SYN (synchronize sequence number), informs server it wants to establish connection
            * 2. server responds to client by sending SYN-ACK (acknowledgement) 
            * 3. client responds to server with ACK -> reliable connection established, now two way data transfer is possible
    * UDP
        * connectionless protocol (no handshake mechanism)
        * data can be sent but cannot know whether it was successfully delivered on not (typically for apps that require fast data transfers)
        * error handling must be done on the receiving side
        * faster than TCP because there is no connection setup (less network traffic) and does not consume resources on receiving side (does not keep connection open)

