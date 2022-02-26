---
layout: post
title: Using Spring Data JPA
subtitle: Object Relational Mapping in Java
date: 2022-02-27 01:06:00 +0900
background: '/img/bg-post.jpg'
category: "java"
tags: [java, spring, jpa, orm]
---

### What is Java Persistence API (JPA)?
Let's first define [persistence](https://en.wikipedia.org/wiki/Persistence_(computer_science)).
> The characteristic of the state of a system that outlives (persists more than) the process that created it. 

Data is typically persisted by storing them in databases. So the JPA is a java specification that provides basic rules for implementing object-relational mapping (ORM). That means that JPA doesn't do any of the work. Instead, ORM tools like Hibernate implement the JPA specifications. 

### Why use ORM?
You can increase the development speed by avoiding repetitive code, such as the code responsible for mapping objects to the database. There are also fewer chances of error by not having to handle raw queries. And by only dealing with java objects, you can still use OOP-style programming without having to worry about mapping each to the DB.

### Using Spring Data JPA
Spring Data JPA is another abstraction layer that is meant to facilitate the use of JPA, more specifically the JPA provider like Hibernate. So Spring Data JPA is not a JPA provider.

### Annotations
#### @Entity
Defines an entity class, which is basically a POJO (Plain old java object) that represents a table in a database. Instances of this class represent rows of the table. The name of the entity defaults to the class name, but it can be set differently through `@Entity(name="EntityName")`.

#### @Id
Specifies the field as PK (primary key).

#### @GeneratedValue
Specifies the PK generation strategy. If you want to use the auto-increment option, you must set the strategy as:  
`@GeneratedValue(strategy=GenerationType.IDENTITY)`

#### @Column
All the fields of the class become a column by default. But you can use this to set different options other than the default values. For instance, the name will default to the field name, and to a length of 255 (for string columns only).


Let's look at an example of an entity class.
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
