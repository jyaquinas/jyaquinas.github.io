---
layout: post
title: '[LC 208] Implement Trie (Prefix Tree)'
subtitle: Implementing a Trie Class
date: 2022-05-26 21:38:00 +0900
background: '/img/bg-post.jpg'
category: "LeetCode"
tags: [leetcode, algorithm, trie]
---

```python
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.character = {} #lowercase letters

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.character:
                node.character[c] = TrieNode()
            node = node.character[c]
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.character:
                return False
            node = node.character[c]
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.character:
                return False
            node = node.character[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

```