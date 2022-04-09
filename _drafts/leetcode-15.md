---
layout: post
title: '[LC 15] 3Sum'
subtitle: ---
date: 2022-04-08 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "LeetCode"
tags: [leetcode, algorithm, ]
---

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                tot = nums[i] + nums[l] + nums[r]
                if tot == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif tot < 0:
                    l += 1
                else:
                    r -= 1
        return res
```