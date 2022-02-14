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
| CUSTOMER_ID<br>FIRST_NAME<br>LAST_NAME<br>BIRTHDAY<br>ADDRESS<br>AGE |


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

If you want to return only distinct values, you can use `SELECT DISTINCT` instead.

### Where
The `WHERE` clause is used to filter the records and extract only the ones that meet a certain condition. This can be used for all `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements.

Strings must be enclosed in single quotes, while numbers do not.
```sql
SELECT * FROM customers WHERE first_name = 'Jack';
SELECT * FROM customers WHERE age = 1;
```

You can also use multiple conditions using `AND` and `OR`.
```sql
SELECT * FROM customers WHERE first_name = 'John' AND age > 20;
SELECT * FROM customers WHERE first_name = 'John' AND (age < 10 OR age > 30);
```

These are the comparison operators that can be used with `WHERE`:  

| Operator | Description |
| --- | --- |
| = | Equal |
| <> or != | Not equal |
| > | Greater than |
| >= | Greater than or equal to |
| < | Less than |
| <= | Less than or equal to |
| NOT | negate a condition |
| BETWEEN | Between a range (inclusive)[^2] |
| IS NULL | is NULL value |
| NOT NULL | is  non-NULL value |
| IN() | Matches a value inside the IN, mostly used to avoid using multiple OR conditions |
| LIKE | Pattern matching |
| EXISTS() | True if subquery returns at least one row |  


### IN
Mostly used to avoid using multiple `OR` conditions.

`SELECT * FROM customers WHERE first_name = 'Jack' OR name = 'John' OR name = 'Jane';` is equivalent to   
`SELECT * FROM customers WHERE first_name IN ('Jack', 'John', 'Jane);`

### LIKE
This operator is used in a `WHERE` clause for pattern matching using the following wildcards:
* `'%'`: represents any character of any length, including the length of zero
* `'_'`: represents a single character

Here are a few examples:  

| Expression | Example matches |
| --- | --- |
| `'a%'` | apple, at, a, are |
| `'%s'` | cars, mats, bats, s |
| `'c_t'` | cat, cot, cut |
| `'_r%'` | arp, art, articulate, bracket |


*Note: This also works with numbers. `WHERE num LIKE '32_'` will find 320, 321, 322, 323...*

### EXISTS
As mentioned above, this operator is used with a subquery, where the condition is if the subquery returns at least one row. A subquery is a select statement that is nested inside another query.

Say we have another table USERNAME.
| ACCOUNTS |
| --- |
| CUSTOMER_ID<br>USERNAME<br>PASSWORD |

We can then query something like this:
```sql
SELECT username FROM accounts WHERE EXISTS (SELECT * FROM customers WHERE customers.customer_id = accounts.customer_id);
```
And it will return all the usernames where it has matching customer_id in both tables.

*Note:* The query above can be similarly achieved with an inner join, such as:
```sql
SELECT username FROM  customers c INNER JOIN accounts a ON c.customer_id = a.customer_id;
```

The difference is that the one using `EXISTS` simply returns results from the CUSTOMERS table when the condition matches, and the `INNER JOIN` combines two tables first and returns results from the combined table. Having duplicates can lead to having repeated rows if the inner join is used.

### Subqueries

### ORDER BY

### GROUP BY

### JOIN




---
[^1]: If multiple tables are used without any join operations, it will simply do a cross join (or a [cartesian product](https://en.wikipedia.org/wiki/Cartesian_product)) to create all possible combinations.
[^2]: `WHERE age BETWEEN 20 and 30` is equal to `WHERE age >= 20 AND age <= 30`
