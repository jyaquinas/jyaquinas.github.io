---
layout: post
title: ---
subtitle: ---
date: 2022-02-22 22:03:00 +0900
background: '/img/bg-post.jpg'
category: ""
tags: []
---

* What is java bean?
    * objects that are managed by spring IoC container

* for large projects with more complex data, it may be required to perform complex join operations for obtaining/searching for data
    * it is common to use spring data jpa for CUD operations, and use other frameworks for read operations (querydsl, jooq, mybatis)

* Dirty checking - JPA entity
    * https://jojoldu.tistory.com/415
    * https://www.netsurfingzone.com/hibernate/dirty-checking-in-hibernate/
    * automatically checks if objects have been modified and will update regularly (when session flushed or transaction is commited)

* changing default java version 
    * `sudo /usr/sbin/alternatives --config java`, then select java version
    * check with `java -version`

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

