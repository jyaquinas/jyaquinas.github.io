---
layout: post
title: '[LC 416] Partition Equal Subset Sum'
subtitle: Solution Using Dynamic Programming
date: 2022-05-22 16:30:00 +0900
background: '/img/bg-post.jpg'
category: "LeetCode"
tags: [leetcode, algorithm, dynamic programming]
---

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # problem: can integers sum up to sum/2?
        # 2 choices: use integer, not use integer 
        
        # DP (from)
        # the recursive version is essentially looping through all the integers, and adding/not adding to the sum
        s = sum(nums)
        if s % 2 != 0:
            return False
        target = s/2
        
        dp = set([0])
        for n in nums:
            if target in dp: 
                return True
            temp = set()    # cannot modify set during iteration
            for val in dp:
                if val + n <= target:
                    temp.add(val + n)
            dp.update(temp)
        return False
        
        # caching (memoization)
        # time: O(n*t), t=sum/2 -> O(nlogn) if sorted first
        # space: O(n*t)
        s = sum(nums)
        if s % 2 != 0:
            return False
        
        target = s/2
        # nums.sort()
        dp = {}
        
        def dfs(i, s):
            if i == len(nums) - 1:
                return s == target
            if (i,s) in dp:
                return dp[(i,s)]
            
            dp[(i, s)] = dfs(i + 1, s + nums[i]) or dfs(i + 1, s)
            return dp[(i, s)]
        
        return dfs(0, 0)
            
        
        # brute force 
        # time: O(2^n), n = height of tree
        # space: O(n)
        s = sum(nums)
        if s % 2 != 0:
            return False
        
        target = s/2
        nums.sort()
        
        def dfs(i, s):
            if i == len(nums) - 1:
                return s == target
            return dfs(i + 1, s + nums[i]) or dfs(i + 1, s)
        
        return dfs(0, 0)
```