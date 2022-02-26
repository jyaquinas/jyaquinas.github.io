---
layout: post
title: What is JPA?
subtitle: Object Relational Mapping in Java
date: 2022-02-22 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "java"
tags: [java, spring, jpa, orm]
---

### What is Java Persistence API (JPA)?
Let's first define [persistence](https://en.wikipedia.org/wiki/Persistence_(computer_science)).
> The characteristic of state of a system that outlives (persists more than) the process that created it. 

Data is typically persisted by storing them in databases. So the JPA is a java specification that provides basic rules for implementing object-relational mapping (ORM). That means that JPA doesn't do any of the work. Instead, ORM tools like Hibernate implement the JPA specifications. 

### Why use ORM?
* reduce repetitive code
* speed up development
* focus of OOP style programming without worrying about how to map each to the DB
* less chances of error by not handling raw queries

### Spring Data JPA
* wrapper class to facilitate use of JPA, more specifically the JPA provider like Hibernate (not a JPA provider)
* recommended over using hibernate or jpa
* easily switch between databases without modifying entire code base (due to the use of same CRUD operations in the interfaces)
* JPA data access abstraction? -> requires some JPA provider, like Hibernate

### Annotations
#### @Entity
Defines an entity class, which is basically a POJO (Plain old java object) that represents a table in a database. Instances of this class represent rows of the table. Name of the entity defaults to the class name, but it can be set differently through `@Entity(name="EntityName")`.

#### @Id
Specifies the field as PK (primary key).

#### @GeneratedValue
Specifies the PK generation strategy. If you want to use the auto increment option, you must set the strategy as:  
`@GeneratedValue(strategy=GenerationType.IDENTITY)`

#### @Column
All the fields of the class become a column by default. But you can use this to set different options other than the default values. For instance, the name will default to the field name, and to a length of 255 (for string columns only).


Let's look at an example.
```java
@Getter
@NoArgsConstructor
@Entity // defines an entity class -> represents DB table
public class Posts {

    @Id // specifies PK field
    @GeneratedValue(strategy = GenerationType.IDENTITY) // specifies rule for PK generation. IDENTITY -> auto increment option
    private Long id;

    @Column(length = 500, nullable = false)
    private String title;

    @Column(columnDefinition = "TEXT", nullable = false)
    private String content;

    // uses default column settings if not specified
    private String author;

    @Builder
    public Posts(String title, String content, String author) {
        this.title = title;
        this.content = content;
        this.author = author;
    }
```

### Why not use @Setter?
* instead of setting value directly, set through methods whose objectives are clear and specific, such as setBoolToFalse() instead of setBool(bool val)

