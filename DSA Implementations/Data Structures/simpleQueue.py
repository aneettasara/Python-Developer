#QUEUE TYPE 1 : SIMPLE QUEUE

class simpleQueue:
    def __init__(self,size):
        self.front = self.rear = -1
        self.queueSize = size 
        self.a = [None] * size
    
    def isEmpty(self):
        if ( self.front == -1 and self.rear == -1 ) or self.front > self.rear:
            return True
        else:
            return False
            
    def isFull(self):
        if self.rear == self.queueSize-1:
            return True
        else:
            return False

    def peek(self):
        print("\nELEMENT AT THE FRONT "+str(self.front)+" IS: "+str(self.a[self.front]))
    
    def enQueue(self,data):
        if self.isEmpty():
            print("\nQUEUE IS EMPTY")
            self.front += 1
        if not self.isFull():
            self.rear += 1
            self.a[self.rear] = data
        else:
            print("\nQUEUE IS FULL")
    
    def deQueue(self):
        if self.isEmpty():
            print("\nQUEUE IS EMPTY")
        self.front += 1
    
    def printQueue(self):
        print("\nQUEUE")
        if not self.isEmpty():
            for i in range(self.front,self.rear+1):
                print(i,end="--")
            print()
            for i in range(self.front,self.rear+1):
                print(self.a[i],end=" ")
        else:
            print(" - ")
        print("\n...............................")

q = simpleQueue(5)
print("--q.enQueue(5)")
q.enQueue(5)
print("--q.enQueue(10)")
q.enQueue(10)
print("--q.enQueue(20)")
q.enQueue(20)
print("--q.enQueue(40)")
q.enQueue(40)
print("--q.printQueue()")
q.printQueue()
print("--q.deQueue()")
q.deQueue()
print("--q.printQueue()")
q.printQueue()
print("--q.enQueue(8)")
q.enQueue(8)
print("--q.enQueue(16)")
q.enQueue(16)
print("--q.printQueue()")
q.printQueue()
print("--q.peek()")
q.peek()
