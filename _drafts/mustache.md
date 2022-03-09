---
layout: post
title: Mustache
subtitle: 
date: 2022-03-03 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "java"
tags: [mustache, java]
---

### What Is a Template Engine?
* generate data from the server, convert to html, then sent to browser for display?


### What is Mustache?
* template engine, supports multiple languages
* server template engine in java, client template engine in js
* other template engines:
    * jps, velocity, freemarker, thymeleaf
* pros:
    * relatively simple syntax
    * same syntax for client/server templates (mustache.js, mustache.java)
    * no logic code? easy to separate view and server
    * supported in intellij community version
    
### Setup
* add `implementation 'org.springframework.boot:spring-boot-starter-mustache'` to the dependencies in build.gradle file
* mustache files should be located in src/main/resources/templates so that spring boot can automatically detect them


Notes.  
* use `{{>}}` to bring another file into the current file, such as `{{>layout/header}}`


---
links:
* https://www.baeldung.com/mustache
