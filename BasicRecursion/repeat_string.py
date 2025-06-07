#Write a code using recursion to print a string n times

def string_rec(i, n, str):
    if i>n:
        return
    print(i, ":", str)
    i+=1
    string_rec(i,n, str)
    
# Print 1-n using recursion
def number_recursion(i, n):
    if i>n:
        return
    print(i)
    i+=1
    number_recursion(i, n)
    
# Print n-1 using recursion
def reverse_recursion(i, n):
    if n<i:
        return
    print(n)
    n-=1
    reverse_recursion(i,n)
        
    
# string_rec(1, 3, "Romit")
# number_recursion(1, 5)
reverse_recursion(1,5)