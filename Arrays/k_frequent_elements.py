# Return elements whose frequency is at least k.

def topKFrequent(nums, k):
    hashMap = {}
    for n in nums:
        if n not in hashMap:
            hashMap[n] = 1
        else:
            hashMap[n] +=1
    
    res = []
    for key, cnt in hashMap.items():
        res.append([cnt, key])
    res.sort()
    
    ans = []
    for i in range(len(res) - k, len(res)):
        ans.append(res[i][1])
    return ans


nums=[1,2,2,3,3,3,4,4, 5, 5, 5]
k=2
print(topKFrequent(nums,k))