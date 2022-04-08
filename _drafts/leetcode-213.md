---
layout: post
title: '[LC 213] House Robber II'
subtitle: ---
date: 2022-04-08 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "LeetCode"
tags: [leetcode, algorithm, ]
---


```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        
    
    # dp(i) : max money at house i, nums[i]
    # dp(i) = max(nums[i] + dp(i-2), dp(i-1)) 
        # if you select the current money, you can select max 2 houses before. if not, you can only select the previous house.
    # if 0th house selected, cannot select 1st and last -> 2 ~ n - 1
    # if 0th house not selected -> 1st ~ nth
    # key: do house robber I twice
    
        return max(nums[0] + self.helper(nums[2:-1]), self.helper(nums[1:]))
    
    def helper(self, nums):
        pprev, prev = 0, 0
        maxval = 0
        for i in range(len(nums)):
            maxval = max(pprev + nums[i], prev)
            pprev, prev = prev, maxval
        return maxval
```