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
    * 
* B-TREE (Balanced Trees) index 
    * normal index
    * function based index
    * index-organized table (IOT)
    * Most common type of index
    
* BITMAP index
    * smaller than b-tree
    * con: bitmap inserts/writes will block entire rows (no write concurrency)
    

* https://blogs.oracle.com/sql/post/how-to-create-and-use-indexes-in-oracle-database