---
layout: post
title: '[LC 377] Combination Sum IV'
subtitle: Solution Using Dynamic Programming
date: 2022-05-19 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "LeetCode"
tags: [leetcode, algorithm, dynamic programming]
---

```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:        
    # dp[i]: number of combinations that sum up to i
    # dp[i] = 
    
    # 1: 1 -> 1
    # 2: 11, 2 -> 2
    # 3: 111, 12, 21, 3 -> 4
    # 4: 1111, 112, 121, 211, 22, 31, 13 -> 7
    
    # 1: dp[1-1] + 1 (self) = 1
    # 2: dp[2-1] + dp[2-2] + 1 (self) = 1+0+1 = 2
    # 3: dp[3-1] + dp[3-2] + dp[3-3] + 1(self) = 2 + 1 + 0 + 1 = 4
    # 4: dp[4-1] + dp[4-2] + dp[4-3] = 4 + 2 + 1 = 7
    
        dp = [0] * (target + 1)
        for n in nums:
            if n <= target:
                dp[n] = 1   # + 1 combination for addition with itself
        for i in range(1, target + 1):
            for n in nums:
                if i - n >= 0:
                    dp[i] += dp[i - n]
        return dp[-1]
    
```