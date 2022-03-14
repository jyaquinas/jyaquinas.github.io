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

* Dirty checking - JPA entity
    * https://jojoldu.tistory.com/415
    * https://www.netsurfingzone.com/hibernate/dirty-checking-in-hibernate/
    * automatically checks if objects have been modified and will update regularly (when session flushed or transaction is commited)

* why pass .class
* look into index.js file (mustache)
    * ajax
    * CRUD -> html func (post, get, put, delete)

* spring.profiles.include -> application.properties 
* application.properties vs yaml
* how oauth2 works 
    * https://developers.google.com/identity/protocols/oauth2
* What is tomcat?
    * lightweight server - web server and servlet container (not a full application server) written in java -- is production ready
* session persistence methods
    * use tomcat sessions - but if multiple tomcat servers are used, extra configuration is required to synchronize user sessions across servers
    * saving sessions to DB - but high login rates may create performance issues (due to high request to db)
    * using caches (redis memcached) - mostly used in applications with large user base
* creating annotations in java?
    * https://docs.oracle.com/javase/tutorial/java/annotations/declaring.html


---
## Misc Subjects
* What is java bean?
    * objects that are managed by spring IoC container
* Linux wildcards -> file searching
    * `*` match one or more occurrences of characters, including none
    * `?` match single occurrence of character
    * `[]` match any occurrence of characters in the enclosed bracket
    * ./tmp/* matches files and folders in ./tmp
    * ./tmp/** matches files, folders, and subfolders in ./tmp
    * https://stackoverflow.com/questions/3529997/unix-wildcard-selectors-asterisks
* for large projects with more complex data, it may be required to perform complex join operations for obtaining/searching for data
    * it is common to use spring data jpa for CUD operations, and use other frameworks for read operations (querydsl, jooq, mybatis)
* Shell 
    * ps -> lists processes
        * https://linuxize.com/post/ps-command-in-linux/
        * https://www.geeksforgeeks.org/ps-command-in-linux-with-examples/
        * https://www.oreilly.com/library/view/linux-pocket-guide/9780596806347/re87.html
        * -e: list full process list
        * -f: full format
        * -p: get for a particular process `ps -p 5553`
        * can be used with filter commands like `grep`
    * awk
        * https://www.geeksforgeeks.org/awk-command-unixlinux-examples/
        * `awk '{print $2, $4}'` : prints 2nd and 4th word (whitespace separated) -> $0 represents entire line
        * by default `awk {print} filename.txt` prints entire file line by line
    * tput
        * https://linuxcommand.org/lc3_adv_tput.php
        * can manipulate the terminal's appearance, like color, etc
        * `tput smso` start 'standout' mode
        * `tput rmso` end 'standout' mode
        * `tput sgr0` turn off all attributes
    * set -> csh?
        * https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-linux
        *  we will get a list of all shell variables, environmental variables, local variables, and shell functions
    * `$$`
        * https://tldp.org/LDP/abs/html/internalvariables.html
        * process id of script itself
    * assigning results of a command to a variable
        * wrap around ``
        * `` array=`find . -maxdepth 1 -name '*.txt'` ``
        * results are saved into the array variable
        * use the command `set` in csh
            * `` set array=`find . -maxdepth 1 -name '*.txt'` ``
    * find maxdepth
        * https://www.geeksforgeeks.org/mindepth-maxdepth-linux-find-command-limiting-search-specific-directory/
* Crontab 
    * https://www.adminschoice.com/crontab-quick-reference
    * https://www.cyberciti.biz/faq/how-do-i-add-jobs-to-cron-under-linux-or-unix-oses/
    * https://opensource.com/article/17/11/how-use-cron-linux
    * files used to schedule the execution of programs 
    * 
* Shell scripts
    * .sh files that usually have [shebangs](https://en.wikipedia.org/wiki/Shebang_(Unix)) on the first line
    * `#!/bin/bash` or `#!/bin/csh`
    * to run the scripts:
        * `./scriptname.sh`, `sh scriptname.sh`, `bash scriptname.sh`
    * make sure you have the executable permission, or update it using `chmod`
    * loops and ifs?
        * https://linuxconfig.org/bash-scripting-tutorial

* Bash (bourne again shell) vs sh (bourne shell)
    * what is shell? a CLI (command line interpreter) program that provides interface between user and os service
        * lets you run linux commands
        * sh converts human readable commands and converts them to commands for kernel
    * sh with more features
    * bash scripting is only for bash, but sh scripting is for any shell
    * bash is the default SHELL (can check in your linux by `ps -p $$`)

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

