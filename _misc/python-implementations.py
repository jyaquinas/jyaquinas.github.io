import unittest

MAXSIZE = 50  # default array size


###################### LINKED LIST IMPLEMENTATION
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(map(str, nodes))


###################### HASH TABLE IMPLEMENTATION (separate chaining) -> O(1) / wcs O(n) where n:chain size
class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.capacity = MAXSIZE
        self.size = 0
        self.buckets = [None] * self.capacity

    # assuming key is in the form of string
    def hash(self, key):
        ind = 0
        for i, c in enumerate(key):
            ind += i * ord(c)
        ind %= self.capacity
        return ind

    def insert(self, key, value):
        self.size += 1
        ind = self.hash(key)
        hn = self.buckets[ind]
        if hn is None:
            self.buckets[ind] = HashNode(key, value)
        else:
            # add to end of LL
            while hn.next is not None:
                hn = hn.next
            hn.next = HashNode(key, value)

    def find(self, key):
        ind = self.hash(key)
        hn = self.buckets[ind]

        while hn is not None and hn.key != key:
            hn = hn.next

        if hn is None:
            return None
        else:
            return hn.value

    def remove(self, key):
        ind = self.hash(key)
        hn = self.buckets[ind]
        prev = None
        val = None

        while hn is not None and hn.key != key:
            prev = hn
            hn = hn.next
        if hn == None:
            # No key found
            return val
        else:
            # key found, remove
            self.size -= 1
            val = hn.value
            if prev == None:  # 1st node in list
                self.buckets[ind] = hn.next  # none or next match
            else:
                prev.next = prev.next.next
            return val


######################### STACK IMPLEMENTATION (using array)
class Stack:
    def __init__(self, size=MAXSIZE):
        self.array = [None] * size
        self.top = -1

    def isFull(self):
        return self.top == MAXSIZE - 1

    def isEmpty(self):
        return self.top == -1

    def push(self, value):
        if self.isFull():
            print('Full')
            return
        self.top += 1
        self.array[self.top] = value

    def pop(self):
        if self.isEmpty():
            print('Empty')
            return
        val = self.array[self.top]
        self.top -= 1
        return val

    def peek(self):
        return self.array[self.top]


######################### STACK IMPLEMENTATION (using linked list)
class StackLL:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def push(self, value):
        newnode = Node(value)
        newnode.next = self.top
        self.top = newnode

    def pop(self):
        if self.isEmpty():
            return None
        else:
            node = self.top
            self.top = self.top.next
            return node.data

    def peek(self):
        return self.top.data


######################### QUEUE IMPLEMENTATION (using array)
class Queue:
    def __init__(self, size=MAXSIZE):
        self.size = size
        self.array = [None] * size
        self.front = 0
        self.rear = 0

    def isFull(self):
        return (self.front + 1) % self.size == self.rear

    def isEmpty(self):
        return self.front == self.rear

    def enqueue(self, value):
        if self.isFull():
            print('Full')
            return
        else:
            self.array[self.front] = value
            self.front += 1
            if self.front == self.size:
                self.front = 0

    def dequeue(self):
        if self.isEmpty():
            print('Empty')
            return
        else:
            val = self.array[self.rear]
            self.rear += 1
            if self.rear == self.size:
                self.rear = 0
            return val


######################### QUEUE IMPLEMENTATION (using linked list)
class QueueLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def enqueue(self, value):
        if self.head is None:  # add first element
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def dequeue(self):
        if self.isEmpty():
            print('Empty')
            return
        else:
            val = self.head.data
            self.head = self.head.next
            return val


######################### HEAP IMPLEMENTATION (min, array-based)
class MinHeap:
    def __init__(self, root, size=MAXSIZE):
        self.maxsize = MAXSIZE
        self.arr = [None] * self.maxsize
        self.arr[1] = root
        self.end = 1
        self.root = 1  # starts at 1 to make implementation easier

    def insert(self, value):
        if self.end >= self.maxsize - 1:
            print('heap full')
        else:
            self.end += 1
            self.arr[self.end] = value
            current = self.end
            while self.arr[current] < self.arr[self.__parent(current)]:
                self.__swap(current, self.__parent(current))
                current = self.__parent(current)
                if current == self.root:
                    break

    def pop(self):
        minval = self.arr[self.root]
        self.arr[self.root] = self.arr[self.end]
        self.end -= 1
        self.__heapify(self.root)
        return minval

    # helper (private) funcs
    def __swap(self, pos1, pos2):
        self.arr[pos1], self.arr[pos2] = (self.arr[pos2], self.arr[pos1])

    def __parent(self, pos):
        return pos // 2

    def __leftChild(self, pos):
        return pos * 2

    def __rightChild(self, pos):
        return pos * 2 + 1

    def __isLeaf(self, pos):
        return self.end >= pos > self.end // 2

    def __heapify(self, pos):
        if self.__isLeaf(pos):
            return
        elif self.arr[pos] > self.arr[self.__leftChild(pos)] or self.arr[pos] > self.arr[self.__rightChild(pos)]:
            if self.arr[self.__leftChild(pos)] < self.arr[self.__rightChild(pos)]:  # left is smaller, swap with left
                self.__swap(pos, self.__leftChild(pos))
                self.__heapify(self.__leftChild(pos))
            else:  # swap with right
                self.__swap(pos, self.__rightChild(pos))
                self.__heapify(self.__rightChild(pos))


# heap=MinHeap(50)
# heap.insert(55)
# heap.insert(40)
# heap.insert(60)
# heap.insert(55)
# heap.insert(65)
# heap.insert(25)
# heap.insert(10)
# print(heap.pop())
# print(heap.pop())
# print(heap.pop())

######################### DFS IMPLEMENTATION


######################### BFS IMPLEMENTATION


######################## BINARY SEARCH
def binarySearch(arr, target):
    L = 0
    R = len(arr) - 1
    while L <= R:
        m = (R - L) // 2 + L
        if target == arr[m]:
            return m
        elif target > arr[m]:
            L = m + 1
        else:
            R = m - 1
    return -1


# arr=[1,3,6,7,8,10,12]
# print(binarySearch(arr,8)

######################### BINARY SEARCH TREE (find, insert, delete, bfs, dfs_in-pre-post) -> O(n)
class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        print(self.data)


class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, root, value):
        if not root or root.data == value:
            print('root null or value exists')
            return
        elif value > root.data:  # insert right
            if root.right:
                self.insert(root.right, value)
            else:
                root.right = TNode(value)
        elif value < root.data:  # insert left
            if root.left:
                self.insert(root.left, value)
            else:
                root.left = TNode(value)

    def visitInOrder(self, node):
        if node:
            self.visitInOrder(node.left)
            print(node.data)
            self.visitInOrder(node.right)

    def visitPreOrder(self, node):
        if node:
            print(node.data)
            self.visitPreOrder(node.left)
            self.visitPreOrder(node.right)

    def visitPostOrder(self, node):
        if node:
            self.visitPostOrder(node.left)
            self.visitPostOrder(node.right)
            print(node.data)

    def search(self, root, value):
        if root:
            if root.data == value:
                return root
            elif value > root.data:
                return self.search(root.right, value)
            elif value < root.data:
                return self.search(root.left, value)

    def delete(self, root, value):
        if root:
            print(root.data)
            if value > root.data:
                root.right = self.delete(root.right, value)
            elif value < root.data:
                root.left = self.delete(root.left, value)
            else:  # value found
                print(f'found:{root.data}')
                # case1 - leaf node or 1 child
                if not root.right:
                    print(f'right empty, left:{root.left}')
                    return root.left  # left node or none
                elif not root.left:
                    # right node or None
                    print(f'left empty, right:{root.right}')
                    return root.right  # right node or none
                # case 2 - 2 children
                else:
                    # find max in left side (or min in right side)
                    temp = root.left
                    print(f'find max of left side: {temp.data}')
                    #                    print(temp.right.data)
                    while (temp.right):
                        temp = temp.right
                    #                        print(temp.data)
                    root.data = temp.data
                    self.delete(root.left, temp.data)
            #                    return root
            return root

    def visitInOrderIterative(self, root):
        s, res = [], []
        curr = root
        while s or curr:
            if curr:
                s.append(curr)
                curr = curr.left
            else:
                curr = s.pop()
                res.append(curr.data)
                #                print(curr.data)
                curr = curr.right
        return res

    def visitPreOrderIterative(self, root):
        s, res = [], []
        curr = root
        while s or curr:
            if curr:
                res.append(curr.data)
                s.append(curr)
                curr = curr.left
            else:
                curr = s.pop()
                curr = curr.right
        return res


#    def visitPostOrderIterative(self,root):


root = TNode(9)
b = BST(root)
b.insert(root, 3)
b.insert(root, 5)
b.insert(root, 15)
b.insert(root, 2)
b.insert(root, 7)
b.insert(root, 4)


class BstTest(unittest.TestCase):
    def test_inOrderIter(self):
        self.assertEqual(b.visitInOrderIterative(root), [2, 3, 4, 5, 7, 9, 15])

    def test_preOrderIter(self):
        self.assertEqual(b.visitPreOrderIterative(root), [9, 3, 2, 5, 4, 7, 15])


# unittest.main()
# print(b.visitPostOrderIterative(root))

######################### MERGE SORT
def mergeSortSlice(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        # array slicing is expensive, but it will be used for the sake of simplicity
        left = arr[:mid]
        right = arr[mid:]
        mergeSortSlice(left)
        mergeSortSlice(right)

        i = j = k = 0
        # replace array values in order
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # copy remaining values, if any
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def mergeSort(arr, l, r):
    if l < r:
        mid = (r + l) // 2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, r)

        left = []
        right = []
        for i in range(l, mid + 1):
            left.append(arr[i])
        for j in range(mid + 1, r + 1):
            right.append(arr[j])

        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# l=[12,11,13,5,6,7,15,1,100]
# print(l)
# res=mergeSort2(l,0,len(l)-1)
# print(res)

######################### QUICK SORT
def partition(arr, l, r):
    pivot = arr[(r + l) // 2]
    while l <= r:
        # find element that should be on the right
        while arr[l] < pivot:
            l += 1
        # find element that should be on the left
        while arr[r] > pivot:
            r -= 1
        # swap elements
        if l <= r:
            temp = arr[l]
            arr[l] = arr[r]
            arr[r] = temp
            l += 1
            r -= 1
    return l


def quickSort(arr, l, r):
    i = partition(arr, l, r)
    if l < i - 1:  # sort left side
        quickSort(arr, l, i - 1)
    if i < r:  # sort right side
        quickSort(arr, i, r)


# l=[12,11,13,5,6,7,15,1,100]
# print(l)
# quickSort(l,0,len(l)-1)
# print(l)

######################### TREE IMPLEMENTATION?


######################### GRAPH IMPLEMENTATION?


######################### INT TO BINARY
def int2bin(intval):
    l = []
    temp = intval
    while temp >= 1:
        l.append(temp % 2)
        temp = temp // 2
    bin = ''
    while l:
        bin += str(l.pop())
    return bin


######################### INT TO BINARY (Recursive)
def int2binRec(intval):
    if intval == 0:
        return 0
    else:
        return (intval % 2 + 10 * int2binRec(intval // 2))


######################### BIT TASKS
def getBit(num, i):
    return (num & (1 << i)) != 0


def setBit(num, i):
    return num | (1 << i)


def clearBit(num, i):
    mask = ~(1 << i)
    return num & mask


def toggleBit(num, i):
    n = (num & (1 << i)) == 0
    mask = ~(1 << i)
    return (num & mask) | (n << i)


###############
# Reverse a linked list (single)
def reverseList(head):
    node, prev = head, None
    while node:
        node.next, prev, node = prev, node, node.next
    return prev


#
# head=Node(5)
# head.next=Node(7)
# head.next.next=Node(9)
# head.next.next.next=Node(11)
# head.next.next.next.next=Node(53)
# ll=LinkedList()
# ll.head=head
# print(repr(ll))
# rev=reverseList(head)
# ll.head=rev
# print(repr(ll))

################ heapq library
import heapq

h = []
heapq.heappush(h, 5)
heapq.heappush(h, 3)
heapq.heappush(h, 6)
heapq.heappush(h, 1)
heapq.heappush(h, 10)
heapq.heappush(h, 8)
print(h)

# print(heapq.heappop(h))
print(heapq.nlargest(3, h))
print(heapq.nsmallest(3, h))


class TestHeap(unittest.TestCase):
    def test_nlargest(self):
        self.assertEqual(heapq.nlargest(3, h), [10, 8, 6])

    def test_nsmallest(self):
        self.assertEqual(heapq.nsmallest(3, h), [1, 3, 5])


# unittest.main()

###################### rolling hash

def hash(string):
    hk = 0
    mod = 100001
    base = 71
    for i, c in enumerate(string[::-1]):
        hk += (ord(c) * base ** i)
    return hk % mod


# calcs hash by adding new char to back and popping front char
def hashpoppush(hk, string, char):
    mod = 100001
    base = 71
    hk -= (ord(string[0]) * base ** (len(string) - 1))
    hk *= base
    hk += ord(char)
    return hk % mod


testword = 'pneumonoultramicroscopicsilicovolcanoconiosis'
nextchars = ['1', 'b', '3', 'c', '4', 'd', '5']
for c in nextchars:
    key = hash(testword)
    key2 = hash(testword[1:] + c)
    rolledhk = hashpoppush(key, testword, c)
    print(key2, rolledhk, key2 == rolledhk)
    testword = testword[1:]


##################### trie

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isEndOfWord = True

    def search(self, word):
        node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        return node.isEndOfWord

    def delete(self, word):
        node = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        node.isEndOfWord = False
        return True

# print("Trie")
# t = Trie()
# words = ['camp', 'camper', 'cat', 'cater']
# print('Inserting words: ', words)
# for word in words:
#     t.insert(word)
# for word in words:
#     print(word, 'is in trie?', t.search(word))
# deletewords = ['car', 'camper']
# print('Delete words: ', deletewords)
# for word in deletewords:
#     print(word, 'deleted?', t.delete(word))
# for word in words:
#     print(word, 'is in trie?', t.search(word))
