---
layout: post
title: Python Algorithm Tips
subtitle: A few tricks for your interview prep
date: 2022-03-16 22:17:00 +0900
background: '/img/bg-post.jpg'
category: "Python"
tags: [python, algorithm]
---

### Strings
Strings in python are immutable. This means that concatenating or appending to a string will simply copy the entire resulting string to a new variable.

```python
a = '123'
b = a + '4'     # O(n) time
print(id(a) == print(b)) # prints False
```

So instead of appending to the string at every step, which would be **O(n)** time at every step (doing this n times will result in a time complexity of **O(n^2)**), append to a list first and then convert the result to a string only once at the end.


### Backtracking (Recursion)
Let's look at the [permutation problem](https://leetcode.com/problems/permutations/) from LC. You will probably use a function similar to the one below. Most of the backtracking problems have a very similar format.

```python        
def dfs(self, nums: List[int], path: List[int], ans: List[List[int]]):
    if not nums:
        ans.append(path[:])

    for i in range(len(nums)):
        self.dfs(nums[:i]+nums[i+1:], path + [nums[i]], ans)
```

Now, let's focus on this line:

`path + [nums[i]]` on the recursive call. 

But we can achieve the same thing by doing the following:

```python
path.append(nums[i])
self.dfs(nums[:i]+nums[i+1:], path, ans)
path.pop()
```

See the difference? 

You should choose the second method because `path + [nums[i]]` actually creates a new list and copies the value to the new variable. This operation itself is **O(n)**. Yea, it won't make a huge difference for such a small list, but it starts mattering when we're dealing with much larger ones.

On the other hand, `path.append(nums[i])` and `path.pop()` are both **O(1)**. 

We can quickly see this with this example:
```python
a = [1,2,3]
b = a + [4]
a.append(4)
print(id(a) == id(b))   # prints False
```

The final code we get is:
```python
def dfs(self, nums: List[int], path: List[int], ans: List[List[int]]):
    if not nums:
        ans.append(path[:])

    for i in range(len(nums)):
        path.append(nums[i])
        self.dfs(nums[:i]+nums[i+1:], path, ans)
        path.pop()
```
