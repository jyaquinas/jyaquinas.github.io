---
layout: post
title: Basic Linux Commands
subtitle: A quick overview
date: 2022-02-13 09:44:00 +0900
background: '/img/bg-post.jpg'
category: "Linux"
tags: [linux]
---

### pwd
This will print out the current working directory that you're in. It will usually be something like `/home/user`.

### cd
This is the command used for navigating through the directories. You can either input the absolute path or relative to your current directory.  

Let's say our current directory is `/home/user`, and we have a folder named "a" in there.
* `cd a` or `cd /home/user/a` will take us to `/home/user/a`
* `cd ..` will move one directory up
* `cd -` will move to the previous directory

### ls
Use this to print out the contents in your current directory[^1]. So if we have the following files in our home directory: a.txt, b.txt, c.txt  

`ls` will print out `a.txt b.txt c.txt`.  
This command has a couple of command options. Here are a few important ones.
* `ls -a`: list all files including hidden ones
* `ls -l'` list all files in long format (includes information like date created and permissions)
* `ls -R`: recursively lists all files in directory and subdirectory

You can also combine the commands, such as `ls -la`, which will list all files including the hidden ones in long format.

### mkdir & rmdir
This is used to create and delete folders. Just append the folder name at the end, like `mkdir foldername`.  

*Note: `rmdir` only lets you remove empty directories. To remove all of the subdirectories that it contains, use `rm -r foldername`.*

### mv
This is mostly used for moving files around, but it can also be used for renaming files.  
To move a file, simply write the file name, followed by the destination path. `mv filename.txt /home/user/a`.[^2]  
To rename a file, write the old file name, followed by the new file name. `mv oldfilename.txt newfilename.txt`  

### cp
Use this command to copy files to a target destination.  
`cp filename.txt /home/user/a`

### rm
Use this to remove files and directories. As mentioned before, to delete a directory and all of contents or subdirectories that it contains, use `rm -r`.

### touch
This command is used to create a new file. This can be anything from a simple txt file to an html file.  
`touch filename.txt`

### echo
This is used to move some data into some file, usually some text.  
* `echo 'text' > filename.txt`: Use a single greater-than sign to overwrite the file. So this will replace the old data with the new data.  
* `echo 'text' >> filename.txt`: Use two greater-than signs to add data to the file. New data will be added to a new line.  

*Note: If you use a filename that doesn't exist, a new file with the content inside will be created.*

### vi | nano
These are text editors in linux. But since nano is newer and easier to use, let's focus on nano.  

Typing `nano filename.txt` will take you to editor mode. Make the necessary changes, and then save by pressing **Ctrl+O**, exit by pressing **Ctrl+X**.  
You can see the other options you can use on the bottom of the terminal window.

### cat
If you want to know what kind of content is inside a file, use `cat` to print out the content. Simply type `cat filename.txt`.  

You can create a new file by using `cat > newfilename.txt`. You can then type the content you want into the file, then exit by pressing **Ctrl+Z**.

### grep
Use this command to find certain words or phrases within a text.

For instance, if we want to find if the word "hello" exists somewhere in the file, we can use `grep hello filename.txt`.  
This will then display all the lines that contain the word.  

For phrases, place them inside quotes, like `grep 'target phrase' filename.txt`.

### sudo
`sudo` stands for "SuperUser Do". Use this to run commands with administrative or root privileges.

### chmod
This is used for changing the read, write, and execute permissions of files and directories.
I'll provide more info about this in a separate post.



---
[^1]: You can list the contents of another directory if you append the directory's path at the end. `ls /home/user/a`
[^2]: Note that you can also move folders around. Use the folder name instead of the file name.
