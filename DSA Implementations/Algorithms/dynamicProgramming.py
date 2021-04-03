import array as arr

#   Recursion
def fibonacci(n):
    if n >= 3:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return 1
    
#   Memoize
def fib(n, memo):
    if memo[n] != 0:
        return memo[n]
    if n >= 3:
        result = fib(n-1,memo) + fib(n-2,memo)
    else:
        result = 1
    memo[n] = result
    return result        

#   Bottom Up
def fib_bottom_up(n):
    size_of_bottom_up = n + 1
    b = arr.array('d', [0] * size_of_bottom_up)
    b[1] = 1
    b[2] = 1
    for i in range(3,n+1):
        b[i] = b[i-1] + b[i-2]
    return b[n]
        
    
print("Fibonacci Sequence: 1 1 2 3 5 8 13 21 ...")
number = int(input("Enter the position to find the fibonacci number at that position: "))

print("\n Recursion")
print(str(number)+"th fibonacci number: "+str(fibonacci(number)))

print("\n Memoized Solution")
size_of_memo = number + 1
memo = arr.array('d', [0] * size_of_memo)
print(str(number)+"th fibonacci number: "+str(fib(number, memo)))

print("\n Bottom Up Approach")
print(str(number)+"th fibonacci number: "+str(fib_bottom_up(number)))
