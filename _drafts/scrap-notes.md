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

* spring.profiles.include -> application.properties 
* application.properties vs yaml
* how oauth2 works 
    * https://developers.google.com/identity/protocols/oauth2

* creating annotations in java?
    * https://docs.oracle.com/javase/tutorial/java/annotations/declaring.html

* yum install -> list available packages
    * `yum list available packagename\*`
* `2>&1` -> [post](https://superuser.com/questions/71428/what-does-21-do-in-command-line#:~:text=The%201%20denotes%20standard%20output,is%20being%20redirected%20as%20well.)
    * > The 1 denotes standard output (stdout). The 2 denotes standard error (stderr). So 2>&1 says to send standard error to where ever standard output is being redirected as well. Which since it's being sent to /dev/null is akin to ignoring any output at all.
* changing default java version 
    * `sudo /usr/sbin/alternatives --config java`, then select java version
    * check with `java -version`
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
* python heapq -> heapreplace(arr, val) heappushpop(arr, val)
    * heappushpop() will push value to the heap first before popping the min value
    * heapreplace() is a one step pop and replace operation, more efficient than heappushpop, but will get the min value from the heap disregarding the val that is being input. That means that the popped value can be larger than the value being input. 

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
* Web server vs web application server 

* Crontab 
    * https://www.adminschoice.com/crontab-quick-reference
    * https://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/
    * https://opensource.com/article/17/11/how-use-cron-linux
    * files used to schedule the execution of programs 
    * 


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
    

* Oracle packages
    * > A package is a schema object that groups logically related PL/SQL types, variables, constants, subprograms, cursors, and exceptions. A package is compiled and stored in the database, where many applications can share its contents.

* SQL Tuning
    * selectivity = number of rows from query / total rows
        * OR cardinality / total rows?
        * selectivity of 1 -> all rows are unique, high selectivity
        * full table scan for low selectivity 
    * cardinality = selectivity * total rows 
        * number of unique values in a column
    * Analyzing execution plan
        * explain plan
            * `EXPLAIN PLAN FOR <QUERY>` -> saves to plan_table
            * `SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY())`
            * `EXPLAIN PLAN SET statement_id = 'MyID' FOR SELECT FROM EXPLOYEES where employee_id = 100;`
            * `EXPLAIN PLAN SET statement_id = 'MyID' INTO MyPlanTable FOR SELECT FROM EMPLOYEES where employee_id = 100;`
        * autotrace -> produces execution plan and statistics, uses plan_table like the explain plan
            * `SET AUTOTRACE ON;`
            * `SET AUTOTRACE ON [EXPLAIN|STATISTICS];`
            * `SET AUTOTRACE TRACE[ONLY] ON [EXPLAIN|STATISTICS];`
            * `SET AUTOTRACE OFF`
        * v$SQL_PLAN -> actual execution plans stored here, similar to plan table, connected to V$SQL view
            * `SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR('****'));`
            * look at cost, access methods, cardinality, join mehtods/join types, partition pruning, etc
    * Note: comparing costs between 2 different queries is meaningless because the costs are relative to the specific query. 
        * More accurate to compare consistent gets (from autotrace) -> physical reads that the DB performs to get data from data block (disk I/O)
    * access predicate vs filter predicate
        * access predicate: only fetch matching rows (usually through index)
        * filter predicates: discard non-matching rows (after fetching more rows than needed)
    * Tuning strategies
        * Parse time reduction 
        * execution plan comparison and analysis
        * query analysis strategy
            * update statistics (must have DBA access) - outdated statistics may mislead the optimizer 
            * improve query structure
            * use optimizer hints
            * changing access path 
            * improve join order and join methods

* subquery factoring (WITH CLAUSE) vs global temporary tables (GTT)
    * used for improving query speed for complex subqueries
    * typically used when subquery is executed multiple times
* case expression
    * https://docs.oracle.com/cd/B19306_01/server.102/b14200/expressions004.htm
    * >CASE expressions let you use IF ... THEN ... ELSE logic in SQL statements without having to invoke procedures.
    ```sql
        SELECT cust_last_name,
        CASE credit_limit WHEN 100 THEN 'Low'
        WHEN 5000 THEN 'High'
        ELSE 'Medium' END
        FROM customers;
    ```

* lead
    * https://docs.oracle.com/cd/B19306_01/server.102/b14200/functions074.htm
    * > LEAD is an analytic function. It provides access to more than one row of a table at the same time without a self join. Given a series of rows returned from a query and a position of the cursor, LEAD provides access to a row at a given physical offset beyond that position.
    * basic syntax:
    ```sql
    LEAD(expression [, offset ] [, default ])
    OVER (
        [ query_partition_clause ] 
        order_by_clause
    )
    ```
    
    * `expression`: must return single value, expression that is evaluated for the row
    * `offset`: offset value from current row, default is 1
    * `default`: if offset goes beyond scope of partition, it will return this default value. NULL by default.
    * `query_partition_clause`: this clause divides the rows into partitions to which the lead function will be applied (Think of it as applying the lead function on different categories, and each category being ordered by the condition stated in order_by_clause). It will treat the entire thing as single partition by default.
    * `order_by_clause`: specifies order of rows in each partition

    ```sql
    SELECT last_name, hire_date, 
    LEAD(hire_date, 1) OVER (ORDER BY hire_date) AS "NextHired" 
    FROM employees WHERE department_id = 30;

    LAST_NAME                 HIRE_DATE NextHired
    ------------------------- --------- ---------
    Raphaely                  07-DEC-94 18-MAY-95
    Khoo                      18-MAY-95 24-JUL-97
    Tobias                    24-JUL-97 24-DEC-97
    Baida                     24-DEC-97 15-NOV-98
    Himuro                    15-NOV-98 10-AUG-99
    Colmenares                10-AUG-99
    ```

* trim 
    * trim leading or trailing characters
    * `TRIM( [ [ LEADING | TRAILING | BOTH ] trim_char FROM ] string)`
    * `[ LEADING | TRAILING | BOTH ]` is optional, `BOTH` by default
    * `trim_char` specifies the character to be removed, if none specified, space by default 
    * 
* substr
    * returns substring starting from `position` with length `substring_length`
    * `SUBSTR( str, position [, substring_length] );`
    * `position`
        * 0 -> treated as 1
        * positive -> counts from left to right
        * negative -> counts from right to left (backwards)
    * if `substring_length` is omitted -> returns to end of string
* instr
    * search for substring in a string and returns the index of the first occurrence
    * `INSTR(string , substring [, position [, occurrence]])`
    * `position` -> integer that indicates at what position the search should start (pos -> left to right, neg -> right to left, backwards); default 1
    * `occurrence` -> determines which occurrence to search for, default 1 (first occurence)

    
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
        * dependency (through method parameter, class variable, etc): shown by dashed line and flat arrow
        * association:
        * aggregation: 
        * composition: 