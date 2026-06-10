nums = [3,4,5,6]
target = 7
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
                
print(twoSum(nums, target))
