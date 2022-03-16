---
layout: post
title: Java Command
subtitle: ----
date: 2022-03-16 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "Java"
tags: [java, cli]
---

* java cli commands
    * https://docs.oracle.com/en/java/javase/13/docs/specs/man/java.html#using-the-jdk_java_options-launcher-environment-variable
* basic syntax:
    * `java [options] mainclass [args...]`
        * it starts a java runtime environment (JRE) or the java virtual machine (JVM), loads the specified main class, and calls the `main` method of that class
        * passes in the program arguments as arguments for the main method
* standard options
    * -cp: class path -> sets the class path where the user-defined ("classes that are not java extensions or part of java platform") classes/packages are defined -> `;` separated list of directories, jar files,
        * if -cp not used, defaults to the CLASSPATH environment variable, or the current directory if the variable isn't set
    * -verbose:gc -> display info about each garbage collection (GC) event
        * the alias `-XX:+PrintGC`, has been depracated in >= Java 9
    * -verbose:class -> display info about loaded class
    * -verbose:module -> display info about modules in use
* extra options
    * start with `-X` -> options for Java HotSpot Virtual Machine
    * `-Xms[size]` -> set minimum and initial size of heap
        * must be multiple of 1024, greater than 1MB
        * `-Xms4G`
        * `-XX:MinHeapSize` and `-XX:InitialHeapSize` can be used instead 
        to set min and init heap size, respectively
        * if not set, it will be set to sum of young and old generation size
    * `-Xmx[size]` -> set max size of heap
        * can also use `-XX:MaxHeapSize`
        * should not exceed the physical memory of the machine
        * recommended to set so that heap is 30% full after a full GC (can check through GC log)
    * `-Xloggc:[file]` -> outputs additional info about gc into the file
        * depracated -> >= Java 9 `-Xlog:gc:[file]` is used
* advanced options 
    * start with `-XX` -> options for tuning specific areas (runtime behavior, dynamic just-in-time (JIT) compilation, gathering system info, garbage collection) of Java Hotspot VM
    * Boolean options -> enable/disable options that are disabled/enabled by default
        * enable using `-XX:+OptionName`
        * disable using `-XX:-OptionName`
    * if option requires an argument, separate from the option by a space, colon, or an equal sign (differs for each option)
    * specifying size -> use no sufix, or suffix `k`, `K` for kb, `m`, `M` for mb, `g`, `G` for gb
        * ex:  8g, 8192m, 8388608k, or 8589934592
    * specifying percentage -> values from 0 to 1, e.g. 0.25 for 25%
    * `-XX:NewRatio=[ratio]` -> set ratio between young and old generation sizes (default young-to-old ratio = 2)
    * `-XX:NewSize=[size]` -> sets initial size of heap for young generation 
        * java recommends keeping the size > 25% and < 50% of the overall heap size
    * `-XX:SurvivorRatio=[ratio]` -> sets ratio between eden and survivor space size (within the young generation) ==> default is 8
    * `-XX:[+-]UseAdaptiveSizePolicy` -> enabled by default, automatically resizes the generations (heap)
    * `-XX:HeapDumpPath=[path]` -> sets the path/filename for writing the heap dump from heap profiles (HPROF), when the dumping of java heap on `OutOfMemoryError` exception is thrown (set by the `-XX:+HeapDumpOnOutOfMemoryError` -> disabled by default)
