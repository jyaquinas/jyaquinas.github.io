---
layout: post
title: ---
subtitle: ---
date: 2022-02-22 22:03:00 +0900
background: '/img/bg-post.jpg'
category: ""
tags: []
---

## Misc Subjects
* testing functions without return values
    * https://coderbook.com/@marcus/how-to-unit-test-functions-without-return-statements-in-python/
    * https://docs.python.org/3/library/unittest.mock.html
* using patch and setting return values to the mock class
    * https://stackoverflow.com/questions/18191275/using-pythons-mock-patch-object-to-change-the-return-value-of-a-method-called-w
    * https://alexmarandon.com/articles/python_mock_gotchas/
    
* python is pass by object reference:
    * mutable objects (list, dic, set, etc) -> passed by ref
    * immutable objects (str, int, tuple, etc) -> passed by val
    ```python
    # pass by value or ref -> in python pass by obj ref
    def addMutable(obj):
        obj.append(1)
        obj[0]=0
    l = [1,2]
    addMutable(l)
    print(l)

    def addImmutable(obj):
        obj+=2
    a=5
    addImmutable(a)
    print(a)
    ```
* python heapq -> heapreplace(arr, val) heappushpop(arr, val)
    * heappushpop() will push value to the heap first before popping the min value
    * heapreplace() is a one step pop and replace operation, more efficient than heappushpop, but will get the min value from the heap disregarding the val that is being input. That means that the popped value can be larger than the value being input. 

* classmethod vs staticmethod
    * https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod
    * staticmethod 
        * equivalent to the static methods seen in other languages
        * cannot access/modify class state
        * usually for utility functions
        * example: 'asdf'.isupper() 
    * classmethod
        * can access/modify class state (some class variable that will affect all class instances)
        * receives class as implicit first argument
        * commonly used for factory methods (alternative constructor??)

        ```python
        # from geekforgeeks
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            
            # a class method to create a Person object by birth year.
            @classmethod
            def fromBirthYear(cls, name, year):
                return cls(name, date.today().year - year)
        ```
        * example: dict.fromkeys() - return a dict instance from the arguments
