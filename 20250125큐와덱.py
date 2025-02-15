
MAX_QSIZE=10

class CircularQueue:
    def __init__(self):
        self.front=0
        self.rear=0
        self.items=[None]*MAX_QSIZE

    def isEmpty(self):return self.front==self.rear
    def isFull(self):return self.front==(self.rear+1)%MAX_QSIZE
    def clear(self):self.front=self.rear
    def enqueue(self,item):
        if self.isFull()==False:
            self.rear+=1
            self.rear%=MAX_QSIZE
            self.items[self.rear]=item
    def dequeue(self):
        if self.isEmpty()==False:
            self.front=(self.front+1)%MAX_QSIZE
            return self.items[self.front]
    def peek(self):
        if self.isEmpty()==False:
            return self.items[(self.front+1)%MAX_QSIZE]
    def size(self):
        return (self.rear-self.front+MAX_QSIZE)%MAX_QSIZE
    def display(self):
        out=[]
        if self.front<self.rear:
            out=self.items[self.front+1:self.rear+1]
        else:
            out=self.items[self.front+1:]+self.items[:self.rear+1]
        print("[f=%s, r=%d] ==>"%(self.front,self.rear),out)
'''
q=CircularQueue()
for i in range(8):
    q.enqueue(i)
    q.display()
for i in range(5):
    q.dequeue()
    q.display()
for i in range(8,14):
    q.enqueue(i)
    q.display()
'''
class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()

    def addRear(self,item):self.enqueue(item)
    def deleteFront(self):return self.dequeue()
    def getFront(self):return self.peek()
    def addFront(self,item):
        self.items[self.front]=item
        self.front=(self.front-1+MAX_QSIZE)%MAX_QSIZE
    def deleteRear(self):
        item=self.items[self.rear]
        self.rear=(self.rear-1+MAX_QSIZE)%MAX_QSIZE
        return item
    def getRear(self):
        return self.items[self.rear]

dq=CircularDeque()
for i in range(9):
    if i%2==0:dq.addRear(i)
    else:dq.addFront(i)
    dq.display()
for i in range(2):
    dq.deleteFront()
    dq.display()
for i in range(3):
    dq.deleteRear()
    dq.display()
for i in range(9,14):
    dq.addFront(i)
    dq.display()

