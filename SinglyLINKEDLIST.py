class Node:
    def __init__(self, data=None, next=None):
        self.data = data
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
        return ' -> '.join(nodes)
    
    def insertAtBEGIN(self, data):  # INSERT AT BEGIN OF LINKED LIST
        self.head = Node(data, self.head)
        
    def insertAtEND(self, data):    # INSERT AT END OF LINKED LIST      
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)
        else:
             self.head = Node(data) 
             
    def insertAtPOSITION(self, data, position):    # INSERT AT A POSITION OF LINKED LIST      
        if self.head:
            if position == 1:
                self.head = Node(data, self.head)
            else:
                curr = self.head
                counter = 2
                while curr.next:
                    if counter == position:
                        curr.next = Node(data, curr.next)
                    counter +=  1               
                    curr = curr.next            
        else:
             self.head = Node(data)
             
    def deleteAtBEGIN(self):  # DELETE AT BEGIN OF LINKED LIST
        if self.head:
            curr = self.head
            self.head = curr.next
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
        
N = int(input("Enter LIST SIZE: ")) # 10
L = [int(item) for item in input("Enter LIST ITEMS : ").split()] # 10 9 8 7 6 5 4 3 2 1
LL = LinkedList()
for i in range(N):
    if L[i] % 2 == 0 :
        LL.insertAtBEGIN(L[i])
    else:
        LL.insertAtEND(L[i])
print("\n PRINT LINKED LIST:                  ",LL)   # PRINT LINKED LIST
LL.insertAtPOSITION(25,5)
print("\n insertAtPOSITION(25,5) LINKED LIST: ",LL)
LL.deleteAtBEGIN()
print("\n deleteAtBEGIN() LINKED LIST:        ",LL)
LL.deleteAtEND()
print("\n deleteAtEND() LINKED LIST:          ",LL) 
LL.deleteAtPOSITION(7)
print("\n deleteAtPOSITION(7) LINKED LIST:    ",LL)  
LL.deleteValue(6)
print("\n deleteValue(6) LINKED LIST:         ",LL)  
print("\n searchValue(4) LINKED LIST:         ",LL,"\n") 
LL.searchValue(4)
LL.reverseLinkedList()
print("\n reverseLinkedList() LINKED LIST:    ",LL)
LL.deleteLinkedList()
print("\n deleteLinkedList() LINKED LIST:     ",LL)

#   OUTPUT
'''
Enter LIST SIZE: 10

Enter LIST ITEMS : 10 9 8 7 6 5 4 3 2 1

 PRINT LINKED LIST:                   2 -> 4 -> 6 -> 8 -> 10 -> 9 -> 7 -> 5 -> 3 -> 1

 insertAtPOSITION(25,5) LINKED LIST:  2 -> 4 -> 6 -> 8 -> 25 -> 10 -> 9 -> 7 -> 5 -> 3 -> 1

 deleteAtBEGIN() LINKED LIST:         4 -> 6 -> 8 -> 25 -> 10 -> 9 -> 7 -> 5 -> 3 -> 1

 deleteAtEND() LINKED LIST:           4 -> 6 -> 8 -> 25 -> 10 -> 9 -> 7 -> 5 -> 3

 deleteAtPOSITION(7) LINKED LIST:     4 -> 6 -> 8 -> 25 -> 10 -> 9 -> 5 -> 3

 deleteValue(6) LINKED LIST:          4 -> 8 -> 25 -> 10 -> 9 -> 5 -> 3

 searchValue(4) LINKED LIST:          4 -> 8 -> 25 -> 10 -> 9 -> 5 -> 3 

4  FOUND AT POSITION  1

 reverseLinkedList() LINKED LIST:     3 -> 5 -> 9 -> 10 -> 25 -> 8 -> 4

 deleteLinkedList() LINKED LIST: 
'''