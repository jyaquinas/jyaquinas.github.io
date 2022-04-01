---
layout: post
title: Oracle Join Operations
subtitle: ---
date: 2022-03-28 22:03:00 +0900
background: '/img/bg-post.jpg'
category: ""
tags: []
---

* Join types
    * equijoins (matching rows with equality operator) vs nonequijoins (no equality operator)
    * outer joins (return matching and nonmatching rows)
    * semijoins (return rows matching with EXISTS subquery)
    * antijoins (return rows that don't match with NOT IN subquery)
    
* Join methods
    * Nested loop joins
        * efficient when row sources are small
        * optimizer may select this when bigger table has an index
    * Sort merge joins
        * better than nested loop if table is big and/or one side is sorted
        * sorts both row sources
        * index full scan, index range scan may help improve performance since data is already sorted in indexes
        * efficient when join condition is nonequijoin
        * 
    * Hash joins
        * better than sort merge if both sides not sorted
        * creates hash table of smaller table, maps rowid to hashvalue of key columns
        * performs full table scan on the other table, then compares hash values of key column to the hash table, then finds the corresponding rowid
        * used only for equijoins
    * Cartesian joins
        * costliest merge -> joins all rows from both sides

