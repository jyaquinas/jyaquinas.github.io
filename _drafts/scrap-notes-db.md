---
layout: post
title: ---
subtitle: ---
date: 2022-02-22 22:03:00 +0900
background: '/img/bg-post.jpg'
category: ""
tags: []
---

    
* Oracle packages
    * > A package is a schema object that groups logically related PL/SQL types, variables, constants, subprograms, cursors, and exceptions. A package is compiled and stored in the database, where many applications can share its contents.

* Failover and loadbalancing in oracle db
    * https://docs.oracle.com/cd/E15217_01/doc.1014/e12490/failover.htm
    * https://docs.oracle.com/cd/B28196_01/idmanage.1014/b25344/failover.htm

* Using sqlplus in cloud oracle with wallet
    * download wallet, then upload to cloud storage
    * unzip wallet to a directory
    * set TNS_ADMIN variable to the directory `export TNS_ADMIN=/dir/`
    * edit sqlnet.ora and set update the directory
    * `sqlplus admin@dbname` -> dbname from tnsnames.ora
    * input password and voila

* pass variable to sql script by using `&1 &2`
    * `insert into authors (firstname, lastname) values ('&1', '&2');`
    * then use `@script.sql var1 var2`
    
* Oracle sql
    * `:=` is used for assigning values to variables
    * oracle sql vs pl/sql 
        * https://www.tutorialspoint.com/difference-between-sql-and-pl-sql
        * oracle sql is oracles version of SQL
        * pl/sql -> procedural language SQL -- extension of oracle sql, has functionalities of functions, control structures, triggers, etc (a programming language that uses SQL, meant for DBs)
        * cannot use pl/sql in mysql
        * `;` ends sql statement, `/` executes whatever is in the buffer (usually for running plsql blocks defined by begin and end)
    * plsql loops
        * https://blogs.oracle.com/sql/post/better-loops-and-qualified-expressions-array-constructors-in-plsql
        * https://stackoverflow.com/questions/36325831/use-oracle-pl-sql-for-loop-to-iterate-through-comma-delimited-string
        * https://stackoverflow.com/questions/2242024/for-each-string-execute-a-function-procedure
        * https://livesql.oracle.com/apex/livesql/file/tutorial_KS0KNKP218J86THKN85XU37.html

```sql
DECLARE
    type nt_arr is table of varchar2(50);
    arr nt_arr := nt_arr ('1234','asdf','23g');
BEGIN
  FOR i IN 1..arr.count
  LOOP
    DBMS_OUTPUT.PUT_LINE( arr(i) );
  END LOOP;
END;
```

* SQL Tuning
    * selectivity = number of rows from query / total rows
        * OR cardinality / total rows?
        * selectivity of 1 -> all rows are unique, high selectivity
        * full table scan for low selectivity 
    * cardinality = selectivity * total rows 
        * number of unique values in a column
    * Analyzing execution plan
        * explain plan
            * `EXPLAIN PLAN FOR <QUERY>` -> saves to plan_table
            * `SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY())`
            * `EXPLAIN PLAN SET statement_id = 'MyID' FOR SELECT FROM EXPLOYEES where employee_id = 100;`
            * `EXPLAIN PLAN SET statement_id = 'MyID' INTO MyPlanTable FOR SELECT FROM EMPLOYEES where employee_id = 100;`
        * autotrace -> produces execution plan and statistics, uses plan_table like the explain plan
            * `SET AUTOTRACE ON;`
            * `SET AUTOTRACE ON [EXPLAIN|STATISTICS];`
            * `SET AUTOTRACE TRACE[ONLY] ON [EXPLAIN|STATISTICS];`
            * `SET AUTOTRACE OFF`
        * v$SQL_PLAN -> actual execution plans stored here, similar to plan table, connected to V$SQL view
            * `SELECT * FROM TABLE(DBMS_XPLAN.DISPLAY_CURSOR('****'));`
            * look at cost, access methods, cardinality, join mehtods/join types, partition pruning, etc
    * Note: comparing costs between 2 different queries is meaningless because the costs are relative to the specific query. 
        * More accurate to compare consistent gets (from autotrace) -> physical reads that the DB performs to get data from data block (disk I/O)
    * access predicate vs filter predicate
        * access predicate: only fetch matching rows (usually through index)
        * filter predicates: discard non-matching rows (after fetching more rows than needed)
    * Tuning strategies
        * Parse time reduction 
        * execution plan comparison and analysis
        * query analysis strategy
            * update statistics (must have DBA access) - outdated statistics may mislead the optimizer 
            * improve query structure
            * use optimizer hints
            * changing access path 
            * improve join order and join methods

* subquery factoring (WITH CLAUSE) vs global temporary tables (GTT)
    * used for improving query speed for complex subqueries
    * typically used when subquery is executed multiple times
* case expression
    * https://docs.oracle.com/cd/B19306_01/server.102/b14200/expressions004.htm
    * >CASE expressions let you use IF ... THEN ... ELSE logic in SQL statements without having to invoke procedures.
    ```sql
        SELECT cust_last_name,
        CASE credit_limit WHEN 100 THEN 'Low'
        WHEN 5000 THEN 'High'
        ELSE 'Medium' END
        FROM customers;
    ```

* lead
    * https://docs.oracle.com/cd/B19306_01/server.102/b14200/functions074.htm
    * > LEAD is an analytic function. It provides access to more than one row of a table at the same time without a self join. Given a series of rows returned from a query and a position of the cursor, LEAD provides access to a row at a given physical offset beyond that position.
    * basic syntax:
    ```sql
    LEAD(expression [, offset ] [, default ])
    OVER (
        [ query_partition_clause ] 
        order_by_clause
    )
    ```
    
    * `expression`: must return single value, expression that is evaluated for the row
    * `offset`: offset value from current row, default is 1
    * `default`: if offset goes beyond scope of partition, it will return this default value. NULL by default.
    * `query_partition_clause`: this clause divides the rows into partitions to which the lead function will be applied (Think of it as applying the lead function on different categories, and each category being ordered by the condition stated in order_by_clause). It will treat the entire thing as single partition by default.
    * `order_by_clause`: specifies order of rows in each partition

    ```sql
    SELECT last_name, hire_date, 
    LEAD(hire_date, 1) OVER (ORDER BY hire_date) AS "NextHired" 
    FROM employees WHERE department_id = 30;

    LAST_NAME                 HIRE_DATE NextHired
    ------------------------- --------- ---------
    Raphaely                  07-DEC-94 18-MAY-95
    Khoo                      18-MAY-95 24-JUL-97
    Tobias                    24-JUL-97 24-DEC-97
    Baida                     24-DEC-97 15-NOV-98
    Himuro                    15-NOV-98 10-AUG-99
    Colmenares                10-AUG-99
    ```

* trim 
    * trim leading or trailing characters
    * `TRIM( [ [ LEADING | TRAILING | BOTH ] trim_char FROM ] string)`
    * `[ LEADING | TRAILING | BOTH ]` is optional, `BOTH` by default
    * `trim_char` specifies the character to be removed, if none specified, space by default 
    * 
* substr
    * returns substring starting from `position` with length `substring_length`
    * `SUBSTR( str, position [, substring_length] );`
    * `position`
        * 0 -> treated as 1
        * positive -> counts from left to right
        * negative -> counts from right to left (backwards)
    * if `substring_length` is omitted -> returns to end of string
* instr
    * search for substring in a string and returns the index of the first occurrence
    * `INSTR(string , substring [, position [, occurrence]])`
    * `position` -> integer that indicates at what position the search should start (pos -> left to right, neg -> right to left, backwards); default 1
    * `occurrence` -> determines which occurrence to search for, default 1 (first occurence)
* listagg
    * aggregates the result from multiple rows into a single list of values separated by a delimiter 
    * syntax
    ```sql
    LISTAGG (
        [ALL] column_name [,
        delimiter]
    ) WITHIN GROUP(
        ORDER BY
            sort_expressions
    );
    ```
    * 


## Data Warehouse, or OLAP (online analytical processing) DB vs OLTP (Online Transaction Processing) DB
* Data Warehouse
    * mostly used for providing data (read heavy)
    * gathers/collects data form different sources into a central repository
    * few concurrent users (relative to OLTP)
    * stores large amounts of data
    * data denomalization is common
    * bitmap indexes might be more suitable
* OLTP
    * supports large numbers of concurrent transactions (insert, update, delete)
    * large number of concurrent users
    * data is typically normalized
    * b-tree indexes might be more suitable

## Oracle Index
* btree indexes should be created based on how often that column is used for querying (where clause), and how selective it is (more selective the better it is)


## Cassandra
* partition key
    * made up of one or more fields used for partitioning data across multiple nodes (uses consistent hashing for uniformly distributing data)
    * querying without a partition key in the where clause results in inefficient full cluster scan (must visit all nodes) - it also applies to composite partition keys (must include all and in the same order)

* clustering key
    * made up of one or more fields use for grouping rows with same partition key, and is stored in order
    * defines how data is stored and sorted within a partition
* partition key always comes first in the primary key definition (shown by double parenthesis), followed by the clustering key/s

```sql
 create table example (
      k_part_one text,
      k_part_two int,
      k_clust_one text,
      k_clust_two int,
      k_clust_three uuid,
      data text,
      PRIMARY KEY((k_part_one, k_part_two), k_clust_one, k_clust_two, k_clust_three)      
  );
```

* best practices
    * each partition should be < 100mb (ideally < 10mb )
    * goal is to design tables with partition/clustering keys that will evenly distribute the partitions, and support the needed queries

* example
    * https://www.baeldung.com/cassandra-data-modeling
    