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

result = iter_fibbo(7)
print("Result: ", result)