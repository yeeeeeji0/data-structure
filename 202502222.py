'''
class Node:
    def __init__(self,elem,link=None):
        self.data=elem
        self.link=link

class CircularLinkedQueue:
    def __init__(self):
        self.tail=None
        
    def isEmpty(self):
        if self.tail==None:
            return True
        else:
            return False
        
    def clear(self):
        self.tail=None

    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data
        
    def enqueue(self,item):
        node=Node(item,link=None)
        if self.isEmpty():
            node.link=node
            self.tail=node
        else:
            node.link=self.tail.link
            self.tail.link=node
            self.tail=node

    def dequeue(self):
        if not self.isEmpty():
            data=self.tail.link.data
            if self.tail.link==self.tail:
                self.tail==None
            else:
                self.tail.link=self.tail.link.link
            return data

    def size(self):
        if self.isEmpty():return 0
        else:
            count=1
            n=self.tail.link
            while not n==self.tail:
                n=n.link
                count+=1
            return count

    def display(self):
        print(self.tail.link.data,end=' ')
        n=self.tail.link
        while not n==self.tail:
            n=n.link
            print(n.data,end=' ')
        print()

q=CircularLinkedQueue()
for i in range(8):
    q.enqueue(i)
q.display()
for i in range(5):
    q.dequeue()
q.display()
for i in range(8,14):
    q.enqueue(i)
q.display()

import sys
input=sys.stdin.readline
from collections import deque
q=deque()
n=int(input())
for i in range(n):
    s=input().split()
    if s[0]=='push_front':
        q.appendleft(s[1])
    elif s[0]=='push_back':
        q.append(s[1])
    elif s[0]=='pop_front':
        if len(q)==0:
            print(-1)
        else:
            print(q.popleft())
    elif s[0]=='pop_back':
        if len(q)==0:
            print(-1)
        else:
            print(q.pop())
    elif s[0]=='size':
        print(len(q))
    elif s[0]=='empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif s[0]=='front':
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif s[0]=='back':
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])
'''   
from collections import deque
q=deque()
n=int(input())
for i in range(1,n+1):
    q.append(i)
while len(q)>1:
    q.popleft()
    a=q.popleft()
    q.append(a)
print(q[0])
