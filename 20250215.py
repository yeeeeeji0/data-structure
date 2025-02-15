'''
class Node:
    def __init__(self,elem,link=None):
        self.data=elem
        self.link=link

class LinkedStack:
    def __init__(self):
        self.top=None

    def isEmpty(self):return self.top ==None
    def clear(self):self.top=None
    def push(self,item):
        n=Node(item,self.top)
        self.top=n
    def pop(self):
        if not self.isEmpty():
            n=self.top
            self.top=n.link
            return n.data
    def size(self):
        count=0
        node=self.top
        while not node==None:
            node=node.link
            count+=1
        return count

    def display(self):
        node=self.top
        while not node==None:
            print(node.data,end=' ')
            node=node.link

s=LinkedStack()
s.push(1)
s.push(2)
s.pop()
s.push(2)
s.push(3)
print(s.size())
s.display()

class LinkedList:
    def __init__(self):
        self.head=None

    def isEmpty(self):return self.head==None
    def clear(self):self.head=None
    def size(self):
        count=0
        node=self.head
        while not node==None:
            node=node.link
            count+=1
        return count
    def display(self):
        node=self.head
        while not node==None:
            print(node.data,end=' ')
            node=node.link
        print()
            
    def getNode(self,pos):
        if pos<0:return None
        node=self.head
        while node!=None and pos>0:
            node=node.link
            pos-=1
        return node
    
    def getEntry(self,pos):
        node=self.getNode(pos)
        if node==None:return None
        else:return node.data
        
    def insert(self,pos,elem):
        before=self.getNode(pos-1)
        if before==None:
            self.head=Node(elem,self.head)
        else:
            before.link=Node(elem,before.link)
    def delete(self,pos):
        before=self.getNode(pos-1)
        if before==None:
            if not self.isEmpty():
                self.head=self.head.link
        elif before.link!=None:
            before.link=before.link.link

    def replace(self,pos,elem):
        node=self.getNode(pos)
        if node!=None:
            node.data=elem
        
s=LinkedList()
s.display()
s.insert(0,10)
s.insert(0,20)
s.insert(1,30)
s.insert(s.size(),40)
s.insert(2,50)
s.display()
s.replace(2,90)
s.display()
s.delete(2)
s.delete(s.size()-1)
s.delete(0)
s.display()
s.clear()
s.display()
'''
n=int(input())
s=[]
re=[]
start=0
for i in range(n):
    a=int(input())
    if start==0:
        for i in range(1,a+1):
            s.append(i)
            re.append('+')
        start=a
    
    else:
        if a<start:
            for i in range(len(s)):
                p=s.pop()
                re.append('-')
                if p==a:
                    break
                
        elif a==start:
            s.pop()
            re.append('-')
        else:
            for i in range(start+1,a+1):
                s.append(i)
                re.append('+')
            start=a
            s.pop()
            re.append('-')
