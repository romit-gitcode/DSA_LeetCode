nums = [3, 6, 5, 4]
target = 11
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

# Solution3: Sorted two pointers while loop
def twoSum3(nums, target):
    A = []
    for index, num in enumerate(nums, 0):
        A.append([num, index])
    # print(A)
              
    A.sort()
    i, j = 0, len(A)-1
    while i<j:
        if(A[i][0]+A[j][0] == target):
            return [A[i][1], A[j][1]]
        elif A[i][0] + A[j][0] > target:
            j-=1
        else:
            i+=1
    return []
    
    
print(twoSum3(nums, target))
