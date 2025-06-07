
def factorial(n, initial):
    if n<1:
        return initial
    
    return factorial(n-1, initial*n)

def fact(n):
    if n==0 :
        return 1
    return n*fact(n-1)
    
# result = factorial(6, 1)
result = fact(6)
print("RESULT: ",result)
    
    