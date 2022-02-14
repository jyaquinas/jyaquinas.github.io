---
layout: post
title: Linux File Permissions
subtitle: Understanding and changing file permissions in linux
date: 2022-02-13 09:44:00 +0900
background: '/img/bg-post.jpg'
category: "Linux"
tags: [linux]
---


When you see the contents of a directory in long format (`ls -l`), you'll be able to see their permissions.

The first column will look something like this: `drwxr-xr-x`

The first character represents the file type, such as `-` for regular files and `d` for directories. Then it's followed by 3 sets of 3 characters, each character representing read, write, and execute permissions, in the respective order. A `-` means it has no permission for that action.
* `rwx`: has full read, write, and execute permissions
* `rw-`: can only read and write
* `---`: has no permissions at all
