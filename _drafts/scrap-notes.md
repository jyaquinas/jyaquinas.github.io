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
    * set
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
* 
        
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
    
