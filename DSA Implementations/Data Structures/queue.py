#QUEUES

class Queue:
    def __init__(self,size):
        self.front = self.rear = -1
        self.queueSize = size 
        self.s = [0] * size
    
    def isEmpty(self):
        if ( self.front == -1 and self.rear == -1 ) or self.front > self.rear:
            print("\nQUEUE IS EMPTY")
        else:
            print("\nQUEUE IS NOT EMPTY")
            
    def isFull(self):
        if self.rear == self.queueSize-1:
            print("\nQUEUE IS FULL")
        else:
            print("\nQUEUE IS NOT FULL")

    def peek(self):
        print("\nELEMENT AT THE FRONT "+str(self.front)+" IS: "+str(self.s[self.front]))
    
    def enQueue(self,data):
        if ( self.front == -1 and self.rear == -1 ) or self.front > self.rear:
            self.front += 1
        if self.rear != self.queueSize-1:
            self.rear += 1
            self.s[self.rear] = data
    
    def deQueue(self):
        self.front += 1
    
    def printQueue(self):
        print("\nQUEUE")
        if self.front != -1 and self.rear != -1:
            for i in range(self.front,self.rear+1):
                print(self.s[i],end=" ")
        else:
            print(" - ")
        print("\n...............................")

s = Queue(5)
s.isEmpty()
s.printQueue()
s.enQueue(5)
s.printQueue()
s.enQueue(10)
s.printQueue()
s.enQueue(20)
s.printQueue()
s.isFull()
s.printQueue()
s.enQueue(40)
s.printQueue()
s.isEmpty()
s.printQueue()
s.deQueue()
s.printQueue()
s.enQueue(8)
s.printQueue()
s.enQueue(16)
s.printQueue()
s.isFull()
s.printQueue()
s.peek()
s.printQueue()
