#Examples of arm strong number 371, 1634

import math
def isArmstrong(n):
    original = n
    sum=0
    len = int(math.log10(n)+1)
    while n>0:
        remainder = n%10
        n=n//10
        sum = sum + remainder**len
    return sum == original

usr_input = int(input("Enter a Number: "))
print(isArmstrong(usr_input))