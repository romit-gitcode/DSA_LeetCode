#Duplicate Integer
# Solved 
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true
# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false

def hasDuplicate(nums):
    ele_dict = {}
    for ele in nums:
        if ele in ele_dict:
            return True
        else:
            ele_dict[ele] = 1
    return False

nums = [1,2,3,3]
print(hasDuplicate(nums))            
  
         