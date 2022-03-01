---
layout: post
title: Using H2 Database with Spring and Gradle
subtitle: In-memory Database for Testing
date: 2022-03-02 08:45:00 +0900
background: '/img/bg-post.jpg'
category: ""
tags: []
---

H2 Database is a in-memory database that is typically used for testing.

### Setup
Add the h2database dependency in your 'build.gradle' file.

```groovy
dependencies {
    implementation 'com.h2database:h2'
}
```

If you don't have an 'application.properties' under src -> main -> resources, add one. 

Add the following lines:

`spring.h2.console.enabled=true`  

This will let you access the DB through the console. You can access it through this link:  
localhost:8080/h2-console

`spring.datasource.url=jdbc:h2:mem:testdb
`. 

This specifies the JDBC url you need to use for connecting to the DB. If this is not set, it will be automatically generated for you. You can then find the url in the console output, something like this:

```shell
2022-02-27 21:02:53.192  INFO 5544 --- [           main] o.s.b.a.h2.H2ConsoleAutoConfiguration    : H2 console available at '/h2-console'. Database available at 'jdbc:h2:mem:867794d1-6dd5-4b6e-a1f1-afeb1368f399'
```

The default username will be `sa` with no password. 