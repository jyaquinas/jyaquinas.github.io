---
layout: post
title: '[LC 417] Pacific Atlantic Water Flow'
subtitle: Solution Using BFS
date: 2022-05-22 18:30:00 +0900
background: '/img/bg-post.jpg'
category: "LeetCode"
tags: [leetcode, algorithm, bfs]
---


```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m, n = len(heights), len(heights[0])
        pacific = [[0] * n for _ in range(m)]
        atlantic = [[0] * n for _ in range(m)]
        res = []
        
        for i in range(m):
            self.bfs(heights, pacific, i, 0, m, n)
            self.bfs(heights, atlantic, i, n - 1, m, n)
        for j in range(n):
            self.bfs(heights, pacific, 0, j, m, n)
            self.bfs(heights, atlantic, m - 1, j, m, n)
        
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i,j])
        return res
                    
    def bfs(self, heights, matrix, r, c, m, n):
        visited = set((r,c))
        q = deque([[r,c]])
        while q:
            i, j = q.popleft()
            matrix[i][j] = 1
            for x,y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nr, nc = i + y, j + x
                if 0 <= nr < m and 0 <= nc < n and (nr,nc) not in visited and heights[nr][nc] >= heights[i][j]:
                    q.append([nr, nc])
                    visited.add((nr, nc))
```