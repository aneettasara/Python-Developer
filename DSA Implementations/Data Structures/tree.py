class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def find_sum(root_node):
    if root_node == None:
        return 0
    return root_node.data + find_sum(root_node.left) + find_sum(root_node.right)

def print2D(root, space):
    if root == None:
        return
    space += 5  
    print2D(root.right, space)    
    print()  
    for i in range(0, space): 
        print(end = " ")  
    print(root.data)  
    print2D(root.left, space)  
    
def print_tree(root_node):
    return print2D(root_node, 0)     

A = TreeNode(2)
B = TreeNode(3)
C = TreeNode(4)
D = TreeNode(5)
E = TreeNode(6)
A.left = B
A.right = C
B.left = D
B.right = E
print("TREE: ")
print(print_tree(A))
print("SUM OF ALL NODES IN TREE: ")
print(find_sum(A))
