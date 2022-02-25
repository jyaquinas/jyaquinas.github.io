---
layout: post
title: What is Lombok?
subtitle: Be more productive with less boilerplate code
date: 2022-02-25 12:55:00 +0900
background: '/img/bg-post.jpg'
category: "java"
tags: [java, lombok]
---

### What is Lombok?
Lombok is a java library that helps reduce boilerplate code, such as getters and setters, by automatically generating them at compile time. So because it's not in our source code, it saves space and improves readability.

### Using Lombok with Gradle
Add these 2 lines for your dependencies in your 'build.gradle' file. 

Also, make sure that the *Enable annotation processing* check box is ticked. You can find it in Preferences -> Build, Execution, Deployment -> Compiler -> Annotation Processors.

```groovy
dependencies {
    implementation 'org.projectlombok:lombok'
    annotationProcessor 'org.projectlombok:lombok'
}
```

### @Getters and @Setters
You can use the `@Getter` and `@Setter` annotations both at the class and field levels. 

```java
public class Person{
    @Getter @Setter private String name;
    @Getter private Integer age;
}
```

This will generate a `getName()`, `setName()`, and a `getAge()` function. These will be public by default. You can specify the access level (`PUBLIC`, `PROTECTED`, `PACKAGE`, or `PRIVATE`) like this:  
`@Setter(AccessLevel.PROTECTED)`

If it's used at the class level, it will generate getters and setters for all the non-static variables in the class. 

```java
@Getter @Setter
public class Person{
    private String name;
    private Integer age;
}
```


### @NoArgsConstructor
This automatically generates a constructor with no arguments. 

### @RequiredArgsConstructor
This generates a constructor with required arguments, with those arguments being variables with the `final` field or with `@NonNull` constraints. 

```java
@RequiredArgsConstructor
public class Person{
    private final String name;
    private Integer age;
    // Person(String Name)
}
```

### @AllArgsConstructor
This will create a constructor that requires arguments for all the fields in the class, and will initialize them with the given values.

```java
@AllArgsConstructor
public class Person{
    private String name;
    private Integer age;
    // Person(String Name, Integer age)
}
```

### @ToString
It will automatically implement `toString()` and print out the class name, with all the fields and their values, separated by a comma.

```java
@ToString
@AllArgsConstructor
public class Person{
    private String name;
    private Integer age;
    // If we initialize Person("John", 20)
    // toString() returns "Person(name=John, age=20)"
}
```

### @Data
Using `@Data` is the same as using `@Getter @Setter @EqualsAndHashCode @ToString @RequiredArgsConstructor` all at the same time. It bundles all of these into a single annotation. So if you don't intend on using them all, just use the specific annotations that you need.