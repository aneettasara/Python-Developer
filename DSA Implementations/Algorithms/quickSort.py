# QUICK SORT
import array as arr

def partition(a, l, r):
    pivot = a[r]
    i = l - 1
    for j in range(l,r):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[r] = a[r], a[i+1]
    return i+1    

def quickSortRec(a, l, r):
    if l >= r:
        return
    p = partition(a, l, r)
    quickSortRec(a, l, p-1)
    quickSortRec(a, p+1, r)
    
def quickSort(a):
    quickSortRec(a, 0, len(a) - 1)

def printArray(a):
    for i in range(len(a)):
        print(a[i],end="  ")

a = arr.array('i',[3,-2,-1,0,2,4,1])      # Output:  -2  -1  0  1  2  3  4  
#a = arr.array('i',[3, 1, -1, 0, 2, 5])      # Output: -1  0  1  2  3  5  
        
print("\nInput Array : ")
printArray(a)

quickSort(a)
print("\nOutput Array : ")
printArray(a)
