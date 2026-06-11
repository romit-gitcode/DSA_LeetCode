from collections import defaultdict
strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

# Solution 1: Brute Force Sorting + Hashmap using python default dict
def groupAnagrams(strs):
    res = defaultdict(list)
    for s in strs:
        str_key = "".join(sorted(s))
        res[str_key].append(s)
    return list(res.values())

# why I had to use default dict here why cant i just use {} directly
#Ans: You can absolutely use a standard dictionary {} directly! However, if you do, you have to write extra code to manually handle missing keys.If you try to append to a key that doesn't exist yet in a standard dictionary, Python throws a KeyError.
# See the code below:
# Solution 2: Brute FOrce without default dict
def groupAnagrams2(strs):
    res = {}
    for s in strs:
        str_key = "".join(sorted(s))
        if(str_key not in res):
            res[str_key] = []
        res[str_key].append(s)
    return list(res.values())


print(groupAnagrams2(strs))