

def bubble_sort(arr) :
    for i in range(len(arr)-1) :
        found = False
        for j in range(len(arr)-i-1) :
            if arr[j] > arr[j+1] :
                arr[j],arr[j+1] = arr[j+1],arr[j]
                found = True

        if not found :
            break


arr = [52,78,2,45,6]
print('before : ',arr)
bubble_sort(arr)     
print('after ',arr)   