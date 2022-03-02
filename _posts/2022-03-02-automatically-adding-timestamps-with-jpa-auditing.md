---
layout: post
title: Automatically Adding Timestamps With JPA Auditing
subtitle: In-memory Database for Testing
date: 2022-03-02 22:06:00 +0900
background: '/img/bg-post.jpg'
category: "Java"
tags: [jpa, java, spring]
---

### What is JPA Auditing?
JPA Auditing automatically tracks and logs events whenever there is a change in our entities. This can be used to automatically generate *created* or *last updated* timestamps.

### Why use JPA auditing?
It's fairly simple to automatically add timestamps for columns such as 'DATE_CREATED' or 'DATE_MODIFIED' in databases. But if we want to implement this through our entities, we would have to manually add such fields for all of our entities, which would lead to lots of repetitive code. 

Spring Data makes this easier for us through JPA Auditing. 

### Setting up JPA
We first want to enable JPA auditing by adding the annotation `@EnableJpaAuditing` in our main application class.

Since this timestamp property can be used by multiple entities, we will simply implement a separate base class for these. 

We use the `@EntityListener` annotation to specify the callback listener class. `AuditingEntityListener` is a JPA entity listener class provided by Spring Data.

```java
@Getter
@MappedSuperclass   // mapping info will be applied to entities that inherit from this class
@EntityListeners(AuditingEntityListener.class)  // adds auditing functionality
public class BaseTimeEntity {

    @CreatedDate // automatically saves time when entity is created
    private LocalDateTime createdDate;

    @LastModifiedDate   // automatically saves time when entity is modified
    private LocalDateTime modifiedDate;

}
```

Now, our entity classes simply have to extend this base class to have these properties. We can access the dates through functions like `getCreatedDate()` or `getModifiedDate()`.
