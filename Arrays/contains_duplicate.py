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
            print("hashMap",ele_dict)
            return True
        else:
            ele_dict[ele] = 1
    print("hashMap",ele_dict)
    return False

def hasDuplicate2(nums):
    set1 = set()
    for ele in nums:
        if ele in set1:
            print("set",set1)
            return True
        else:
            set1.add(ele)
    return False

def hasDuplicate3(nums):
   print("nums1",nums)
   set2 = set(nums)
   print("nums2",nums)
   print("len(set2)", len(set2))
   print("len(nums)",len(nums) )
   print("set", set2)
   return len(set2) != len(nums)

nums = [1,2,3,3]
print(hasDuplicate3(nums))            
      