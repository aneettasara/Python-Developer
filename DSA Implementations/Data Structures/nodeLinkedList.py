class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
def countNodes(head):
    print("Count of Nodes: ")
    c = 0
    curr =  head
    while (curr!=None):
        c += 1
        curr = curr.next      
    return c

print("LINKED LISTS INTRO")
n1 = Node(6)
n2 = Node(4)
n3 = Node(3)
n4 = Node(2)
n5 = Node(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print(countNodes(n1))
