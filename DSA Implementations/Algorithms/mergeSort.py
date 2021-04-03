# MergeSort

def mergeSort(array):
    
    if len(array) > 1:
        
        r = len(array)//2
        L = array[:r]
        M = array[r:]
        
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0
        
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1


array = [6, 5, 12, -10, 9, 1]       # Output: [-10, 1, 5, 6, 9, 12]
print("INPUT")
print(array)
mergeSort(array)
print("OUTPUT")
print(array)
