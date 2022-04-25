---
layout: post
title: '[LC 740] Delete and Earn'
subtitle: ---
date: 2022-04-08 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "LeetCode"
tags: [leetcode, algorithm, dynamic programming]
---


```python
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        # dp(i): max score up to number i
        # dp(i) = max(i + dp(i - 2), dp(i - 1)) if i -1 exists
        
        nums.sort() # O(nlogn)
        counter = collections.Counter(nums)
        maxval = 0
        prev, bprev, prevnum = 0,0,0
        
        for n,cnt in counter.items():
            if prevnum == n - 1:
                maxval = max(n * cnt + bprev, prev)
            else:
                maxval += n * cnt
            bprev, prev, prevnum = prev, maxval, n
        return maxval
```