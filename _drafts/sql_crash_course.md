---
layout: post
title: SQL Crash Course
subtitle: Quick overview of the basics
date: 2022-02-09 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "Database"
tags: [sql, oracle, database]
---

### Select

Let's say this is our table.

| CUSTOMERS |
| --- |
| FIRST_NAME<br>LAST_NAME<br>BIRTHDAY<br>ADDRESS<br>AGE |


The basic format is:
```sql
SELECT exp FROM table_name [WHERE condition];
```

`exp`: use * for selecting all columns, or list the specific columns you want  
`table_name`: at least one table required[^1]  
`condition`: returns all rows if no condition is used

ex)
```sql
SELECT * FROM customers;
SELECT first_name, last_name FROM customers;
SELECT first_name, last_name FROM customers WHERE age > 20;
```


[^1]: If multiple tables are used without any join operations, it will simply do a cross join (or a [cartesian product](https://en.wikipedia.org/wiki/Cartesian_product)) to create all possible combinations.
