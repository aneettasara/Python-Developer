def recIpStack(ipStack,indexPop):
    index = len(ipStack) - 1
    if ipStack[index] == '(':   
        ipStack.pop(-1)
        ipStack += indexPop  
        return
    else:                     
        indexPop.append(ipStack.pop(index))
        recIpStack(ipStack,indexPop)
   
def reverseParentheses(ipStr):
    print("INPUT STRING: " +str(ipStr))
    ipStack = []
    for i in range(len(ipStr)):
        if ipStr[i] == ')':
            indexPop = []
            recIpStack(ipStack,indexPop)
        else:
            ipStack.append(ipStr[i])             
    return ''.join(map(str, ipStack))   
        
ip = "a(bcdefghijkl(mno)p)q"
#ip = "(u(love)i)" # "iloveu"
op = reverseParentheses(ip)
print("OUTPUT STRING: " +str(op))
