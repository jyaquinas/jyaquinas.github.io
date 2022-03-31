---
layout: post
title: '[LC 438] Find All Anagrams in a String'
subtitle: ---
date: 2022-03-31 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "LeetCode"
tags: [leetcode, algorithm, ]
---

## [LeetCode 438](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
> Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
>
>An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
>
> 
>
>Example 1:
>
>Input: `s = "cbaebabacd", p = "abc"`
>Output: `[0,6]`
>Explanation:
>The substring with start index = 0 is "cba", which is an anagram of "abc".
>The substring with start index = 6 is "bac", which is an anagram of "abc".
>Example 2:
>
>Input: `s = "abab", p = "ab"`
>Output: `[0,1,2]`
>Explanation:
>The substring with start index = 0 is "ab", which is an anagram of "ab".
>The substring with start index = 1 is "ba", which is an anagram of "ab".
>The substring with start index = 2 is "ab", which is an anagram of "ab".
---


```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m, n = len(s), len(p)
        if n > m:
            return []
        
        res = []
        p_hash = r_hash = 0
        p_hm = [0] * 26
        s_hm = [0] * 26
        
        for c in p:
            p_hash += ord(c)
            p_hm[ord(c) - ord('a')] += 1
        for i in range(n):
            r_hash += ord(s[i])
            s_hm[ord(s[i]) - ord('a')] += 1
            

        for i in range(m - n + 1):
            if r_hash == p_hash and p_hm == s_hm:
                res.append(i)
            
            r_hash -= ord(s[i])
            s_hm[ord(s[i]) - ord('a')] -= 1
            
            if i + n < m:
                r_hash += ord(s[i + n])
                s_hm[ord(s[i + n]) - ord('a')] += 1
                
        return res
```
**Time: O(n)**  
**Space: O(1)** -> const array of size 26