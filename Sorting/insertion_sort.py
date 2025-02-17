

def insertion_sort(arr):
    for index in range(1,len(arr)):
        current_element = arr[index]
        pos = index
        while pos > 0 and current_element < arr[pos-1]:
            arr[pos]  = arr[pos-1]
            pos -= 1
        arr[pos] = current_element


arr = [2,44,1,551,11]


insertion_sort(arr)
print(arr)
