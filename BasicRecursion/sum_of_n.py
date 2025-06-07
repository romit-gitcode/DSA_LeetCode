# Sum of n numbers using recursion

def sum_of_n(i, n, sum):
    if i>n:
        print(sum)
        return
    
    sum=sum+i
    i+=1
    sum_of_n(i, n, sum)
    
# The above funtion works but if you want to return a value in the recusrive call then only in the last stack it will return if you dont do it ans will be none
def return_sum_of_n(i, n, sum):
    if i>n:
        return sum
    
    sum=sum+i
    i+=1
    return return_sum_of_n(i, n, sum)

# More better approch
def better_sum(n, sum):
    if n<1:
        return sum
    
    return better_sum(n-1, sum+n)
    
# sum_of_n(1, 5, 0)
# result = return_sum_of_n(1, 5, 0)
result = better_sum(5, 0)
print("Result: ",result)
