---
layout: post
title: Shell Scripting In Linux
subtitle: ----
date: 2022-03-15 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "Linux"
tags: [linux]
---


* Shell scripts
    * check shells installed:
        * `cat etc/shells`
    * .sh files that usually have [shebangs](https://en.wikipedia.org/wiki/Shebang_(Unix)) on the first line
    * `#!/bin/bash` or `#!/bin/csh`
    * to run the scripts:
        * `./scriptname.sh`, `sh scriptname.sh`, `bash scriptname.sh`, `. scriptname.sh`
        * to run scripts within scripts, you can also do the same `. path/file.sh`
    * make sure you have the executable permission, or update it using `chmod`
    * loops and ifs?
        * https://linuxconfig.org/bash-scripting-tutorial
* Bash (bourne again shell) vs sh (bourne shell)
    * what is shell? a CLI (command line interpreter) program that provides interface between user and os service
        * lets you run linux commands
        * sh converts human readable commands and converts them to commands for kernel
    * sh with more features
    * bash scripting is only for bash, but sh scripting is for any shell
    * bash is the default SHELL (can check in your linux by `ps -p $$`)
* forloop
    ```shell
    for i in {1..5}
    do
        echo "output: $i"
    done

    max=10
    for (( i=2; i <= $max; ++i ))
    do
        echo $i
    done
    ```

    *csh uses `foreach i (1,2,3)`
* if statement
    * https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php
    * https://acloudguru.com/blog/engineering/conditions-in-bash-scripting-if-statements

```shell
a=10
b=20
if [ $a -lt $b ] 
then 
   echo '$a is less than $b'
else
    echo '$a is not less than $b'
fi
```

* Note: be careful of the spaces

| Operator | Description |
| --- | --- |
| [ num1 -lt num2 ] | num1 < num2 |
| [ num1 -le num2 ] | num1 <= num2 |
| [ num1 -gt num2 ] | num1 > num2 |
| [ num1 -ge num2 ] | num1 >= num2 |
| [ num1 -eq num2 ] | num1 == num2 |
| [ num1 -ne num2 ] | num1 != num2 |
| [ str1 = str2 ] | str1 == str2 |
| [ str1 != str2 ] | str1 != str2 |
| [ -d file ] | file exists and is a directory |
| [ -e file ] | file exists |
| [ -r file ] | file exists and has read permission |
| [ -w file ] | file exists and has write permission |
| [ -x file ] | file exists and has execution permission |
| [ -s file ] | file exists and size is greater than zero |
