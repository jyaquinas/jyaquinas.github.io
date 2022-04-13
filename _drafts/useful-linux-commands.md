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
* `$()` is commonly used but you may find other syntaxes, like ` `` ` (former is recommended as it's more readable, and supported in most shells)
* linux will execute whatever is inside the `$()` before it executes the rest - allows you to input the results of the command into the text of the command

```bash
# Saves the string "date" 
datevar=date
echo $datevar # will output "date"

# Saves the actual date into the variable
datevar=$(date)
echo $datevar # will output the date
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
* `kill [option] [pid]` 
* other kill options (see full list with `kill -l`)
    * `-1`: Reload a process.
    * `-9`: Kill a process.
    * `-15`: Gracefully stop a process.

* awk
    * https://www.geeksforgeeks.org/awk-command-unixlinux-examples/
    * `awk '{print $2, $4}'` : prints 2nd and 4th word (whitespace separated) -> $0 represents entire line
    * by default `awk {print} filename.txt` prints entire file line by line
* tput
    * https://linuxcommand.org/lc3_adv_tput.php
    * can manipulate the terminal's appearance, like color, etc
    * `tput smso` start 'standout' mode
    * `tput rmso` end 'standout' mode
    * `tput sgr0` turn off all attributes
* `$$`
    * https://tldp.org/LDP/abs/html/internalvariables.html
    * process id of script itself
* assigning results of a command to a variable
    * wrap around ``
    * `` array=`find . -maxdepth 1 -name '*.txt'` ``
    * results are saved into the array variable
    * use the command `set` in csh
        * `` set array=`find . -maxdepth 1 -name '*.txt'` ``
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
* `cut` command (newer than awk)
    * https://linuxize.com/post/linux-cut-command/
    * https://www.geeksforgeeks.org/cut-command-linux-examples/
    * options: -f (fields), -b (bytes), -c (characters), -d (delimiter), -s (gets only lines with delimiters)
    * arguments for the list: N (nth field), N- (nth field to the end), N-M (nth to mth field), -N (first to nth field)
    * gets or cuts sections from each line and prints it out to the stout
    * `cut -b 1,2,3 file.txt` -> gets 1,2,3rd byte from each line (tabs and backspaces are counted as 1 byte)
        * mytext -> myt
    * `cut -b 1-3,5-7 file.txt` 
        * mytextbla -> mytxtb
    * `cut -b 1- file.txt` -> 1st bite till the end
    * `cut -b -3 file.txt` -> first byte to 3rd byte
    * `cut -c 1,2,3 file.txt` -> gets the character in specified positions (tabs and backspaces count as 1 char)
    * `cut -f 1,3 file.txt` -> gets 1st and 3rd field delimited by tab (by default)
    * `cut -f 1,3 -d ':' file.txt` -> same as above but uses `:` as delimiter

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
* -head
    * displays first 10 lines
    * similar to -tail (opposite)
    * `-q` -> quiet (does not display the filenames), `-v` -> verbose (displays filenames)
* -tail
    * command used for displaying last 10 lines of files, or monitoring file changes in real time, usually for reading/monitoring log files
    * `tail [filename]` -> default displays last 10 lines
    * `tail -n [number] [filename]` -> displays last n lines' 
        * `tail -[number] [filename]` can also be used instead
    * `tail -c [number] [filename]` -> displays last n bytes
    * `tail -f [filename]` -> will start monitoring the file in real time, exit by pressing `ctrl + c`
    * `tail [filename1] [filename2]` -> for multiple files
    * can be used with other commands, like `ps -ef | tail -2`
* nohup (no hangup)
    * keeps process running even after terminal is closed
    

* csh - not recommended to use --> [why](https://www.grymoire.com/unix/CshTop10.txt) or [why](http://www.faqs.org/faqs/unix-faq/shell/csh-whynot/)
    * set -> csh?
        * https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-linux
        *  we will get a list of all shell variables, environmental variables, local variables, and shell functions
    * set vs setenv
        * setenv -> variables exported to subshell
        * set -> not exported to subshell
        * setenv ==> `export` in bash