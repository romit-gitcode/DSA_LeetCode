# Iterative 2 pointer method point one pointer at start and one at end, swap and increase start pointer and decrese end pointer, stop when star > end

def iterative_reverse_arr(arr, n):
    p1 = 0
    p2 = n-1
    while p1<p2:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1+=1
        p2-=1
    return arr

# Recursive method
def recursive_reverse_arr(arr, start, end):
    if start>end :
        return arr
    
    arr[start], arr[end] = arr[end], arr[start]
    return recursive_reverse_arr(arr, start+1, end-1)
    
    
arr1 = [5,4,3,2,1]
# print(iterative_reverse_arr(arr1, len(arr1)))
print(recursive_reverse_arr(arr1, 0, len(arr1)-1))
