---
layout: post
title: '[LC 338] Counting Bits'
subtitle: Solution Using Dynamic Programming
date: 2022-04-08 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "LeetCode"
tags: [leetcode, algorithm, dynamic programming]
---


```python
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        offset = 1 #offset -> values that only have one '1' in binary (1,2,4,8,16)
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset *= 2
            res[i] = 1 + res[i - offset]
        return res
        
        
        # 0 00 = base case = 0
        # 1 01 = 1 + dp[1-1] (offset 1)
        # 2 10 - 1 + dp[0] = 1 + dp[2 - 2] (offset 2)
        # 3 11 - 1 + dp[1] = 1 + dp[3 - 2]
        # 4 100 - 1 + dp[0] = 1 + dp[4 - 4] (offset 4)
        # 5 101 - 1 + dp[1] = 1 + dp[5 - 4]
        # 6 110 - 1 + dp[2] = 1 + dp[6 - 4]
        # 7 111 - 1 + dp[3] = 1 + dp[7 - 4]
        # 8 1000 - 1 + dp[8 - 8] (offset 8)
```
