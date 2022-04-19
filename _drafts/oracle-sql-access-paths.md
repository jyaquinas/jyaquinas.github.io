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
When the condition uses an equality operator, such as `WHERE number=10`, and the column has a unique index, it will use an index unique scan to return **a single row**. If there is a chance that the result contains multiple rows, the optimizer will not use this access path. 

### Index Range Scan



* https://docs.oracle.com/database/121/TGSQL/tgsql_optop.htm#GUID-CDC8B946-2375-4E5F-B50E-DE1E79EAE4CD
