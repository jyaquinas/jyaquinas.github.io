---
layout: post
title: '[LC 424] Longest Repeating Character Replacement'
subtitle: Solution Using Sliding Window
date: 2022-05-24 21:34:00 +0900
background: '/img/bg-post.jpg'
category: "LeetCode"
tags: [leetcode, algorithm, sliding window]
---

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq =defaultdict(int)
        maxlen = maxf = l = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            maxf = max(maxf, freq[s[r]])
            while r - l + 1 - maxf > k:
                freq[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen
```