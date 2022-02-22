---
layout: post
title: What is Gradle?
subtitle: Building projects with gradle
date: 2022-02-21 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "gradle"
tags: [build tool, gradle, java]
---

### What is Gradle?

* general build automation tool
* supports various languages, such as java, groovy, kotlin, scala, c+, swift
* built on JVM
* build scripts written in groovy or kotlin
* helps you with dependency management - [link](https://docs.gradle.org/current/userguide/core_dependency_management.html#dependency_management_in_gradle)

You can manage your project dependencies through the build.gradle file.

Here are the basic components.

```groovy
plugins {
    id 'java' 
    id 'org.springframework.boot' version '2.6.3'
    id 'io.spring.dependency-management' version '1.0.11.RELEASE'    
}

repositories {
    mavenCentral() 
}

dependencies {
    implementation 'org.springframework.boot:spring-boot-starter-web'
    implementation 'junit:junit:4.13.1'

    testImplementation 'org.springframework.boot:spring-boot-starter-test'

}
```

### Plugins
Plugins add extra functionalities to your gradle build. For instance, adding the java plugin will add gradle tasks that will help you with your java development, such as compiling, testing, or generating java docs. You can check out more info [here](https://docs.gradle.org/current/userguide/java_plugin.html#header)

You can either use [core plugins](https://docs.gradle.org/current/userguide/plugin_reference.html) or other [free Gradle plugins](https://plugins.gradle.org/).



### Repositories
`repositories` is where you tell Gradle to download it from.  

### Dependencies
`dependencies` is where you decide which dependencies and versions your project will need. There are different configurations you can use in here. [link](https://docs.gradle.org/current/userguide/java_plugin.html#sec:java_plugin_and_dependency_management)

### Tasks
--



---
ref
* https://tomgregory.com/gradle-tutorial-for-complete-beginners/
* https://tomgregory.com/anatomy-of-a-gradle-build-script/




