def twoSum(nums, target):
    x = [0,0]
    for i in range(len(nums)):
        print("LIST VALUE: ",i," : ",nums[i])
    for i in range(len(nums)):
        print("LIST--> ",nums)
        a = nums[i]
        b = target - a
        print("SUM VALUE: ",a," + ",b)
        #new = nums[i+1:]
        #print("new LIST--> ",new)
        if ( b in nums[i+1:]):
            x[0]=i
            if a == b :
                x[1]=nums.index(b,i+1)
            else:
                x[1]=nums.index(b)
            break
    return x
    
nums = [2,7,11,15]
target = 9
#Output: [0,1]
#nums = [3,2,4]
#target = 6
#Output: [1,2]
#nums = [3,3]
#target = 6
#Output: [0,1]
x = twoSum(nums,target)
print("OUTPUT: ",x)