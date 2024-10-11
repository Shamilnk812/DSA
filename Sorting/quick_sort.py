

def find_pivot_place(arr, first, last) :
    pivot = arr[first]
    left = first+1
    right = last

    while True :
        while left <= right and arr[left] <= pivot :
            left += 1
        while left <= right and arr[right] >= pivot :
            right -= 1

        if right < left :
            break
        else :
            arr[left],arr[right] = arr[right],arr[left]

    arr[first],arr[right] = arr[right],arr[first]
    return right



def quick_sort(arr,first,last) :
    if first < last :
        p = find_pivot_place(arr,first,last)
        quick_sort(arr,first,p-1)
        quick_sort(arr,p+1,last)


arr = [45,25,88,11]
quick_sort(arr,0,len(arr)-1)
print(arr)