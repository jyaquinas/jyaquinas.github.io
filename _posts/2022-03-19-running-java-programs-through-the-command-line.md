---
layout: post
title: Running Java Programs Through the Command Line
subtitle: Basics of java command
date: 2022-03-19 09:28:00 +0900
background: '/img/bg-post.jpg'
category: "Java"
tags: [java, cli]
---

### Why Run Java Through the Command Line Interface (CLI)?
When you're developing on your computer, you can compile and run your java programs through the SDK. But when you're deploying it on a cloud server, in many cases, you will only have access to the CLI. 

You might also have to run multiple java programs to get your application starting. So instead of manually executing them, you can write a short shell script where it will execute all of them for you. That way, you'll only have to run the script. 

### Basics of Java Command
This is the basic syntax:

`java [options] mainclass [args...]`

*Note: this can only run compiled java programs, so make sure to compile your files first using the `javac` command.*

The java command will start a java application by loading the java virtual machine (JVM), loading the specified `mainclass`, and calling the main method. The arguments, `args`, specified in the command will be passed to the main method. 

Let's look at this simple java program.

```java
// HelloWorld.java
public class HelloWorld{
    public static void main(String[] args){
        for(String s:args){
            System.out.println(s);
        }
    }
}
```

Let's compile and run this in the command line.
```shell
javac HelloWorld.java
java HelloWorld hello world
# hello
# world
```

The arguments `hello` and `world` were passed to the main function and were printed out. 

### Java Command Options
The options can be mainly divided into 3 parts: standard, extra, and advanced.

#### Standard Options
These options are used for the most basic actions, such as setting the classpath or the verbose output. Here are a few standard options.

`-cp`  
Sets the classpath where the user-defined classes/packages are, i.e. classes that are not java extensions or part of the java platform. If this is not used, it will default to the `CLASSPATH` environment variable. If this variable isn't set, then it will default to the current directory.

`-verbose:GC`  
Displays info about each garbage collection (GC) event. Note that the alias `-XX:+PrintGC` has been deprecated in >= Java 9

`-verbose:class`  
Displays info about the loaded class.

`-verbose:module`  
Displays info about modules in use.

`-D[property]=[value]`  
Sets the system properties where `property` is a string with no spaces and `value` is a string but can contain spaces (if so, must be enclosed in quotations). This can be used for custom system properties, which can be used with external frameworks if needed. 

#### Extra Options
These options start with `-X` and are options for the Java Hotspot VM.

`Xms[size]`  
Sets the minimum and initial size of the heap. The `size` must be a multiple of 1024 and must be greater than 1MB, such as `-Xms4G`.  
`-XX:MinHeapSize` and `-XX:InitialHeapSize` can be used instead to set min and init heap size, respectively.

`-Xmx[size]`  
Sets the max size of the heap. The `size` shouldn't be greater than the physical memory of the machine. Oracle also recommends setting this value so that the heap is 30% full after a full GC event (you can check through the GC log).  
`-XX:MaxHeapSize` can also be used.

`-Xlog:gc:[file]`  
Outputs additional info about the GC into the file. You may also find `-Xloggc:[file]`, which has been deprecated since Java 9.

#### Advanced Options
Advanced options start with `-XX` and they are used for specific areas (runtime behavior, gathering system info, garbage collection, etc) of the Java Hotspot VM.

Different options will be used differently. But here are a few types of options that can be used.

**Boolean Options**  
These are enable/disable options that are disabled/enabled by default. You can set them by using the `+` or `-` sign, like the following:  
`-XX:+OptionName` -> enable  
`-XX:-OptionName` -> disable  

**Options with Arguments**  
If an option requires an argument, you can separate the option with the argument using a space, colon, or an equal sign.  
Use the following suffixes to specify size:  
* `k`, `K` for kb
* `m`, `M` for mb
* `g`, `G` for gb

For example: 8g, 8192m, or 8589934592.

`-XX:NewRatio=[ratio]`  
Sets the ratio between the young and old generation[^gc] sizes. The default young-to-old ratio is 2.

`-XX:NewSize=[size]`  
Sets initial size of the heap for young generation. Java recommends keeping the size > 25% and < 50% of the overall heap size.

`-XX:SurvivorRatio=[ratio]`  
Sets the ratio between eden and survivor space sizes[^ygc] (within the young generation). The default is 8.

`-XX:[+-]UseAdaptiveSizePolicy`  
Enabled by default, automatically resizes the generations (heap).

`-XX:HeapDumpPath=[path]`  
Sets the path/filename for writing the heap dump from heap profiler (HPROF), when the dumping of java heap on `OutOfMemoryError` exception is thrown (set by the `-XX:+HeapDumpOnOutOfMemoryError` -> disabled by default).

### More Info
There are tons more. You can check out the [documentation](https://docs.oracle.com/en/java/javase/13/docs/specs/man/java.html#using-the-jdk_java_options-launcher-environment-variable) for more information about the java command.

---
[^gc]: Young and old generation sizes refer to the heap sections in Java used for garbage collection. These can be tuned to optimize the java GC. Check out this [blog post](https://blog.devgenius.io/java-garbage-collection-what-is-the-young-generation-old-generation-and-permanent-generation-953462ae2598) for more info.  
[^ygc]: The eden and survivor spaces are part of the young generation. Refer to the blog post mentioned above.
