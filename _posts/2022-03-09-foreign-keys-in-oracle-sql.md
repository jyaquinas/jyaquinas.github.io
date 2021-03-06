---
layout: post
title: Foreign Keys in Oracle SQL
subtitle: Set relationships between tables
date: 2022-03-09 21:04:00 +0900
background: '/img/bg-post.jpg'
category: "Database"
tags: [oracle sql, sql, database]
---

### What is a foreign key?
Foreign keys establish a relationship between two tables. A column from one table (child table) references the primary key from another table (parent table). The foreign key is defined in the child table.

### Why use them?
It helps maintain the referential integrity of your DB, i.e. only existing values from the foreign table (the primary key being referenced) can be added as a foreign key.

If you try to insert a non-existent value, you'll get an error.
>ORA-02291: integrity constraint (ADMIN.SYS_C0028304) violated - parent key not found

Of course, you can maintain this integrity yourself. But can we be 100% sure that you, and everyone else using the DB, will never make a mistake? :smirk:

### Syntax
```sql
CREATE TABLE child_table (
    ...
    CONSTRAINT fk_name
    FOREIGN KEY (col1, col2, ...) REFERENCES
        parent_table (col1, col2, ...)
        ON [DELETE|UPDATE] [referential_actions]
)
```

***Note:*** using the keyword CONSTRAINT along with the constraint name is optional. If this part is omitted, oracle will automatically assign a name to it.  
More info about referential actions below.

You can also add or remove foreign keys for existing tables.
```sql
ALTER TABLE child_table
    ADD CONSTRAINT fk_name
        FOREIGN KEY (col1, col2, ...) REFERENCES
        parent_table (col1, col2, ...)
        ON [DELETE|UPDATE] [referential_actions];

ALTER TABLE child_table
    [DROP|DISABLE|ENABLE] CONSTRAINT fk_name;
```

For example:
```sql
CREATE TABLE authors (
    author_id NUMBER GENERATED BY DEFAULT AS IDENTITY (CACHE 500),
    firstname VARCHAR2(50) NOT NULL,
    lastname VARCHAR2(50) NOT NULL,
    age NUMBER,
    PRIMARY KEY (author_id)
);

CREATE TABLE articles (
    article_id NUMBER GENERATED BY DEFAULT AS IDENTITY (CACHE 500),
    author_id NUMBER NOT NULL,
    title VARCHAR2(100) NOT NULL,
    category VARCHAR2(50),
    PRIMARY KEY (article_id),
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);
```

### Referential Actions
You can specify referential actions whenever there is a *delete* or *update* using the `ON DELETE` and `ON UPDATE` clauses.
* **Cascade**: if primary key is deleted, delete matching columns in the child table
* **Set null**: if primary key is deleted/altered, set referencing values in the child table to null
* **Restrict**: primary key values in the parent table cannot be deleted if it is still referenced by a foreign key
* **Set default**: if primary key is deleted/altered, set referencing values in the child table to a default value  

It is set to `RESTRICT` by default (if `ON DELETE` and `ON UPDATE` clauses are omitted).

Trying to delete a row from the parent table in which its primary key is still being referenced, and the default `RESTRICT` constraint is set, will lead to the following error:
> ORA-02292: integrity constraint (ADMIN.SYS_C0028304) violated - child record found
