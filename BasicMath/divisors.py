import math
# Time Complexity o(n)
def all_divisors(n):
    divisors = []
    for i in range(1,n+1):
        if(n%i==0):
            divisors.append(i)
    return divisors

# BETTER TIME COMPLEXITY
def divisors(n):
    divisors = []
    ori = n
    for i in range(1, int(math.sqrt(n))):
        if(n%i==0):
            divisors.append(i)
            if n//i != i:
                divisors.append(n//i)
    return sorted(divisors)
                
# print(all_divisors(int(input("Enter The Number: "))))
print(divisors(int(input("Enter The Number: "))))

