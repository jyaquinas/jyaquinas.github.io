---
layout: post
title: '[LC 207] Course Schedule'
subtitle: ---
date: 2022-04-08 22:03:00 +0900
background: '/img/bg-post.jpg'
category: "LeetCode"
tags: [leetcode, algorithm, topological sort]
---

## [LeetCode 207](https://leetcode.com/problems/course-schedule/)


---
Pseudocode:  
Khan's Alg (indegree)

* determine the indegree of nodes, then start with those with indegree of 0 (no incoming edges) -> add to topo order
* (if no node with indegree of 0 -> there's a cycle)
* perform dfs on nodes while removing them from the graph (decreasing the indegree)
* each time we find a node with no more incoming edges left (indegree 0), add to the stack for bfs (and to topo order)
* repeat until all graph is traversed

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjlist = [[] for i in range(numCourses)]
        indeg = [0] * numCourses

        for course, req in prerequisites:
            adjlist[course].append(req)
            indeg[req] += 1

        s = []
        cnt = 0
        for i in range(numCourses):
            if indeg[i] == 0:
                s.append(i)
                cnt += 1

        while s:
            c = s.pop()
            for adj in adjlist[c]:
                indeg[adj] -= 1
                if indeg[adj] == 0:
                    s.append(adj)
                    cnt += 1

        return cnt == numCourses
```
