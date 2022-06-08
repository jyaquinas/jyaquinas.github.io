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

