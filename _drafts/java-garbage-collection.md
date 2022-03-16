---
layout: post
title: Java Garbage Collection
subtitle: ----
date: 2022-03-16 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "Java"
tags: [java, gc, heap memory]
---


* young (eden + 2 survivor spaces), old (tenure), permanent generation, and GC?
    * https://blog.devgenius.io/java-garbage-collection-what-is-the-young-generation-old-generation-and-permanent-generation-953462ae2598
    * https://www.oracle.com/webfolder/technetwork/tutorials/obe/java/gc01/index.html
    * https://www.overops.com/blog/improve-your-application-performance-with-garbage-collection-optimization/
    * https://www.oracle.com/java/technologies/javase/gc-tuning-6.html
    * https://www.ateam-oracle.com/post/visualising-garbage-collection-in-the-jvm
    * permanent generation is where JVM keeps data it needs -> metadata about the objects created, not part of the heap
    * different sections of the heap that are differentiated by objects 'age' -> older objects are less likely to be marked for deletion
    * when object is allocated to heap, it is first placed in the eden space 
    * if they pass a certain 'age' threshold, they are moved to the survivor space, and even longer ones to the tenured/old space
    * minor GC (young generation) occurs a lot more frequently, deleting most objects, and ignoring those in the tenured/old space
    * major GC (from old generation)
    Eden Space (heap): The pool from which memory is initially allocated for most objects.

    * https://docs.oracle.com/javase/7/docs/technotes/guides/management/jconsole.html
        > Survivor Space (heap): The pool containing objects that have survived the garbage collection of the Eden space.  
        > Tenured Generation (heap): The pool containing objects that have existed for some time in the survivor space.  
        > Permanent Generation (non-heap): The pool containing all the reflective data of the virtual machine itself, such as class and method objects. With Java VMs that use class data sharing, this generation is divided into read-only and read-write areas.  
        > Code Cache (non-heap): The HotSpot Java VM also includes a code cache, containing memory that is used for compilation and storage of native code.

* why is GC "stop the world" event not desirable?
    * this occurs whenever there's a minor/major GC
    * this will stop all application threads so that the GC can be executed and completed
    * if this event occurs frequently, it can cause performance issues 
    * the goal is to keep this event as rare as possible, this is where GC tuning comes in 
