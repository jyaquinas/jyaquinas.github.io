
---
layout: post
title: '[LC 438] Target Sum'
subtitle: Solution Using Dynamic Programming
date: 2022-05-25 21:47:00 +0900
background: '/img/bg-post.jpg'
category: "LeetCode"
tags: [leetcode, algorithm, dynamic programming]


```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # dp solution?
        

        # 0,0 -> 1,1 -> 2,2 -> 3,3 -> 4,4 -> 5,5 X
        # 0,0 -> 1,1 -> 2.2 -> 3,3 -> 4,4 -> 5,3 O
        
        # 2nd level, repeated node (2,0)
        # 0,0 -> 1,1 -> 2.2 -> 3,3 -> 4,2 -> 5,3 O
        # 0,0 -> 1,1 -> 2,0 ->
        # 0,0 -> 1,-1 -> 2,0 ->
        # 0,0 -> 1,-1 -> 2,-2
        
        # Caching (memoization)
        # time: O(n*t), t: sum of n 
        # space: O(n*t)
        
        cache = {}
        def dfs(i, cursum):
            if (i, cursum) in cache:
                return cache[(i, cursum)]
            if i >= len(nums):
                return cursum == target
            
            cache[(i, cursum)] = dfs(i + 1, cursum + nums[i]) + dfs(i + 1, cursum - nums[i])
            
            return cache[(i, cursum)]
        
        return dfs(0, 0)
        
        
        # Brute force
        # Try all choices (add, subtract)
        # time: O(2^n)
        # space: O(n)
        def dfs(i, cursum):
            if i >= len(nums):
                return cursum == target
                
            return dfs(i + 1, cursum + nums[i]) + dfs(i + 1, cursum - nums[i])
        
        return dfs(0, 0)
```