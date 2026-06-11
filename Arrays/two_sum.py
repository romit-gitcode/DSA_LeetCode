nums = [3, 6, 5, 4]
[3,4,5,6]
target = 8
# nums = [4,5,6]
# target = 10
# nums = [5,5]
# target = 10

# Solution1: Brute Force
def twoSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
# Solution2: Sorted Two pointer
def twoSum2(nums, target):
    # print("sorted",sorted(nums))
    original= []
    for i, num in enumerate(nums, 0):
        original.append([num, i])
    print("orignal: ",original)
    original.sort()
    print("sorted: ",original)
    
    j=len(original)-1
    k=0
    for i in range(len(original)):
        print("range(len(original)): ", range(len(original)), i)
        if(original[k][0]+ original[j][0] == target):
            return [original[k][1], original[j][1]]
        elif original[i][0]+ original[j][0] < target:
            k+=1
        else:
            j-=1
    return []
                
print(twoSum2(nums, target))
