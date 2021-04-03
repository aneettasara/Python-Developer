def factorial(n):
    if n >= 1:
        return n * factorial(n-1)
    else:
        return 1
    
def fibonacci(n):
    if n >= 3:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return 1

print("\n RECURSION")

print("\n Factorial of a number n! ...")
print("Factorial of 0: "+str(factorial(0)))
print("Factorial of 1: "+str(factorial(1)))
print("Factorial of 5: "+str(factorial(5)))

print("\n Fibonacci Sequence: 1 1 2 3 5 8 13 21 ...")
print("8th fibonacci number: "+str(fibonacci(8)))
print("1th fibonacci number: "+str(fibonacci(1)))
print("5th fibonacci number: "+str(fibonacci(5)))
