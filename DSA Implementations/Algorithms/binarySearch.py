# BINARY SEARCH
import array as arr

def binary_search(a,target):
    left_pointer = 0
    right_pointer = len(a) - 1
    while left_pointer <= right_pointer:
        mid_pointer = int((left_pointer + right_pointer) / 2)
        if a[mid_pointer] == target:
            return mid_pointer
        elif target < a[mid_pointer]:
            right_pointer = mid_pointer - 1
        else:
            left_pointer = mid_pointer + 1
    return -1

a = arr.array('i',[2,3,4,7,8,9,11,13])
target = 8

print("Array")
for i in range(len(a)):
    print(a[i],end="--")
print("\nPositions")
for i in range(len(a)):
    print(i,end="--")
print("\n")

index_of_target = binary_search(a,target)
if index_of_target > -1:
    print(str(target)+" found at position: "+str(index_of_target))
else:
    print(str(target)+" not found!!")
    
