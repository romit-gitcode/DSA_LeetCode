# Product of Array Except Self

# Given an integer array nums, return an array answer such that:

# answer[i] = product of all elements in nums except nums[i]

# You must solve it without using division and in O(n) time.

def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= postfix
        postfix *= nums[i]

    return answer

nums = [1,2,3,4]
print(productExceptSelf(nums))       
