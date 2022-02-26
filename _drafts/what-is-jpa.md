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
JPA is a java specification that provides basic rules for implementing object-relational mapping (ORM). That means that JPA doesn't do any of the work. Instead, ORM tools like Hibernate implement the JPA specifications. 

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
Specifies the PK (primary key) field. 
:blush: