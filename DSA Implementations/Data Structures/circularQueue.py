#QUEUE TYPE 2 : CIRCULAR QUEUE

class circularQueue:
    def __init__(self,size):
        self.f = self.r = -1
        self.qSize = size 
        self.a = [None] * size
    
    def isEmpty(self):
        if self.f == -1 and self.r == -1:
            return True
        else:
            return False
            
    def isFull(self):
        if ((self.r + 1) % self.qSize == self.f):
            return True
        else:
            return False

    def peek(self):
        print("\nELEMENT AT THE FRONT "+str(self.f)+" IS: "+str(self.a[self.f]))
    
    def enQueue(self,data):
        if not self.isFull():
            if self.isEmpty():
                print("\nQUEUE IS EMPTY")
                self.f = 0
            if self.r + 1 == self.qSize:
                self.r = (self.r + 1) % self.qSize
            else:
                self.r += 1
            self.a[self.r] = data
        else:
            print("\nQUEUE IS FULL")
    
    def deQueue(self):
        if self.isEmpty():
            print("\nQUEUE IS EMPTY")
        self.f = (self.f + 1) % self.qSize
    
    def printQueue(self):
        print("\nCIRCULAR QUEUE")
        if not self.isEmpty():
            for i in range(self.f,self.r+1):
                print(i,end="--")
            print()
            if self.r >= self.f:
                for i in range(self.f,self.r+1):
                    print(self.a[i],end=" ")
            else:
                for j in range(self.f,self.qSize):
                    print(self.a[j],end=" ")
                for k in range(0,self.r+1):
                    print(self.a[k],end=" ")
        else:
            print(" - ")
        print("\n...............................")

q = circularQueue(4)
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
print("--q.enQueue(32)")
q.enQueue(32)
print("--q.enQueue(64)")
q.enQueue(64)
print("--q.printQueue()")
q.printQueue()
print("--q.peek()")
q.peek()
