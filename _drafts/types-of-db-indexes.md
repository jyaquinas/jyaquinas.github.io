---
layout: post
title: Types of Oracle Database Indexes
subtitle: Understanding B-Tree and Bitmap Indexes
date: 2022-03-28 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "Database"
tags: [database, oracle, indexes]
---

### What are indexes?
Indexes are used for increasing the search speed of databases. It creates a separate lookup table and maps them to the actual rows so that the search operations can be more efficient. 

### Types of Indexes
There are two main types of indexes: B-Tree and bitmap indexes. 

#### B-Tree Index
B-Tree stands for balanced tree, meaning that the indexed values are stored in a balance tree structure, allowing any lookup to take **O(logn)** time. 

The indexed values are always stored in a sorted order. Each node contains a range of indexed values, with each of the child nodes further dividing each of the ranges. The leaf nodes contain the actual indexed values, each mapped to a rowid, which is then used to lookup the actual row from the table. Notice how the leaf nodes are also doubly linked with each other. This allows scanning through the indexed values in a sequential order. 

[INSERT BTREE INDEX IMAGE]

Indexes can also be created for multiple columns simultatenously. These are referred to composite indexes. The order of the columns used for creating the composite indexes are important because they define how the indexes will be stored and ordered. The leading column is used as the primary sort order. The following columns are used as secondary, tertiary orders.

So because of this characteristic, we can only query the table using the index if we use the leading portions of the index. 

Let's say we have an index on columns (a, b, c).

These are some combinations of the columns that will trigger the optimizer to use the index:
* a
* a, b
* a, b, c

Anything that doesn't use the leading portion of the index, such as (b, c), will not use the index. The tree is stored in a way that a is sorted first, before b and c are.

The B-tree index is the default index used in Oracle. It is also the most common type of index. 

Also, one thing to note is that B-tree indexes cannot contain null values (we can't sort null values, can we?).

#### Bitmap Index
Bitmap indexes are also stored in a b-tree, but unlike B-tree indexes, bitmap indexes map to a range of rowids. Each column value is associated with a bitmap, and each bit in the bitmap represents a rowid. If the rows are too large, multiple bitmaps can be generated for the same column value, each representing a different range of rowids. Each of the leaf nodes hold the column value, start rowid, end rowid, and the bitmaps for the corresponding rowids. 

[INSERT BITMAP INDEX IMAGE]

Because each bitmap represents a column value, bitmap indexes are typically used for low cardinality data, i.e. there are few distinct column values out of the total number of rows. An example would be the gender column for users, where the possible values are limited to `Male`, `Female`, and `NULL`. And yes, unlike b-tree indexes, bitmap indexes can take null values. 

Also, because the entire bitmap represents a range of rowids, an DML operation on a bitmap index blocks the entire range of rows until the operation is finished. So another insert operation on another row that is part of th same range of rowids will be blocked. This is another reason why bitmap indexes are typically used for tables that are read heavy and don't require many writes. 

Note that bitmap indexes can also be created for multiple columns. It will then create a bitmap for all the combinations of the column values. 

But aside from this disadvantage, bitmap indexes are efficient for `AND`, `OR, `NOT`, `COUNT` operations. 

Let's look at the following example. 

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

Now let's look at the following query.
```sql
SELECT * FROM USERS WHERE gender='M' AND role='Admin'
```

Since the two columns have a bitmap index, the following operation can be done.
```
Male    1 0 0 1 0
Admin   1 0 1 0 0
(AND) ------------
Result  1 0 0 0 0
```
Which will give us row 1, user `John`.

As for the `COUNT` operation, it will simply go through the bitmap and count all the `1` values. 

These bitmaps will typically be partitioned into ranges if the row numbers become large, such as Admin for rows 1 to 10, and Admin for rows 11 to 20, and so on. 

### Creating and Deleting Indexes
This is the basic syntax for creating new indexes.

```sql
CREATE [BITMAP/UNIQUE] INDEX index_name ON table_name([column/s])
```

Add the keyword `BITMAP` for bitmap indexes. You can also add the `UNIQUE` keyword if it's guaranteed that the values of the column are unique. By default, the indexes created are nonunique, and those with the same column values will be sorted by ascending rowid. 

To delete an index:

```sql
DROP INDEX index_name
```

The DB will assume that this index is in your current schema. If you want to delete an index from another schema, use the following syntax:

```sql
DROP INDEX schema_name.index_name
```


#### Reference
* https://blogs.oracle.com/sql/post/how-to-create-and-use-indexes-in-oracle-database
* https://docs.oracle.com/cd/E11882_01/server.112/e40540/indexiot.htm#CNCPT1170
