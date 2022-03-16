---
layout: post
title: Trie Data Structure
subtitle: The data structure I've been neglecting
date: 2022-02-07 13:18:00 +0900
background: '/img/bg-post.jpg'
category: "Data Structures"
tags: [data structures, algorithms, trie, python]
---


I think I first came across the concept of a trie (pronounced *try*) when I was reading the book *Cracking the Coding Interview*. But I never really gave it much thought. Plus, I never came across a problem on [Leet Code](https://www.leetcode.com) where I had to use one (at least for me). But I recently came across a problem where using a trie was the only way to efficiently solve the problem.

Let's briefly go over the basics.

A trie is a special type of tree that can compactly store strings. This is especially true if the words are very similar, i.e. having overlapping parts, like prefixes.

Each node contains a boolean flag, `isEndOfWord`, that can be used to indicate the end of a word. Now, this can vary depending on the implementation. If you'd like to associate a value for each word, you'd simply replace the bool variable with something like an int to store the value.

The node's children consist of all the possible characters of a word. So if we limit it to lowercase alphabets, a-z, it can have up to 26 children (stored in an array).

**Pros**
* space-efficient if storing similar words
* efficient for looking up prefixes
* relatively fast insert and lookup

**Cons**
* space inefficient for non-overlapping words
* slower than hash table (depends on how the hash value is calculated)

Here is the implementation in python.

```python
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isEndOfWord = True

    def search(self, word):
        node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.isEndOfWord

    def delete(self, word):
        node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        node.isEndOfWord = False
        return True

```

Let's test it.
```python
t = Trie()
words = ['camp', 'camper', 'cat', 'cater']
print('Inserting words: ', words)

for word in words:
    t.insert(word)

for word in words:
    print(word, 'is in trie?', t.search(word))

deletewords = ['car', 'camper']
print('Delete words: ', deletewords)

for word in deletewords:
    print(word, 'deleted?', t.delete(word))
for word in words:
    print(word, 'is in trie?', t.search(word))
```

Outputs:
```
Inserting words:  ['camp', 'camper', 'cat', 'cater']
camp is in trie? True
camper is in trie? True
cat is in trie? True
cater is in trie? True
Delete words:  ['car', 'camper']
car deleted? False
camper deleted? True
camp is in trie? True
camper is in trie? False
cat is in trie? True
cater is in trie? True
```
