---
layout: post
title: Other Linux Commands You Might Not Know
subtitle: If you're a beginner like me
date: 2022-03-15 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "Linux"
tags: [linux]
---



* Linux wildcards -> file searching
    * `*` match one or more occurrences of characters, including none
    * `?` match single occurrence of character
    * `[]` match any occurrence of characters in the enclosed bracket
    * ./tmp/* matches files and folders in ./tmp
    * ./tmp/** matches files, folders, and subfolders in ./tmp
    * https://stackoverflow.com/questions/3529997/unix-wildcard-selectors-asterisks
* command substitution in linux
    * `$()` is commonly used but you may find other syntaxes, like ` `` ` (former is recommended as it's more readable, and supported in most shells)
    * linux will execute whatever is inside the `$()` before it executes the rest - allows you to input the results of the command into the text of the command
    * `datevar=date` is going to assign the string date into the variable
    * `echo $datevar` will give you `date`
    * `datevar=$(date)` will give you the actual date
* ps -> lists processes
    * https://linuxize.com/post/ps-command-in-linux/
    * https://www.geeksforgeeks.org/ps-command-in-linux-with-examples/
    * https://www.oreilly.com/library/view/linux-pocket-guide/9780596806347/re87.html
    * -e: list full process list
    * -f: full format
    * -p: get for a particular process `ps -p 5553`
    * can be used with filter commands like `grep`
* kill -> kill process
    * https://phoenixnap.com/kb/how-to-kill-a-process-in-linux
    * `kill [pid]` 
    * `kill -9 [pid]` -> force kill (sends SIGKILL signal) -> `-SIGKILL` can also be used

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

* csh - not recommended to use --> [why](https://www.grymoire.com/unix/CshTop10.txt) or [why](http://www.faqs.org/faqs/unix-faq/shell/csh-whynot/)
    * set -> csh?
        * https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-linux
        *  we will get a list of all shell variables, environmental variables, local variables, and shell functions
    * set vs setenv
        * setenv -> variables exported to subshell
        * set -> not exported to subshell
        * setenv ==> `export` in bash