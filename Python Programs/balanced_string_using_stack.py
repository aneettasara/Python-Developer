# STACKS
# Balanced String Problem

#def printStack(ipStack):
#    print("Stack")
#    for ele in ipStack:
#        print(ele, end=' ')
#    print()

def isBalanced(ipStr):
    ipStack = []
    for i in range(len(ipStr)):
        #printStack(ipStack)
        if ipStr[i] == ')' or ipStr[i] == ']' or ipStr[i] == '}':
            ipStack.pop(-1)
        else:
            ipStack.append(ipStr[i]) 
    if ipStack == []:        
        return 1
    else:
        return -1

ip = "([])(){}(()()()"
op = isBalanced(ip)
if op == 1:
    print("INPUT: "+str(ip)+" is balanced")
else:
    print("INPUT: "+str(ip)+" is NOT balanced")
