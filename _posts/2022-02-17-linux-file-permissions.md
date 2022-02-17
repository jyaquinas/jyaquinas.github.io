---
layout: post
title: Linux File Permissions
subtitle: Understanding and changing file permissions
date: 2022-02-17 20:59:00 +0900
background: '/img/bg-post.jpg'
category: "Linux"
tags: [linux]
---

### Understanding Permissions

When you see the contents of a directory in long format (`ls -l`), you'll be able to see their permissions.

The first column will look something like this: `drwxr-xr-x`

The first character represents the file type, such as `-` for regular files and `d` for directories. Then it's followed by 3 sets of 3 characters, each character representing read, write, and execute permissions, in the respective order. A `-` means it has no permission for that action.

The 3 sets will correspond to the different permissions: *user* (file owner), *group* (group members), and *other* (everyone else) permissions.

* `rwxrwxrwx`: all users have full read, write, and execute permissions
* `rwxrw-r--`: owner can read, write, and execute, but *group* users can only read and write, and the rest can only read
* `rwx------`: owner has full permission, but the rest have none

### Modifying Permissions
There are two ways we can modify permissions, the symbolic (text) and numeric methods.

#### Symbolic
The basic syntax is:  
```shell
chmod [USERFLAG][+-=][rwx] FILE
```

* `[USERFLAG]`: You can use a, u, g, o, for all, *user*, *group*, and *other*, respectively. Multiple flags can be used at the same time.  
* `[+-=]`: You can use +, -, and = for adding, removing, and replacing (overrides old permissions) the specified permissions. If only `=` is used without any permissions, it will simply remove all permissions.
* `[rwx]`: You can select one or multiple permissions
* `FILE`: It can be either a file or directory, as well as files with a certain extension by using `*.extension`, such as `*.txt`

Here are a few examples:
```shell
chmod g+w file.txt      # adds write permission to group
chmod o+rw file.txt     # adds read and write permission to others
chmod og-rwx file.txt   # removes all permissions from group and others
chmod og= file.txt      # achieves the same as above
chmod a=r file.txt      # gives only read permission to everyone
chmod u+x, g=r file.txt # adds execute permision to user and gives only read permission to group
chmod a=r *.txt         # gives write permission to all for all txt files
```

#### Numerical
The basic syntax is the same as the symbolic method, but instead of the `g+w` portion, we will use a numeric representation for it.

Three digits are used, each representing the permission for the *user*, *group*, and *other*.

| Number Representation | Permission |
| --- | --- |
| 0 (000) | No permission |
| 1 (001) | Execute permission |
| 2 (010) | Write permission |
| 3 (011) | Write and execute permission |
| 4 (100) | Read permission |
| 5 (101) | Read and execute permission |
| 6 (110) | Read and write permission |
| 7 (111) | Read, write, and execute permission |

So if we have 764, *user* has full permission, *group* has read and write permissions, and *other* only has read permission.

Here are a few examples:
```shell
chmod 666 file.txt    # gives read and write permissions to all
chmod 740 *.txt       # gives full permission to user, read permission to group, and no permission to others for txt files
chmod 777 directory   # gives full permission to all for the directory
```

<br>
### Bonus
You can change the permissions for all the files and subdirectories of a folder by using the `-R`.
```linux
chmod 755 -R directoryname
```
This will change the permissions of all files and subdirectories.

But say you want to change all the files contained in the folder and subfolders with a certain extension. We can do that with the help of `find`.
```shell
find . -name '*.txt' -exec chmod 755 {} \;
```
This will change the permission of all the txt files in the directory and subdirectories, but not the directories themselves.
