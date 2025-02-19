
def heapify(arr,n,i):
    largest = i
    left = 2 * i + 1     # find left child
    right = 2 * i + 2    # find right child
    if left < n and arr[left] > arr[largest] :
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if i != largest:
        arr[i],arr[largest] = arr[largest],arr[i]   # swap 
        heapify(arr,n,largest)


def build_max_heap(arr):
    n = len(arr)
    starting_index = (n-1) // 2  # starting node 
    for i in range(starting_index,-1,-1):
        heapify(arr,n,i)




arr = [22,33,55,155,90,3]
build_max_heap(arr)
print(arr)

