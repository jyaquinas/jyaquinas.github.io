---
layout: post
title: 'Lombok: Be More Productive With Less Boilerplate Code'
subtitle: Lombok Basics
date: 2022-02-25 12:55:00 +0900
background: '/img/bg-post.jpg'
category: "Java"
tags: [java, lombok]
---

### What is Lombok?
Lombok is a java library that helps reduce boilerplate code, such as getters and setters, by automatically generating them at compile time. So because it's not in our source code, it saves space and improves readability.

### Why use Lombok?
Aside from improving code readability, it really helps not to have to edit all the constructors, getters/setters, and other boilerplate code every time there is a small change, which can happen a lot, especially during the early development phase. 

### Using Lombok with Gradle
Add these 2 lines for your dependencies in your 'build.gradle' file. 

Also, make sure that the *Enable annotation processing* check box is ticked. You can find it in Preferences -> Build, Execution, Deployment -> Compiler -> Annotation Processors.

```groovy
dependencies {
    implementation 'org.projectlombok:lombok'
    annotationProcessor 'org.projectlombok:lombok'
}
```
### Annotations
#### @Getters and @Setters
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

#### @NoArgsConstructor
This automatically generates a constructor with no arguments. 

#### @RequiredArgsConstructor
This generates a constructor with required arguments, with those arguments being variables with the `final` field or with `@NonNull` constraints. 

```java
@RequiredArgsConstructor
public class Person{
    private final String name;
    private Integer age;
    // Person(String Name)
}
```

#### @AllArgsConstructor
This will create a constructor that requires arguments for all the fields in the class, and will initialize them with the given values.

```java
@AllArgsConstructor
public class Person{
    private String name;
    private Integer age;
    // Person(String Name, Integer age)
}
```

#### @ToString
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

#### @Data
Using `@Data` is the same as using `@Getter @Setter @EqualsAndHashCode @ToString @RequiredArgsConstructor` all at the same time. It bundles all of these into a single annotation. So if you don't intend on using them all, just use the specific annotations that you need.

#### @Builder
This allows the class to be constructed using a [builder pattern](https://refactoring.guru/design-patterns/builder). 

```java
public class Person{
    private String name;
    private Integer age;
    
    @Builder
    public Person(String name, Integer age){
        this.name = name;
        this.age = age;
    }
}
```

So for the example above, we would be able to construct a class like this:   

```java
Person person = Person.builder()
        .name("John")
        .age(20)
        .build();
```
Of course, this would be more effective for classes with lots of fields so that we can avoid having monstruous constructors with tons of parameters. This also makes it easier to see what values correspond to which parameters, as opposed to using the typical constructors and having to input them in a specific order.