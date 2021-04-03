#STACKS

class Stack:
    def __init__(self,size):
        self.top = -1
        self.stackSize = size 
        self.s = [0] * size
    
    def isEmpty(self):
        if self.top == -1:
            print("\nSTACK IS EMPTY")
        else:
            print("\nSTACK IS NOT EMPTY")
            
    def isFull(self):
        if self.top == self.stackSize-1:
            print("\nSTACK IS FULL")
        else:
            print("\nSTACK IS NOT FULL")

    def peek(self):
        print("\nELEMENT AT THE TOP "+str(self.top)+" IS: "+str(self.s[self.top]))
    
    def pushElement(self,data):
        self.top += 1
        self.s[self.top] = data
    
    def popElement(self):
        self.top -= 1
    
    def printStack(self):
        print("\nSTACK")
        if self.top != -1:
            for i in range(0,self.top+1):
                print(self.s[i],end=" ")
        else:
            print(" - ")
        print("\n...............................")

s = Stack(5)
s.isEmpty()
s.printStack()
s.pushElement(5)
s.printStack()
s.pushElement(10)
s.printStack()
s.pushElement(20)
s.printStack()
s.isFull()
s.printStack()
s.pushElement(40)
s.printStack()
s.isEmpty()
s.printStack()
s.popElement()
s.printStack()
s.pushElement(8)
s.printStack()
s.pushElement(16)
s.printStack()
s.isFull()
s.printStack()
s.peek()
s.printStack()
