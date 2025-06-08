# LeetCode 125. Valid Palindrom
# Q) A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Input: s = "A man, a plan, a canal: Panama" -> valid
# Input: s = "race a car" -> not valid
# Input: s = " " -> valid

def leet_palindrom(s):
    cleaned = "".join(char.lower() for char in s if char.isalnum()) 
    start = 0
    end = len(cleaned)-1
    flag = True
    
    for i in range(0, len(cleaned)//2):
        if cleaned[start]==cleaned[end]:
            start+=1
            end-=1
        else: 
            flag = False
    return flag


# Iterative method
def iter_palindrom(str):
    start = 0
    end = len(str)-1
    flag = True
    
    for i in range(0, len(str)//2):
        if str[start] == str[end]:
            start+=1
            end-=1
            flag = True
        else:
            flag = False
    return flag
        
#Recursive Method
def recur_palindrom(str, start, end):
    if start>end:
        return True
    if str[start]!=str[end]:
        return False
    
    if str[start]==str[end]:
        return recur_palindrom(str, start+1, end-1)
        
if __name__ == "__main__":
    # s = "madsdadm"
    s = "A man, a plan, a canal: Panama"
    # result = iter_palindrom(s)
    # result = recur_palindrom(s, 0, len(s)-1)
    result = leet_palindrom(s)
    print("Is Palindrom: ", result)