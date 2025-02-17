

def binary_search_helper(arr,target,left,right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid + 1
    elif arr[mid] > target :
        return binary_search_helper(arr,target,left,mid-1)
    else:
        return binary_search_helper(arr,target,mid+1,right)
    

    
def binary_search(arr,target):
    return binary_search_helper(arr,target,0,len(arr)-1)


arr = [-3,4,5,6,7]
result = binary_search(arr,7)
print(result)