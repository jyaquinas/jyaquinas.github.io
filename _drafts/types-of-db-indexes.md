---
layout: post
title: Types of DB Indexes
subtitle: ---
date: 2022-03-28 22:03:00 +0900
background: '/img/bg-post.jpg'
category: ""
tags: []
---

* What are indexes
    * used for increasing the search speed (performance)

* creating indexes
    * basic syntax
    * `CREATE INDEX index_name ON table_name(column1[,column2,...])`
    * `DROP INDEX index_name` to delete index

* B-TREE (Balanced Trees) index 
    * normal index
    * function based index
    * index-organized table (IOT)
    * Most common type of index
    * stores data in sorted order in a balanced tree structure for faster lookups 
    * cannot contain null values
    
* BITMAP index
    * smaller than b-tree
    * con: bitmap inserts/writes will block entire rows (no write concurrency)
    * typically used for low cardinality data, i.e. there are few distinct column values out of the total number of rows, and for columns that are not updated frequently (due to the block)
        * an example would be the gender column for a table of users or customers
    * efficient for `AND`, `OR, `NOT`, `COUNT` operations
    * can contain null values, unlike B-tree indexes

| Name | Gender | Role |
| --- | --- | --- | 
| John | M | Admin |
| Maria | F | Guest |
| Janice | F | Admin |
| Jake | M | Guest |
| TestUser | Null | Guest |

```
Bitmap Index On Gender Column

Null    0 0 0 0 1
Male    1 0 0 1 0
Female  0 1 1 0 0

Bitmap Index on Role Column

Null    0 0 0 0 0
Admin   1 0 1 0 0 
Guest   0 1 0 1 1
```

Let's look at the following query.
```sql
SELECT * FROM USERS WHERE gender='M' AND role='Admin'
```

Since the two columns have a bitmap index, the following operation can be done.
```
Male    1 0 0 1 0
AND
Admin   1 0 1 0 0
-----------------
Result  1 0 0 0 0
```
Which will give us row 1, user `John`.


These will typically be partitioned into ranges if the row numbers become large, such as Admin for rows 1 to 10, and Admin for rows 11 to 20, and so on. 


* https://blogs.oracle.com/sql/post/how-to-create-and-use-indexes-in-oracle-database