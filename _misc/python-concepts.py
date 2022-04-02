# General python language related functions/concepts


# lambda ("anonymous function")

print('lambda')
func = lambda x: x * 2  # bad practice, explanation purpose only (use def instead)
func2 = lambda x, y: x + y  # takes 2 arguments
print(func(3))  # outputs 6
print((lambda x: x * 2)(3))  # outputs 6
print(func2(3, 5))  # outputs 8

# map(func, iter) - map function to iter
print('map')


def double(n):
    return n * 2


iterable = [1, -3, 6, -5]
print(list(map(double, iterable)))

# reduce (reduce iterable to a single value by applying a function that takes in two arguments cumulatively)
print('reduce')
from functools import reduce


def mult(a, b):
    return a * b


print(reduce(mult, iterable))  # (((1*3)*6)*5)

# heapq (heap, min heap by default)
print('heap')
import heapq

heap = [5, 3, 2, 6, 7, 0, 1]
print(heap)
heapq.heapify(heap)
print(heap)
print(heapq.nlargest(3, heap))
print(heapq.nsmallest(3, heap))
heapq.heappush(heap, 10)
print(heapq.heappop(heap))
print(heap)

# for max heap, use negative values, then flip back sign when accessing
heap = [5, 3, 2, 6, 7, 0, 1]
maxHeap = list(map(lambda x: x * -1, heap))
print(maxHeap)
heapq.heapify(maxHeap)
print(maxHeap)
print(heapq.nlargest(3, maxHeap))
print(heapq.nsmallest(3, maxHeap))
heapq.heappush(maxHeap, -10)
print(maxHeap[0])

# heapreplace vs heappushpop
a = [5,3,6,2,6]
heapq.heapify(a)
b = a[:]
rep = heapq.heapreplace(a, -1)      # outputs 2
pushpop = heapq.heappushpop(b, -1)  # outputs -1


# iter()
print('iter')
vowels = ['a', 'e', 'i', 'o', 'u']
v_iter = iter(vowels)
print(next(v_iter, None))  # a
print(next(v_iter, None))  # e
print(next(v_iter, None))  # i
print(next(v_iter, None))  # o
print(next(v_iter, None))  # u
print(next(v_iter, None))

# islice('ABCDEFG', 2) --> A B
# islice('ABCDEFG', 2, 4) --> C D
# islice('ABCDEFG', 2, None) --> C D E F G
# islice('ABCDEFG', 0, None, 2) --> A C E G

# deque ('deck' - double ended queue)
from collections import deque

print('deque')
l = [1, 2, 3, 5]
d = deque(l)
d.append(3)
d.appendleft(9)
print(d)
d.pop()
d.popleft()
print(d)

# product - itertools
from itertools import product

print("product - itertools")
print(list(product(range(3), range(2))))
print(list(product([3, 4, 5], [7, 8, 9])))

# counter - collections
from collections import Counter

print('Counter')
c = Counter('thomasss')
del c['s']
print(c)
print('asdff'.count('f'))  # count occurrence of f

# named tuple - collections
print('named tuples')
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
print(p1)
t = (1, 2, 3, 5)
print(t)

# secondary sort
print('secondary sorting')
l = [[1, 'z'], [3, 'b'], [2, 't'], [7, 't'], [5, 'g']]
l.sort(key=lambda x: (x[1], -x[0]), reverse=True)
print(l)

# bisect
print('bisect')
import bisect

l = [1, 2, 3, 5, 6, 7]
print(l)
print('insert location for 4:', bisect.bisect_left(l, 5))
print('insert location for 4:', bisect.bisect_right(l, 5))

# sorting
print('sorting')


class Student:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def __lt__(self, other):
        return self.name < other.name

    def __repr__(self):
        return self.name + ' ' + self.lastname


students = [Student('thomas', 'kim', 29), Student('abigail', 'cook', 50), Student('john', 'cena', 3)]
students.sort()
print(students)
students.sort(key=lambda x: x.age)
print(students)

from collections import defaultdict

l = defaultdict(int)
l[0] += 1
print(l)
a='(1,2)'
print(a[1:-1].split(','))

a = set([2,3])
for c in a:
    print(c)
