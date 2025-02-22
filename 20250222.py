class Node:
    def __init__(self,elem,link=None):
        self.data=elem
        self.link=link

class LinkedList:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False
        
    def clear(self):
        self.head=None

    def size(self):
        num=0
        head=self.head
        while head!=None:
            num+=1
            head=head.link
        return num

    def getNode(self,pos):
        if pos<0:
            return None
        else:
            node=self.head
            while pos>0 and node!=None:
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
            node=Node(elem,before.link)
            before.link=node
    def delete(self,pos):
        before=self.getNode(pos-1)
        if before==None:
            if self.head is not Node:
                self.head=self.head.link
        elif before.link!=None:
            before.link=before.link.link

    def display(self):
        node=self.head
        while node!=None:
            print(node.data,end=' ')
            node=node.link
        print(None)

    def replace(self,pos,elem):
        node=self.getNode(pos)
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


        
