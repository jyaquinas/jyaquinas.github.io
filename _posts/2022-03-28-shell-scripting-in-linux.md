---
layout: post
title: Shell Scripting In Linux
subtitle: Basic syntax for bash scripting
date: 2022-03-28 20:23:00 +0900
background: '/img/bg-post.jpg'
category: "Linux"
tags: [linux, bash, shell script]
---

### Why Shell Scripting?
It's just another way to improve your productivity. Just like how you'd write a program to do the repetitive tasks for you, you can achieve the same with shell scripts. Maybe you need to compile and deploy multiple applications. Instead of manually running these commands one by one, you can simply run a single shell script that will run all of the commands for you. 

There are various shell languages (bash, csh, zsh, etc) that you can choose from. You can check which languages are installed on your server by using the command `cat etc/shells`. But since bash is the most commonly used one, I'll be using bash syntax. 

### Shell Script Files
All executable shell script files have a file extension of `.sh` and will start with a [shebangs](https://en.wikipedia.org/wiki/Shebang_(Unix)) on the first line. 

`#!/bin/bash` or `#!/bin/csh` (depending on the language you're using)

This tells the shell interpreter what shell language you'll be using. If not, it will use the system default, which you can check with `echo $SHELL`.

### Running Shell Scripts
Make sure you have execution permission on the sript file. Check out this [post]({% link _posts/2022-02-17-linux-file-permissions.md %}) for more info on linux file permissions.

`chmod +x [filename]`

There are a couple ways you can execute the script file:
* `./scriptname.sh`[^dot]
* `sh scriptname.sh`
* `bash scriptname.sh`

If the script is in another directory, use the absolute path along with the filename.

You can also run shell scripts within a shell script with the same commands mentioned above. Say we have a file, `print_hello.sh`, which simply contains `echo hello`. We'll have another file called `print_helloworld.sh`.

```shell
#!/bin/bash
./print_hello.sh
echo world
```

This will execute the print_hello.sh file, which will print `hello`, then it will move on and print `world`.

### Functions
There are two ways we can define functions in bash.
```shell 
#!/bin/bash
# define functions
func1 () {
    # body
    echo func1
}

function func2 {
    # body
    echo func2
}

# call the functions
func1
func2
```

In shell scripts, you are limited to returning integer values, usually to signify the status of the executed function. If you want to return some value, you will have to pass it through a global variable. 
```shell
myfunc () {
    return 5
}
myfunc
echo $? # exit status of the last command executed -> 5
```

You can also pass in parameters to the function. The numbers signify the position of the arguments passed. `$@` will print out all the arguments. 
```shell
myfunc () {
    echo $1 $2
    echo $@
}
myfunc hello world  # outputs 'hello world'
```

Functions can be defined on a single line as well. Just separate the commands with semicolons. They also have to be defined before they are called on the script. 

### Variables
Global variables are variables that can be accessed anywhere in the script. Local variables are defined inside functions and their scope is only within the function. You can declare them using the word `local`.

```shell
var=glo
func1 () {
    local var=loc
}

func2 () {
    var=loc
}

echo $var   # outputs glo
func1
echo $var   # outputs glo (global var not affected)
func2
echo $var   # outputs loc (gloval var changed)
```

#### Saving User Input To a Variable
You can also get the user input and pass that to the function.
```shell
func1 () {
    echo $1
}
echo 'Input the word:'
read userInput  # save user input to the variable, userInput
func1 $userInput
```

### If Statements
Here is the basic syntax:
```shell
if [ condition ]
then 
    # action
elif [ condition ]; then    # separata by semicolon if on the same line
    # action
else 
    # action
fi
```

Here are some of the conditions you can use in the if statement.

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

For examaple:
```shell
a=10
b=20
if [ $a -lt $b ] 
then 
   echo '$a is less than $b'    # this is executed
else
    echo '$a is not less than $b'
fi
```

***Note**: make sure to include spaces between the brackets*

You can also have nested if statements. 

### Loops
#### For Loops
The basic syntax is:
```shell
for [ loop condition ]
do
    # action
done
```

Here are a few examples.
```shell
for i in {1..5}
do
    echo "output: $i"
done

max=10
for (( i=2; i <= $max; ++i ))[^doublepar]
do
    echo $i
done

for f in $(ls):     # prints out result from the ls command
do
    echo "-> $f"
done
```

#### While/Until Loops
Here's the basic syntax:
```shell
while [ condition ]
do
    # action
done
```

Here's an example:
```shell
i=0
while [ $i -lt 10 ]
do
    echo $i
    (( i++ ))
done
```

The syntax is the same for until loops. They're similar to the while loops but instead will run until the stated condition becomes true (or keeps executing while the condition is false). 

### Case Statements
Here is an example.

```shell
echo Select from the following options:
echo 1. a
echo 2. b
echo 3. c
read selection

case $selection in
    a) echo 'You selected a';;
    b) echo 'You selected b';;
    c) echo 'You selected c';;
    *) echo 'Wrong input';;     
esac
```

We define the possible case values using the syntax `caseValue)`. So if the value of `selection` is `a`, the statement in `a)` will be executed. `*)` is similar to the default case and will execute when no values are matched.

---
[^dot]: This is using the relative path of the file. This is not to be confused with the [dot command](https://en.wikipedia.org/wiki/Dot_(command)#:~:text=In%20a%20Unix%20shell%2C%20the,extended%22%20POSIX%20shells%20as%20well.), which can also be used to run scripts. The difference is that the dot command will execute it in the current shell, whereas the other methods will execute them in a new subshell. So changes, like new variable assignments, will affect your current environment if the dot command is used. Check out this [post](https://www.shell-tips.com/bash/source-dot-command/) for more info.  
[^doublepar]: The [double parenthesis](https://tldp.org/LDP/abs/html/dblparens.html) is similar to the `let` command. It lets you perform arithmetic evaluations. 