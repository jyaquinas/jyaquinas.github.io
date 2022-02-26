---
layout: post
title: What is Gradle?
subtitle: Building projects with Gradle
date: 2022-02-24 23:39:00 +0900
background: '/img/bg-post.jpg'
category: "Gradle"
tags: [build tool, gradle, java]
---

### What is Gradle?
Gradle is a general build tool that supports various languages, such as java, groovy, kotlin, scala, c++, etc. 

You can easily manage your project dependencies through the 'build.gradle' file. Groovy will automatically download the necessary components specified in the script. The script can be written in Groovy or Kotlin.

There are different ways to initialize your project with gradle. One is through the cli command `gradle init`. If you're using IntelliJ, you can simply create a new project using gradle. If you're using spring, you can also download the starter project file through [spring initializr](https://start.spring.io/).

Here are the basic components of the 'build.grade' file.

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
`dependencies` is where you decide which dependencies and versions your project will need. There are [different configurations](https://docs.gradle.org/current/userguide/java_plugin.html#sec:java_plugin_and_dependency_management) you can use for this. 

### Tasks
Tasks can also be defined in the file, which will execute during the build. They can be explicitly defined in the script, or they can automatically be added through the plugins. 

### Error Messages
If you want to get more detailed error messages, create a new file named 'gradle.properties' in the same directory as 'build.gradle' and add the following line:
```groovy
org.gradle.warning.mode=all
```

