---
layout: post
title: Oracle Join Operations
subtitle: ---
date: 2022-03-28 22:03:00 +0900
background: '/img/bg-post.jpg'
category: ""
tags: []
---

### Join Types
Determined by join condition.

* inner join (also referred to as simple join)
    * equijoins (matching rows with equality operator)
    * nonequijoins (no equality operator, e.g. `BETWEEN`, `<`, or `>` operators)
* outer joins (return matching and nonmatching rows)
* semijoins (return rows matching with EXISTS subquery)
* antijoins (return rows that don't match with NOT IN subquery)

### Join Methods

* Nested loop joins
    * efficient when row sources are small
    * optimizer may select this when bigger table has an index
    * similar to nested for loop 
    > To perform a nested loops join, Oracle follows these steps:
    > 1. The optimizer chooses one of the tables as the outer table, or the driving table. The other table is called the inner table.
    > 2. For each row in the outer table, Oracle finds all rows in the inner table that satisfy the join condition.
    > 3. Oracle combines the data in each pair of rows that satisfy the join condition and returns the resulting rows.

* Sort merge joins
    * better than nested loop if table is big and/or one side is sorted
    * sorts both row sources
    * index full scan, index range scan may help improve performance since data is already sorted in indexes
    * efficient when join condition is nonequijoin
    > Oracle can only perform a sort-merge join for an equijoin. To perform a sort-merge join, Oracle follows these steps:
    > 1. Oracle sorts each row source to be joined if they have not been sorted already by a previous operation. The rows are sorted on the values of the columns used in the join condition.
    > 2. Oracle merges the two sources so that each pair of rows, one from each source, that contain matching values for the columns used in the join condition are combined and returned as the resulting row source.

* Hash joins
    * better than sort merge if both sides not sorted
    * creates hash table of smaller table, maps rowid to hashvalue of key columns
    * performs full table scan on the other table, then compares hash values of key column to the hash table, then finds the corresponding rowid
    * used only for equijoins
    > Oracle can only perform a hash join for an equijoin. Hash join is not available with rule-based optimization. You must enable hash join optimization, using the initialization parameter HASH_JOIN_ENABLED (which can be set with the ALTER SESSION command) or the USE_HASH hint.
    >
    > To perform a hash join, Oracle follows these steps:
    >
    > 1. Oracle performs a full table scan on each of the tables and splits each into as many partitions as possible based on the available memory.
    > 2. Oracle builds a hash table from one of the partitions (if possible, Oracle will select a partition that fits into available memory). Oracle then uses the corresponding partition in the other table to probe the hash table. All partition pairs that do not fit into memory are placed onto disk.
    > 3. For each pair of partitions (one from each table), Oracle uses the smaller one to build a hash table and the larger one to probe the hash table.
* Cartesian joins
    * costliest merge -> joins all rows from both sides
    
* driving table vs inner table
    * driving table -> full scan typically
    * inner table -> can use index scans
---
* https://logicalread.com/oracle-explain-plans-driving-tables-and-table-joins-h01/
* https://docs.oracle.com/database/121/TGSQL/tgsql_join.htm#TGSQL244