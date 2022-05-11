---
layout: post
title: Other Linux Commands You Might Find Useful
subtitle: Boost your productivity with these commands
date: 2022-04-19 20:39:00 +0900
background: '/img/bg-post.jpg'
category: "Linux"
tags: [linux]
---

### Linux Wildcards
You can use these wildcards for pattern matching. They can be quite useful when searching for patterns in filenames, directories, etc. 
* `*`: match one or more occurrences of characters, including none  
    * `ls *.txt` will look for all files that have the txt extension
* `?`: match single occurrence of character
    * `l?st` -> list, lost, last are matches
* `[]`: match any occurrence of characters in the enclosed bracket
    * `l[ao]st` -> last, lost are matches
* `./tmp/*`: matches files and folders in ./tmp
* `./tmp/**`: matches files, folders, and subfolders in ./tmp

### Command Substitution
This allows us to execute some commands and use the command result in another command. The syntax, `$()`, is commonly used but you may find other syntaxes, like ` `` ` (former is recommended as it's more readable, and supported in most shells). Linux will execute whatever is inside the `$()` before it executes the rest.

```bash
# Saves the string "date" 
datevar=date
echo $datevar # will output "date"

# Saves the actual date into the variable
datevar=$(date)
echo $datevar # will output the date
```

### Variable Substitution
There can be situations where other parts of the command could be mistaken to be part of the variable name, leading to errors. We can use parameter expansion to differentiate the variables. The basic syntax is `${}`.

```bash
weight=80
echo "$weightKG"    # error: weightKG variable doesn't exist

echo "${weight}KG"  # outputs 80KG
```

### ps, pgrep
`ps` will list the processes that are currently running. These are the different options you can use with the command.
* `-e`: list full process list
* `-f`: full format
* `-p`: get a particular process id, `ps -p 5553`

It can also be used with other commands like `grep`. 

`ps -ef | grep *.jar` will get all the processes with the jar extension. 

Another option would be to use `pgrep`, which lets you look up processes using the process name. Some options are:
* `-f`: match against entire command line instead of just process name
* `-l`: list only process name and id
* `-x`: get processes with exact pattern match only

### kill
You can use this command to kill processes that are running. You will need the process id (pid). You can find pid using the `ps` command mentioned above.  

`kill [option] [pid]` 

Options (see full list with `kill -l`):
* `-1`: Reload a process.
* `-9`: Kill a process.
* `-15`: Gracefully stop a process.

### cut
This command cuts or splits each line and returns the results to the standard output. 

`cut [option] [arguments] [filename]`

Options:
* `-f`: fields
* `-b`: bytes
* `-c`: characters
* `-d`: delimiter
* `-s`: gets only lines with delimiters

Arguments for the list: 
* `N`: nth field
* `N-`: nth field to the end
* `N-M`: nth to mth field
* `-N`: first to nth field
        
Here are some examples:
```bash
# gets 1,2,3rd byte from each line (tabs and backspaces are counted as 1 byte)
cut -b 1,2,3 file.txt   # mytext -> myt
cut -b 1-3,5-7 file.txt # mytextbla -> mytxtb
cut -b 1- file.txt      # 1st bite till the end
cut -b -3 file.txt      # first byte to 3rd byte

# gets the character in specified positions (tabs and backspaces count as 1 char)
cut -c 1,2,3 file.txt

# gets 1st and 3rd field delimited by tab (by default)
cut -f 1,3 file.txt 
cut -f 1,3 -d ':' file.txt # same as above but uses `:` as delimiter
```

### tail
`tail` is used for displaying the last 10 lines of files. It is quite useful for monitoring file changes in real-time, usually for reading/monitoring log files, using the `-f` option.

`tail [option] [filename]`

Options:
* `-n [number]` or `-[number]`: displays last n lines
* `-c [number]`: displays last n bytes/characters
* `-f`: monitors file changes in real time (exit by pressing `ctrl + c`)

```bash
# display last 10 lines by default
tail file.txt 
tail -n 5 file.txt  # display last 5 lines
tail -5 file.txt    # same as above

# displays last 5 bytes
tail -c 5 file.txt

# will start monitoring the file in real-time, exit by pressing Ctrl + c
tail -f file.txt

# for multiple files
tail file1.txt file2.txt

# can be used with other commands
ps -ef | tail -2    # gets last 2 lines of command result
```

### head
`head` is similar to tail but the opposite. It displays the first 10 lines. It uses the same `-n` and `-c` options as `tail`. It doesn't have the `-f` option, but instead has additional options: `-v` and `-q`, for verbose and quiet mode, respectively. 

`head [option] [filename]`

```bash
# Does not display filename before each result (-q is usually used with multiple files)
head -q file1.txt file2.txt

# Displays filename before each result
head file1.txt file2.txt

# Always displays filename before each result, even for single files
head -v file1.txt
``` 

### File Descriptors
File descriptors are unique identifiers for files. There are three standard file descriptors associated with each process. 
* 0: stdin (standard input)
* 1: stdout (standard output)
* 2: stderr (standard error)
    
We can use these descriptors to redirect them to a specific output or file.

For instance, if we type some arbitrary unknown command, `aefaes`, this will output some stderr on our terminal. We can then use the stderr descriptor, `2`, to output the error to a specific file. 

`aefaes 2> error.txt` 

We can also output the error to the stdout using the `2>&1` command, and have that be redirected to a file. 

`[command] > output.txt 2>&1`

### &
This command will execute the command in the background in a subshell. This means that the command will immediately return a status of 0 and will not wait for it to finish. This allows you to run multiple processes while the others are running in the background. 

Simply append `&` at the end of the command.  

`[command] &`

### nohup
`nohup` stands for no hangup. There's usually a hangup signal that is sent to the process when a shell is terminated, which triggers all running processes to also be terminated. Therefore, if you want to keep a process running even after closing a terminal, you will want to use this command. 

`nohup [command]`

This is usually used with the `&` command so that it can be executed in the background. 

`nohup [command] &`

The output generated by the command will be directed to the `nohup.out` file, which will be created on the current directory, or in the user's home directory if the current directory has no write permissions. 

You can also redirect the output to a specific file. The command below outputs the stderr to the stdout, which is redirected to the output.out file. 

`nohup [command] > output.out 2>&1 &`

The stderr and stdout can be output on separate files as well.

`nohup [command] > output.out 2> output.err &`

### find
This is one of the most frequently used commands in Linux. It searches for files and directories based on a variety of conditions. 

`find [path/s] [options] [expression]`

Path/s:  

The path specifies where to search for the target files or directories. It will search the current directory by default if nothing is specified. 

Options (multiple options can be used together):

* `-name [name]`: search for file/directory with the specified name (use `-iname` for case insensitive search)
* `-perm [permission]`: search for file/directory with the specified permission (permission must be in octal form, e.g. 744)
* `-type [type]`: find files based on type (separate by comma for multiple types)
    * `f`: regular file
    * `d`: directory
    * `l`: symbolic link
* `-size [size][suffix]`: search by file size (append `+`/`-` before the size to specify greater than or less than)
    * `b`: 512-byte blocks (default)
    * `c`: bytes
    * `k`: kilobytes
    * `M`: megabytes
    * `G`: gigabytes 
* `-empty`: search for files/directories that are empty
* `-user [user]`: search for files/directories owned by specified user
* `-group [group]`: search for files/directories owned by specified group

Expression (append at the end of the find command):

* `-delete`: delete all matching files (for directories, it can only delete empty ones) *[Use with caution]*
* `-exec [command] {} \;`: executes a specified command for all matching files, must be escaped by `\`
    * `{}`: replaced by current file being processed

```bash 
# Find all files with the txt extension
find -name '*.txt'
find ./a -name '*.txt'  # same as above but search from the /a directory

# sets max directory search level to 1
find ./a -maxdepth 1 -name  

# finds files that are greater than 1gb in size
find -type f -size +1G
find -type f -size +1M -size -1G    # 1mb < size < 1gb

# find all empty files/directories and delete them
find -empty -delete

# change command to 644 for all matching files with 777 permission
find -type f -perm 777 -exec chmod 644 {} \;

# search for the world "hello world" inside each script file found
find -type f -name *.sh -exec grep 'hello world' {} \;
```

You can find more info about `find` [here](https://man7.org/linux/man-pages/man1/find.1.html).

### tee
`tee` is used to write to the stdout or other files. It is similar to the `echo` command followed by `>` or `>>`, but the difference is that the `tee` command will also output to the stdout. 

`[command] | tee [option] [filename/s...]`

The output from the `command` will be redirected to the `filename` (or multiple files if more than one is specified). The option `-a` can be used to append to some file instead of overwriting it. 

### export
This command exports variables so that new subshells (child processes) can have access to the exported variables. 

`export [option] [variable]`

Options:
* `-p`: list all exported variables in the current shell
* `-n`: remove exported variable `export -n a`
* `-f`: export functions 
    * `printhello() { echo 'hello'; }`
    * `export -f printhello`

```bash
# exporting variable
var='variable'
bash        # create subshell
echo $var   # outputs nothing
exit

export var
bash        # create subshell
echo $var   # outputs variable
exit

# exporting function
myfunc() { echo 'hello'; }
bash        # create subshell
myfunc      # does nothing
exit

export -f myfunc
bash        # create subshell
myfunc      # prints 'hello'
exit
```

### curl
The `curl` command is a tool for transferring data to and from a server. You'll probably see this most commonly used for http requests (it is also the default if no protocol is specified), but some of the other supported protocols are FTP, TELNET, FILE, etc. You can find the full list of protocols and options [here](https://man7.org/linux/man-pages/man1/curl.1.html).

`curl [option/s] [url/s]`

Options:
* `-s`: silent mode, outputs the data but omits progress meter or error messages
* `-w '%{format}'`: output info to stdout in the specified format
    * `http_code`: gets the numerical response code
* `-o [file]`: store output on a file
* `-O [url]`: download multiple files using multiple `-O` commands

```bash
# http request www.google.com
curl www.google.com

# get http response code from the http request
curl -w '%{http_code}\n' www.google.com

# isolate the http response code from the output by redirecting output to /dev/null
curl -s -w '%{http_code}\n' www.google.com -o /dev/null     # outputs 200 (if successfull)
```

### /dev/null
`/dev/null` is a virtual file that can be written on, typically used for discarding useless info. As you may know, all processes have a stdout. Say we want to get rid of all the output somehow. We can redirect the stdout to the `/dev/null` so that it is not displayed anymore. 

For example, `grep -r hello /sys/` will generate lots of permission denied error messages. We can get rid of all the error messages and only leave the meaningful data we're looking for by writing the error to `/dev/null`.

`grep -r hello /sys/ 2>/dev/null`

Or we can dump everything with `>/dev/null 2>&1`.

### Absolute File Path
We can get the absolute file path using a combination of two commands, `readlink` and `dirname`.

#### readlink
`readlink` gets the absolute path of the link or file.  
> print value of a symbolic link or canonical filename

`readlink -f [filename]`

Option `-f`:
> canonicalize by following every symlink[^symlink] in every component of the given name recursively; all but the last component must exist

#### dirname
This command prints the directory of the supplied path.

`dirname /home/ec2-user/app` outputs `/home/ec2-user`

#### Getting the Absolute Path
Let's now combine the two to get the absolute path of the file. 

`dirname $(readlink -f [filename])`


### source
This is similar to `import` in java. It lets you use the functions defined in another source file.
For instance, we can have a function defined in the `function.sh` file.

```bash
# File: function.sh
#!/bin/bash

function myfunc() {
    echo 'this is from function.sh'
}
```

Then we'll source `function.sh` in our `sourcefunction.sh` file to utilize `myfunc`.

```bash
# File: sourcefunction.sh
#!/bin/bash

source function.sh 

myfunc  # executes myfunc from function.sh
```

Note: the relative path was used for the source file for the sake of simplicity. But since files can move locations, using the absolute path is recommended. 

### lsof
`lsof` (stands for LiSt of Open File) lists all open files. Here's how "file" is defined:

> An open file may be a regular file, a directory, a block special file, a character special file, an executing text reference, a library, a stream or a network file (Internet socket, NFS file or UNIX domain socket.)

`lsof [option] [username]`

Options:
* `-i`: list files that match a specific network address or port
    * `lsof -i tcp:80` 

### wc
This command will count and output the number of lines, words, characters, and bytes of the specified files, depending on the option used. 

`wc [option] [filename/s]`

Options:
* `-l`: output number of lines
* `-w`: output number of words
* `-c`: output number of bytes
* `-m`: output number of characters
* `-L`: output length of longest line


### nc
To check if a specific ip address and port is working, you can easily check with the following command.

`nc -zv [hostname] [port]`

You will get an outp

---
[^symlink]: a symbolic link (symlink, soft link), is similar to shortcuts in windows. It points to some directory or file (even on a different filesystem or partition).