nums = [3, 6, 5, 4]
target = 11
# nums = [4,5,6]
# target = 10
# nums = [5,5]
# target = 10
# nums=[-1,-2,-3,-4,-5]
# target=-8
# nums=[2,5,5,11]
# target=10

# Solution1: Brute Force
def twoSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            
# Solution2: Sorted Two pointer
def twoSum2(nums, target):
    # print("sorted",sorted(nums))
    A = []
    for i, num in enumerate(nums, 0):
        A.append([num, i])
    print("orignal: ",A)
    A.sort()
    print("sorted: ",A)
    
    j=len(A)-1
    k=0
    for i in range(len(A)):
        print("range(len(A)): ", range(len(A)), i)
        if A[k][0]+ A[j][0] == target:
            return [A[k][1], A[j][1]]
        elif A[k][0]+ A[j][0] < target:
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
            return sorted([A[i][1], A[j][1]])
        elif A[i][0] + A[j][0] > target:
            j-=1
        else:
            i+=1
    return []

# Practice:
def twoSum4(nums, target):
    A=[]
    for index, num in enumerate(nums,0):
        A.append([num, index])
        
    A.sort()
    i,j = 0, len(nums)-1
    while i<j:
        if A[i][0] + A[j][0] == target:
            return sorted([A[i][1], A[j][1]])
        elif A[i][0] + A[j][0] < target:
            i += 1
        else:
            j -=1
    return []
            
       
print(twoSum4(nums, target))
