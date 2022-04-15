---
layout: post
title: Other Linux Commands You Might Find Useful
subtitle: ----
date: 2022-03-15 22:03:00 +0900
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
This allows us to execute some command and use the command result in another command. The syntax, `$()`, is commonly used but you may find other syntaxes, like ` `` ` (former is recommended as it's more readable, and supported in most shells). Linux will execute whatever is inside the `$()` before it executes the rest.

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
This command cuts or splits each line and returning the results to the standard ouput. 

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
`tail` is used for displaying last 10 lines of files. It is quite useful for monitoring file changes in real time, usually for reading/monitoring log files, using the `-f` option.

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

# will start monitoring the file in real time, exit by pressing Ctrl + c
tail -f file.txt

# for multiple files
tail file1.txt file2.txt

# can be used with other commands
ps -ef | tail -2    # gets last 2 lines of command result
```

### head
`head` is similar to tail but the opposite. It displays the first 10 lines. It uses the same `-n` and `-c` options as tail. It doesn't have the `-f` option, but instead has additional options: `-v` and `-q`, for verbose and quite mode, respectively. 

`head [option] [filename]`

```bash
# Does not display filename before each result (-q is usually used with multiple files)
head -q file1.txt file2.txt
# Displays filename before each result
head file1.txt file2.txt
# Always displays filename before each result, even for single files
head -v file1.txt
``` 

* nohup (no hangup)
    * keeps process running even after terminal is closed


* find 
    * https://www.tecmint.com/35-practical-examples-of-linux-find-command/#:~:text=The%20Linux%20find%20command%20is,files%20that%20match%20the%20arguments.
    * by default current directory, or specify the path by `find [path] ..`
    * some examples
        * find -name '*.txt'
        * find ./a -name '*.txt'
        * find ./a -maxdepth 1 -name 'a.txt' ==> sets max directory level
* tee
    * https://phoenixnap.com/kb/linux-tee
    * reads from standard input and writes it to standard output & one or more files
    * `echo 'textblabla' | tee -a file.txt` or `tee -a file.txt` then type the text to be input, exit with ctrl + z
    * `-a` is used to append more text (instead of overwritting)
    * similar to using `echo 'textblabla' >> file.txt`, but the difference is that `tee` will output the text to the stout as well
    * another difference is that `tee` can input text into multiple files as opposed to the method mentioned above
* `&` command
    * executes the command in the background - linux will not wait for the command to finish
    * `./shell.sh &` -> in the script, say there is sleep 5, then linux will execute on the background and not wait for it -> other commands can be run while it is running in the background

* export
    * https://linuxconfig.org/learning-linux-commands-export
    * exports variables "globally" so that new subshells can have access to the variables
    * `a = 'variable'`
    * `export a`
    * `bash`
    * `echo $a` -> will print variable
    * options: `-p`, `-n`, `-f`
    * -p: list all exported variables
    * -n: remove exported variable `export -n a`
    * -f: export functions 
        * `printhello() { echo 'hello'; }`
        * `export -f printhello`

* `$$`
    * https://tldp.org/LDP/abs/html/internalvariables.html
    * process id of script itself
* assigning results of a command to a variable
    * wrap around ``
    * `` array=`find . -maxdepth 1 -name '*.txt'` ``
    * results are saved into the array variable
    * use the command `set` in csh
        * `` set array=`find . -maxdepth 1 -name '*.txt'` ``
* curl
    * `-s`: silent mode, outputs the data but omits progress meter or error messages
    * `-w [format]`: output info to stdout in the specified format
        * `curl -w '%{http_code}\n' https://example.com` -> outputs html code, like 200
    * `-o [file]`: store output on a file
    * https://phoenixnap.com/kb/curl-command#:~:text=apt%20install%20curl-,What%20Is%20the%20curl%20Command%3F,to%20be%20sent%20or%20received.

* file descriptors
    * 1: stdout
    * 2: stderr
    * `aefaes 2> error.txt` -> unknown command `aefaes` will throw an error, we can output that error to the error.txt file using the stderr descriptor, 2
* `/dev/null` -> virtual file that can be written on, used for discarding useless info
    * ex: `grep -r hello /sys/` will generate lots of permission denied error messages. We can get rid of all the error messages and only leave the meaningful data we're looking for by writing the error to /dev/null
    * `grep -r hello /sys/ 2>/dev/null`
    * similarly, we can dump stdout and leave only errors using `1>/dev/null`
    * dump everything with `>/dev/null 2>&1` (dumps sterr to stdout, then stdout to null)
* #!/usr/bin/env bash vs #!/bin/bash
    * https://stackoverflow.com/questions/16365130/what-is-the-difference-between-usr-bin-env-bash-and-usr-bin-bash
    * env -> more flexibility on diff systems, will use the first executable that appears on the users `$PATH`
        * con: diff executables can lead to script running differently or unexpectedly

* absolute path of file
    * readlink
        * > print value of a symbolic link or canonical file name
        * gets the absolute path of the link or file
        * `readlink -f [filename]`
        * option `-f`
            * > -f, --canonicalize canonicalize by following every symlink in every component of the given name recursively; all but the last component must exist
        * symbolic link (symlink, soft link) 
            * similar to shortcuts in windows, points to some directory or file (even on a different filesystem or partition)
        * can be used with dirname to get absolute path of a certain file
    * dirname
        * prints directory of of the supplied path
        * `dirname /home/ec2-user/app` -> outputs `/home/ec2-user`
    * combine to get absolute path
        *  `dirname $(readlink -f [filename])`
* source
    * similar to import in java
    * can use the functions defined in the source file
    * https://linuxize.com/post/bash-source-command/#:~:text=The%20source%20command%20reads%20and,Linux%20and%20UNIX%20operating%20systems.
* `lsof`
    * list all files that are open
    * `lsof [option] [username]`
    * `-i`: list files that match a specific network address or port
        * `lsof -i tcp:80`
* `$0`
    * gets name of shell or shell script
* `wc`
    * word count -> outputs 4 columns (number of lines, words, characters/bytes, filename)
    * `wc -l [filename]`: outputs number of lines present in the file
    * https://www.geeksforgeeks.org/wc-command-linux-examples/
    


* csh - not recommended to use --> [why](https://www.grymoire.com/unix/CshTop10.txt) or [why](http://www.faqs.org/faqs/unix-faq/shell/csh-whynot/)
    * set -> csh?
        * https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-linux
        *  we will get a list of all shell variables, environmental variables, local variables, and shell functions
    * set vs setenv
        * setenv -> variables exported to subshell
        * set -> not exported to subshell
        * setenv ==> `export` in bash