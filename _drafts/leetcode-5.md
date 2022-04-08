---
layout: post
title: '[LC 5] Longest Palindromic Substring'
subtitle: ---
date: 2022-04-08 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "LeetCode"
tags: [leetcode, algorithm, ]
---


```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        maxlen = 0
        st = s[0]
        for i in range(len(s)):
            for l, r in [[i , i], [i, i + 1]]:
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                if r - l - 2 > maxlen:
                    maxlen = r - l - 2
                    st = s[l+1:r]
        return st
```