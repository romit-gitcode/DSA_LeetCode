
# Time complexity o(n)
def is_prime(n):
    cnt = 0
    for i in range(1,n+1):
        if(n%i==0):
            cnt+=1
    if(cnt != 2):
        return False
    return True

#time complexity in sqrt of n we just want to loop till sqrt(n) because we know that we can find all the factors just by looping till sqrt(n)
# Also instead of using math.sqrt(n) we will use this technique that also represents sqrt(n) i.e i*i<=n
def is_prime_2(n):
    cnt=0
    i =1 
    while i*i<=n:
        if(n%i==0):
            cnt+=1
            if(n//i != i):
                cnt+=1
        i+=1
    if(cnt != 2):
        return False
    return True

print(is_prime_2(int(input("ENTER A NUMBER: "))))
            