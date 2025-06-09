#Iterative method
def iter_fibbo(n):
    if(n<=0):
        return []
    if(n==1):
        return [0]
    fib = [0,1]
    for i in range(2, n):
        fib.append(fib[i-2]+fib[i-1])
    return fib

# Iterative to return only last
def last_fibbo(n):
    if(n<=1):
        return n
    a, b = 0, 1
    for _ in range(2, n):
        temp = b
        b = a + b
        a = temp
    return b
        

#Recursive method the fun below will only give you the last digit if we want to print the sequesnt we have to use for loop and is impracticall as it will make exponential recursive calls
# Time Complexity: O(2ⁿ) — exponential time complexity.
def recursive_fibbo(n):
    if(n<=0):
        return 0
    if(n==1):
         return 1
    return recursive_fibbo(n-2)+recursive_fibbo(n-1)
    

# result = iter_fibbo(7)
result = last_fibbo(7)
# result = recursive_fibbo(7)

print("Result: ", result)