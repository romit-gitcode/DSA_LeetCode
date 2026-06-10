# two strings are anagram if both the string has exactly same characters but are in differnt order

s1 = "python"
s2 = "tonhpy"
# Solution 1: Sorting
def isAnagram1(s1, s2):
    sorted(s1) == sorted(s2)

# Solution 2:  Using HashMap
def isAnagram2(s1, s2):
    if (len(s1) != len(s2)):
        return False
    
    countS1, countS2 = {}, {}
    for i in range(len(s1)):
        countS1[s1[i]] = 1 + countS1.get(s1[i], 0)
        countS2[s2[i]] = 1 + countS2.get(s2[i], 0)
    # print("Count1: ", countS1)
    # print("Count2: ", countS2)
    return countS1 == countS2

print(isAnagram2(s1,s2))
