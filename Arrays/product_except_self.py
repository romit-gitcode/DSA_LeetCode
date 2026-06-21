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
    print("answer1: ", answer)

    postfix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= postfix
        postfix *= nums[i]

    return answer

# Brute force
def productExceptSelf2(nums):
    n=len(nums)
    products = [1]*n
    # print(products)
    for i in range(n):
        for j in range(n):
            if( i != j):
                products[i] *= nums[j]
            continue
    return products

# Using div operator -> O(n)
def productExceptSelf3(nums):
    product = 1
    for i in nums:
        product = product*i
    
    res = [product]*len(nums)
    for index, i in enumerate(nums):
        res[index] = int(res[index]/i)
    return res
    
# Without using div operator
def producExceptSelf4(nums):
    n = len(nums)
    res = [0] * n
    pref = [0] * n
    suff = [0] * n

    pref[0] = suff[n - 1] = 1
    for i in range(1, n):
        pref[i] = nums[i - 1] * pref[i - 1]
    for i in range(n - 2, -1, -1):
        suff[i] = nums[i + 1] * suff[i + 1]
    for i in range(n):
        res[i] = pref[i] * suff[i]
    return res

# nums = [1,2,3,4]
nums = [1,2,3,4]
print(productExceptSelf3(nums))       
