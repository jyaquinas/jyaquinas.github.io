---
layout: post
title: SQL Tuning Tips
subtitle: Simple tricks you can use to improve your query performance
date: 2022-06-08 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "Database"
tags: [database, sql, oracle]
---

### Use Indexes
Using indexes is one of the best ways to improve your query performance. A lot of the tuning tips involve making changes to the query so that the optimizer will make use of indexes. Keep in mind that creating new indexes on large tables can be very time consuming, so this should be taken into consideration during the design process, when the table is first created.

Check out these posts for more information about the [types of indexes]({% link _posts/2022-05-22-types-of-oracle-db-indexes.md %}) or the different types of [access paths]({% link _posts/2022-05-16-oracle-sql-access-paths.md %}) that the optimizer uses.

If you have an index but the optimizer is not using it, try to use optimizer hints. You can find more info about hints [here](https://docs.oracle.com/cd/B19306_01/server.102/b14211/hintsref.htm#i17496);

```sql
SELECT /*+ INDEX(table_name index_name) */ col1 
    FROM table_name
    WHERE [condition];
```

Also, check if your `WHERE` clause is using all of the columns that make up your index (if you index is made up of multiple columns). Remember that the order of the columns in a composite index matters.

### Avoid Using SELECT *
Only query for the columns that you need. Using the `SELECT *` statement is typically not good practice. Not only does the database need to check the data dictionary to check which columns are available for the specific table, it can reduce the query performance by doing unnecessary extra work. 

If your table has an index on certain columns and you query for only those columns, the optimizer will use the index for better performance. But if you query for all the columns, the optimizer might decide to go for a full table scan instead. If you query for a non-indexed column very often, consider adding that column to the index for better performance.

### Don't Perform Arithmetic Operations On Indexed Columns
It is okay to use arithmetic operators in the `WHERE` clause, but be careful about where you use it. Performing arithmetic operations directly on the indexed columns may cause the optimizer to perform a full table scan. Perform the operations on the value side of the equation. 

Let's say we have an index on the `age` column from our customers table. 

```sql 
-- Will not use index (full table scan)
SELECT * FROM customers 
    WHERE age + 10 = 30;

-- Will use index
SELECT * FROM customers
    WHERE age = 30 + 10;
```

This also applies for other functions being performed on the indexed columns.
Let's assume we have an index on `first_name` column. Try to find another query that will produce the same results without using the functions.

```sql
-- Will not use index
SELECT * FROM customers
    WHERE substr(first_name, 1, 2) = 'Th';

-- Will use index
SELECT * FROM customers
    WHERE first_name LIKE 'Th%';
```

### Avoid Wildcard Characters on the Left Side
When performing pattern-matching conditions using the `LIKE` clause, try to avoid using wildcard characters on the left side of the word. Remember that the indexes are sorted. If we use wildcards on the left side, any character can be the first character. We won't need a sorted list of items, so the optimizer will perform a full table scan. 

If you want to use wildcards in the beginning of the word, use the reverse index while keeping the wildcard characters on the right side of the word. Remember that scanning through an index in reverse order has the same performance as scanning using the original order. 

```sql
-- Will not use index
SELECT * FROM customes
    WHERE first_name LIKE '_ar';

SELECT * FROM customers
    WHERE first_name LIKE '%ane%';

-- Will use index
SELECT * FROM customers
    WHERE first_name LIKE 'Jo%';

-- Using reverse index
SELECT * FROM customers
    WHERE reverse(first_name) LIKE 'naht%';
```

### Handling NULL Values
Remember that B-Tree indexes cannot contain null values. So if your column contains null values, the optimizer opt for a full table scan. If you don't care about the null values not appearing on your results, add the `IS NOT NULL` constraint on your condition so that the optimizer will make use of the index. 

Another option is to add a value that will represent the null value instead of actually leaving the value as null. For instance, for all the null values, you could simply insert a dash, `-`, to represent null values. This way, you can specifically look for null values while using the index. 

If your column values have low cardinality, i.e. few unique values, maybe using a bitmap index would be more appropriate. And as you may know already, bitmap indexes can contain null values.
