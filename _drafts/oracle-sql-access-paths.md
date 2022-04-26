---
layout: post
title: Oracle SQL Access Paths
subtitle: ---
date: 2022-03-28 22:03:00 +0900
background: '/img/bg-post.jpg'
category: ""
tags: []
---

Access path: method by which a query retrieves rows from a row source (table, view, temporary tables resulting from join operations, etc). 

Two main access paths: table access path, index access path. 

| Access Path | Description |
| --- | --- |
| Full Table Scan | Read entire table and filter out irrelevant rows |
| Table Access by RowID | Access row by internal representation of storage location of data | 
| Sample Table Scan | Read from random sample of data |
| Index Unique Scan | Search for a unique index value |
| Index Range Scan | Scans a range of index values in order |
| Index Full Scan | Reads the entire index in order |
| Index Fast Full Scan | Reads the entire index in unsorted order |
| Index Skip Scan |
| Index Join Scan |
| Bitmap Index Single Value |
| Bitmap Index Range Scan |
| Bitmap Merge |
| Bitmap Index Range Scan |
| Cluster Scan |
| Hash Scan |

### Full Table Scan
This is a costly operation since it will read the entire table and then filter out the irrelevant rows. This access path will be used when there isn't a better option, either other access paths are not available or they are more costly. 

Here are a few reasons why a full table scan might be selected:
* No index available
* Low selectivity 
* Stale table statistics
* Small table
* Query uses full table scan hint

### Table Access by RowID
This is the fastest way to retrieve a row from a table because it is using the specific location of the row to retrieve it. This can be done by using the ROWID in the where clause, but this isn't recommended since the ROWID can change. This type of access path will generally be used from the ROWIDs obtained from other index scans. 

### Sample Table Scan
A random sample of data from the table will be used instead of the full table. This is less commonly used and won't be recommended by the optimizer. This access path will only be used if explicitly stated, using the `SAMPLE` clause. 

```sql
-- Randomly read from 10% of the rows
SELECT * FROM myTable SAMPLE (10);

-- Randomly read from 10% of the table blocks
SELECT * FROM myTable SAMPLE BLOCK (10);

-- percentage range: [0.000001,100)
```

### Index Unique Scan
When the condition uses an equality operator, such as `WHERE number=10`, and the column has a unique index, it will use an index unique scan to return **a single row**. If there is a chance that the result contains multiple rows, the optimizer will not use this access path. It'll probably resort to something like an index range scan instead.

### Index Range Scan
When multiple values are possible from a where condition (and it is selective enough), it will perform an index range scan. Of course, it must be on a column with an index, or be a leading column of a compositite index. 

Since the index is already sorted, it will start from the starting point of the where condition and scan the index in order until all the values have been retrieved. Doing this in descending order will not affect the performance as it only scans the index in reverse order. 

Here are some examples of the conditions that might trigger an index range scan:

* `column1 = :val`
* `column1 < :val`
* `column1 > :val`
* combination of the conditions above
* when wildcard searches are not in a leading position, e.g. `'%abc` will not use an index scan

```sql
-- There could be multiple 30 yr old customers
SELECT * FROM customer WHERE age=30;
-- This wildcard search will use an index scan since we know the starting point in the index
SELECT * FROM customer WHERE name like 'jen%';
-- Anything can come before 'as' so the index scan will not be used
SELECT * FROM customer WHERE name like '%as';
```

### Index Full Scan
This type of scan will scan the entire index in order. Because an index is already ordered, an `ORDER BY` clause can trigger an index full scan. But here are a few other reasons why the optimizer might choose this:

* condition uses a column from a composite index but is not the leading column
* all columns in the table and query are in an index and one of the indexed columns is not null
* contains an `ORDER BY` clause on a non-nullable column

### Index Fast Full Scan


### Index Skip Scan
An index skip scan typically occurs when a composite index is used but the leading column in skipped or not used in the query. But it can also occur if the leading column contains few distinct values as opposed to the nonleading columns of the index. 

For example, let's say we have an index on these two columns, (`gender`, `age`), but we only search using the `age` column. Since the index will have sorted the columns in gender first, and then by age, it will search through the `male` gender first, and then through the `female` gender, until all the customers of age `30` have been retrieved. 

### Index Join Scan


### Reference
* https://docs.oracle.com/database/121/TGSQL/tgsql_optop.htm#GUID-CDC8B946-2375-4E5F-B50E-DE1E79EAE4CD
