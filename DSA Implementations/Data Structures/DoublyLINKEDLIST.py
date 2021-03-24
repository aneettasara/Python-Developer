class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
 
    def __repr__(self): # PRINT NODE IN LINKED LIST
        return repr(self.data)
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __repr__(self): # PRINT LINKED LIST
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return ' <-> '.join(nodes)
    
    def insertAtBEGIN(self, data):  # INSERT AT BEGIN OF LINKED LIST
        self.head = Node(data, None, self.head)
        
    def insertAtEND(self, data):    # INSERT AT END OF LINKED LIST      
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data, curr, None)
        else:
             self.head = Node(data) 
    
    def insertAtPOSITION(self, data, position):    # INSERT AT A POSITION OF LINKED LIST      
        if self.head:
            if position == 1:
                self.head = Node(data, None, self.head)
            else:
                curr = self.head
                counter = 2
                while curr.next:
                    if counter == position:
                        curr.next = Node(data, curr, curr.next)
                    counter +=  1               
                    curr = curr.next            
        else:
             self.head = Node(data)
             
    def deleteAtBEGIN(self):  # DELETE AT BEGIN OF LINKED LIST
        if self.head:
            curr = self.head
            if curr.next == None:
                self.head = None
            else:
                self.head = curr.next
                self.head.prev = None
        else:
             print(" EMPTY LINKED LIST")
             
    def deleteAtEND(self):  # DELETE AT END OF LINKED LIST
        if self.head:
            curr = self.head
            if curr.next == None:
                self.head = None
            else:
                while curr.next.next:
                    curr = curr.next
                curr.next = None    
        else:
             print(" EMPTY LINKED LIST") 
             
    def deleteAtPOSITION(self, position):  # DELETE FROM A POSITION OF LINKED LIST
        if self.head:
            if position == 1:
                curr = self.head
                self.head = curr.next
            else:
                curr = self.head
                counter = 2
                while curr.next:
                    if counter == position:
                        curr.next = curr.next.next
                    counter +=  1                
                    curr = curr.next    
        else:
             print(" DATA NOT FOUND AT ",position," / EMPTY LINKED LIST")
             
    def deleteValue(self, value):  # DELETE A VALUE FROM LINKED LIST
        if self.head:
            curr = self.head
            if curr.data == value:
                self.head = curr.next
            else:
                while curr.next:
                    if curr.next.data == value:
                        curr.next = curr.next.next
                    curr = curr.next            
        else:
             print(value," NOT FOUND / EMPTY LINKED LIST") 
    
    def deleteLinkedList(self): # DELETE LINKED LIST 
        self.__init__() 
        
    def searchValue(self, value): # SEARCH A VALUE IN LINKED LIST 
        position = 1
        if self.head:
            curr = self.head
            if curr.data == value:
                 print(value," FOUND AT POSITION ",position)
            else:
                while curr.next:
                    position += 1
                    if curr.next.data == value:
                        print(value," FOUND AT POSITION ",position)  
                    curr = curr.next
        else:
             print(value," NOT FOUND / EMPTY LINKED LIST")  
                      
    def reverseLinkedList(self): # REVERSE LINKED LIST 
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev 
            prev = curr 
            curr = next
        self.head = prev

#   MAIN PROGRAM
        
LL = LinkedList()
LL.insertAtBEGIN(3)
LL.insertAtBEGIN(2)
LL.insertAtBEGIN(1)
print("\n insertAtBEGIN() PRINT LINKED LIST:  ",LL)
LL.deleteValue(1)
print("\n deleteValue(1) LINKED LIST:         ",LL)  
LL.deleteLinkedList()
print("\n deleteLinkedList() LINKED LIST:     ",LL)
LL.insertAtEND(10)
LL.insertAtEND(20)
LL.insertAtEND(30)
print("\n insertAtEND() PRINT LINKED LIST:    ",LL)
LL.insertAtPOSITION(15,2)
print("\n insertAtPOSITION(15,2) LINKED LIST: ",LL)
LL.deleteAtBEGIN()
print("\n deleteAtBEGIN() LINKED LIST:        ",LL)
LL.deleteAtEND()
LL.deleteAtEND()
print("\n deleteAtEND() LINKED LIST:          ",LL) 
print("\n searchValue(15) LINKED LIST:         ",LL,"\n") 
LL.searchValue(15)
LL.deleteAtPOSITION(1)
print("\n deleteAtPOSITION(1) LINKED LIST:    ",LL)
print("\n searchValue(15) LINKED LIST:         ",LL,"\n") 
LL.searchValue(15)
LL.insertAtEND(5)
LL.insertAtEND(7)
LL.insertAtEND(9)
LL.insertAtEND(11)
print("\n insertAtEND() PRINT LINKED LIST:    ",LL)
LL.reverseLinkedList()
print("\n reverseLinkedList() LINKED LIST:    ",LL)

#   OUTPUT
'''
insertAtBEGIN() PRINT LINKED LIST:   1 <-> 2 <-> 3

 deleteValue(1) LINKED LIST:          2 <-> 3

 deleteLinkedList() LINKED LIST:      

 insertAtEND() PRINT LINKED LIST:     10 <-> 20 <-> 30

 insertAtPOSITION(15,2) LINKED LIST:  10 <-> 15 <-> 20 <-> 30

 deleteAtBEGIN() LINKED LIST:         15 <-> 20 <-> 30

 deleteAtEND() LINKED LIST:           15

 searchValue(15) LINKED LIST:          15 

15  FOUND AT POSITION  1

 deleteAtPOSITION(1) LINKED LIST:     

 searchValue(15) LINKED LIST:           

15  NOT FOUND / EMPTY LINKED LIST

 insertAtEND() PRINT LINKED LIST:     5 <-> 7 <-> 9 <-> 11

 reverseLinkedList() LINKED LIST:     11 <-> 9 <-> 7 <-> 5
'''
