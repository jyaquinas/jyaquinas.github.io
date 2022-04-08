---
layout: post
title: '[LC 547] Number of Provinces'
subtitle: ---
date: 2022-04-08 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "LeetCode"
tags: [leetcode, algorithm, ]
---



```python
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        provinces = 0
        for i in range(n):
            if isConnected[i][i]:
                provinces += 1
                self.dfs(i, isConnected)
        return provinces
        
        
    def dfs(self, city, isConnected):
        s = []
        s.append(city)
        while s:
            c = s.pop()
            isConnected[c][c] = 0
            for neighbor, connected in enumerate(isConnected[c]):
                if connected and neighbor != c:
                    s.append(neighbor)
                    isConnected[c][neighbor] = 0
```