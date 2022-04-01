---
layout: post
title: SQL Crash Course
subtitle: Quick overview of the basics
date: 2022-02-18 19:54:00 +0900
background: '/img/bg-post.jpg'
category: "Database"
tags: [sql, oracle, database]
---

_**Note**: syntax will be based on Oracle SQL_

### SELECT

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
SELECT first_name, last_name FROM customers
  WHERE age > 20;
```

If you want to return only distinct values, you can use `SELECT DISTINCT` instead.

### WHERE
The `WHERE` clause is used to filter the records and extract only the ones that meet a certain condition. This can be used for all `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements.

Strings must be enclosed in single quotes, while numbers do not.
```sql
SELECT * FROM customers WHERE first_name = 'Jack';
SELECT * FROM customers WHERE age = 1;
```

You can also use multiple conditions using `AND` and `OR`.
```sql
SELECT * FROM customers
  WHERE first_name = 'John' AND age > 20;
SELECT * FROM customers
  WHERE first_name = 'John' AND (age < 10 OR age > 30);
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

<br>
### IN
Mostly used to avoid using multiple `OR` conditions.

```sql
SELECT * FROM customers
  WHERE first_name = 'Jack'
    OR name = 'John'
    OR name = 'Jane';
```

is equivalent to

```sql
SELECT * FROM customers
  WHERE first_name IN ('Jack', 'John', 'Jane');
```

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
As mentioned above, this operator is used with a subquery, where the condition is met if the subquery returns at least one row. A subquery is a select statement that is nested inside another query (more info below).

Say we have another table called ACCOUNTS.  

| ACCOUNTS |
| --- |
| CUSTOMER_ID<br>USERNAME<br>PASSWORD |

We can then query something like this:
```sql
SELECT username FROM accounts
  WHERE EXISTS (SELECT * FROM customers
                WHERE customers.customer_id = accounts.customer_id);
```
And it will return all the usernames where it has matching customer_id in both tables.

*Note:* The query above can be similarly achieved with an inner join, such as:
```sql
SELECT username FROM customers c
  INNER JOIN accounts a ON c.customer_id = a.customer_id;
```

The difference is that the one using `EXISTS` simply returns results from the CUSTOMERS table when the condition matches and the `INNER JOIN` combines two tables first and returns results from the combined table. Having duplicates can lead to having repeated rows if the inner join is used.

### Subqueries
Subqueries can be used inside `SELECT`, `WHERE`, and `FROM` clauses.

It executes the inner subquery first and uses that result to perform the outer queries.

```sql
SELECT username FROM accounts a
  WHERE a.customer_id IN
    (SELECT c.customer_id FROM customers c
      WHERE c.age > 20);
```
It first executes the subquery to obtain the results. Let's say the customer id for those above the age of 20 turned out to be 1, 5, 7, and 30. Now the outer query will try to find records that have a match with these customer ids.

Note that there can be multiple nested subqueries. But there is a limit of 255 levels of subqueries for the `WHERE` clause, and no limit for the `FROM` clause. (This is for Oracle SQL)

### ORDER BY
This is used to sort the results, and it can only be used with `SELECT` queries.

```sql
SELECT * FROM customers ORDER BY customer_id;
```

It will order the results in ascending order by default even if you don't use the `ASC` keyword. For descending order, use the keyword `DESC`.

You can also use multiple columns.

```sql
SELECT * FROM customers ORDER BY age, customer_id DESC;
SELECT * FROM customers ORDER BY age ASC,
  customer_id DESC; /* This is also possible */
```

This will simply use the following columns as the next sorting condition. So for the query above, if two rows have the same age, it will then sort by customer_id.

### GROUP BY
This clause is used for grouping results based on matching values in specified columns, and usually in conjunction with an aggregate function (e.g. SUM, COUNT, MIN, MAX, AVG).

The syntax is as follows:
```sql
SELECT exp1, exp2, ...
    agg_func1(agg_exp1), agg_func2(agg_exp2), ...
    [WHERE conditions]
    GROUP BY exp1, exp2, ...;
```
`exp1, exp2, ...`: must be included in the `GROUP BY` clause, and excluded from the aggregate functions

The reason why you don't want the same columns in the `GROUP BY` as in the aggregate functions is because it wouldn't make sense to perform some aggregate function on the rows in which all the values are the same. If you're grouping by "age", for example, and you try to get the max age value from a group of people with the same age, you'd just get the same value.

I guess the only aggregate function that would make sense would be `COUNT`, as that will return the count number for each group value.

Here's an example.

```sql
SELECT age, COUNT(customer_id) GROUP BY age;
SELECT age, COUNT(age)
  GROUP BY age; /* this also works */
SELECT age, customer_id
  GROUP BY age; /* this returns an error */
```

You can also group by multiple columns. So if we group by both age and gender, it will return all the existing combinations of the two columns.
So for the example below:

| customer_id | age | gender |
| --- | --- | --- |
| 1 | 20 | M |
| 2 | 20 | F |
| 3 | 25 | M |
| 4 | 25 | M |

```sql
SELECT age, gender, COUNT(customer_id) as count
  GROUP BY age, gender;
```

The result will be:

| age | gender | count |
| --- | --- | --- |
| 20 | M | 1 |
| 20 | F | 1 |
| 25 | M | 2 |

<br>

### JOIN

#### Inner Join  
Inner join is probably the most common type of join you'll be using. It returns results in which the condition is met for both tables. If we look at them in a venn diagram, we're talking about the middle overlapping area, where the two tables intersect.

```sql
SELECT customers.first_name, customers.last_name, accounts.username
  FROM customers INNER JOIN accounts
  ON customers.customer_id = accounts.customer_id;
```
So only the rows that have matching customer ids in both tables will be returned. The keyword `INNER` is optional.

There's another way to perform this inner join, using the older syntax.
```sql
SELECT customers.first_name, customers.last_name, accounts.username
  FROM customer, accounts
  WHERE customers.customer_id = accounts.customer_id;
```

You can also use the `USING` instead of `ON`, but this is only true for **equijoins** (join conditions using an equality operator):
```sql
SELECT customers.first_name, customers.last_name, accounts.username
  FROM customers INNER JOIN accounts
  USING (customer_id);
```

#### Outer Join
We have left outer join and right outer join. Left outer join will return all of the rows from the left table, and only those that match the join condition from the right table.
The opposite will be true for the right outer join.

This can result in some rows with null values.
```sql
SELECT customers.first_name, customers.last_name, accounts.username
 FROM customers LEFT OUTER JOIN accounts
 ON customers.customer_id = accounts.customer_id;
```
Use `RIGHT OUTER JOIN` for right join.

Note that we can achieve right join using the `LEFT OUTER JOIN` by simply switching the order of tables. So the following query is equivalent to the one above.
```sql
SELECT customers.first_name, customers.last_name, accounts.username
 FROM accounts RIGHT OUTER JOIN customers
 ON customers.customer_id = accounts.customer_id;
```

You can also perform join operations on multiple columns or conditions.   
`ON t1.col1 = t2.col2 AND t1.col2 = t2.col2 ...`  
or  
`USING (col1, col2, ...)`  

There's also a **full outer join**, or a full join, where you combine both tables, regardless of whether on not they have a match. So in terms of the venn diagram, we're talking about the entire thing. The syntax is the same, but use the keyword `FULL JOIN` instead.

### INSERT
This statement is used to insert records into a table. The basic syntax is:
```sql
INSERT INTO table_name (col1, col2, ...)
  VALUES (val1, val2, ...);
```
You can omit the comma-separated columns, but then you have to provide the values for all the columns in their respective orders. Not good practice. Also, certain values that have a default value or can be NULL can be omitted.

You can also use `SELECT` in conjunction with `INSERT` to insert multiple values into a table. This is especially useful for copying data into another table.
```sql
INSERT INTO table_name (col1, col2, ...)
  SELECT exp1, exp2, ...
    FROM source_table;
```
This will copy the values obtained from `exp1` and `exp2` into `col1` and `col2`, respectively. You can use literals instead of columns for the `exp` to set a constant value.

So let's say `col2` takes in a number, and instead of `exp2`, we input the value `0`. Then all the rows will have the value 0 for `col2`.
```sql
INSERT INTO table_name (col1, col2)
  SELECT exp1, 0
    FROM source_table;
```

For inserting multiple rows into one or multiple tables using a single statement, use the following syntax:
```sql
INSERT ALL
  INTO table_name (col11, col12, ...) VALUES (val11, val12, ...)
  INTO table_name (col21, col22, ...) VALUES (val21, val22, ...)
  INTO table_name2 (col31, col32, ...) VALUES (val31, val32, ...)
  [subquery];
```
This is the same as using 3 separate `INSERT INTO` statements.

Notice that this statement requires a subquery. The values from `val11`, `val12`, `val21`, ... must correspond to the values obtained from the subquery. If you want to use the values stated in `val11`, `val12`, `val21`, ... as the literal values, then simply use `SELECT * FROM dual` for the subquery.

For instance, say we have two new tables, called USERS1 and USERS2, with only 2 columns, `FIRST_NAME` and `LAST_NAME`. We have another table, CUSTOMERS, with all the user information and we want to copy them into these two new tables. We can do the following.
```sql
INSERT ALL
  INTO users1 (first_name, last_name) values (user_first_name, user_last_name)
  INTO users2 (first_name, last_name) values (user_first_name, user_last_name)
  SELECT user_first_name, user_last_name FROM customers;
```
But say we only want to insert using the values themselves, without a subquery.
```
INSERT ALL
  INTO users1 (first_name, last_name) values ('Elon', 'Musk')
  INTO users2 (first_name, last_name) values ('Jack', 'Ma')
  SELECT * FROM dual;
```

What is a dual table, you ask?
> DUAL is a small table in the data dictionary that Oracle Database and user-written programs can reference to guarantee a known result. The dual table is useful when a value must be returned only once, for example, the current date and time. All database users have access to DUAL.

You can think of it as a dummy query for this case.

You can find more info [here](https://docs.oracle.com/cd/E11882_01/server.112/e40540/datadict.htm#CNCPT1210) or check out this [post](https://asktom.oracle.com/pls/apex/f?p=100:11:0::::P11_QUESTION_ID:1562813956388).

**Important**: Remember to use `commit;` after inserting all the rows to make the changes permanent.

### UPDATE
Use this statement to update existing records in a table.
```sql
UPDATE table_name
  SET
    col1 = val1,
    col2 = val2,
    ...
  WHERE condition;
```
So we could do something like this:
```sql
SELECT customers
  SET age = 30
  WHERE customer_id = 1;
```


---
[^1]: If multiple tables are used without any join operations and without any common columns used in the WHERE clause, it will simply do a cross join (or a [cartesian product](https://en.wikipedia.org/wiki/Cartesian_product)) to create all possible combinations. This is rarely used, so if you get this type of join unintentionally, double-check your syntax.  
[^2]: `WHERE age BETWEEN 20 and 30` is equal to `WHERE age >= 20 AND age <= 30`
