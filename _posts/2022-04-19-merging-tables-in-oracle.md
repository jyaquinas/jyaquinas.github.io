---
layout: post
title: Merging Tables In Oracle
subtitle: Performing multiple operations with a single statement
date: 2022-04-19 22:33:00 +0900
background: '/img/bg-post.jpg'
category: "Database"
tags: [oracle, sql, database]
---

### MERGE
`MERGE` selects data from one or multiple tables and updates/inserts it into a target table. This can be useful when you want to perform multiple operations at once. However, we can only update each row only once, i.e. multiple updates on a single row cannot be done using a single `MERGE` statement.

Here's the basic syntax:
```sql
MERGE INTO target_table
    USING source_table
    ON search_condition
        WHEN MATCHED THEN
            UPDATE SET col1 = val1, col2 = val2, ...
            [update_condition]
            [DELETE WHERE condition]
        WHEN NOT MATCHED THEN
            INSERT (col1, col2, ...)
            VALUES (val1, val2, ...)
            [insert_condition]
```

Oracle will go through each row in the target table and check the search condition. If the `search_condition` is true, then it will update the row with the update conditions, and optionally delete the row based on a delete condition[^delete]. If the `search_condition` is not true, then it will insert into the target table from the source table if the insert condition is met. 

Say we have a table of users that contains their information. We have another table that contains new users, but also existing users with new information that needs to be updated. Instead of performing multiple `INSERT` and `UPDATE` statements, we can do these simultaneously with `MERGE`.

We want to update/insert info from USERS_MIGRATE to our target table, USERS.

**USERS**

| first_name | last_name | age |
| --- | --- | --- | 
| John | Smith | 19 |
| Elon | Musk | 23 |
| Mark | Zuckerberg | 24 |
| Bill | Gates | 25 |
| Jeff | Bezos | 26 |

**USERS_MIGRATE**

| first_name | last_name | age |
| --- | --- | --- | 
| John | Smith | 19 |
| Elon | Musk | 33 |
| Mark | Zuckerberg | 24 |
| Bill | Gates | 15 |
| Jeff | Bezos | 36 |
| Lil | Wayne | 31 |
| Tom | Misch | 32 |
| F | KJ | 33 |

```sql
MERGE INTO USERS u
    USING USER_MIGRATE um
    ON (u.first_name = um.first_name AND u.last_name = um.last_name)
        WHEN MATCHED THEN
            UPDATE SET u.age = um.age 
            WHERE u.age <> um.age
            DELETE WHERE u.age < 20
    WHEN NOT MATCHED THEN
        INSERT (u.first_name, u.last_name, u.age)
        VALUES (um.first_name, um.last_name, um.age);
```

Result:
USERS
| first_name | last_name | age |
| --- | --- | --- | 
| John | Smith | 19 |
| Elon | Musk | 33 |
| Mark | Zuckerberg | 24 |
| Jeff | Bezos | 36 |
| Lil | Wayne | 31 |
| Tom | Misch | 32 |
| F | KJ | 33 |

You'll notice that Bill Gates was deleted after being updated (wasn't added) since the age < 20. But even if John Smith also meets that condition, it wasn't deleted because it wasn't updated by the `MERGE` statement. It was already in the target table.

---
[^delete]: The delete only affects rows that were updated by the `MERGE` statement. Rows that meet the condition but were originally there in the target table will not be deleted. 