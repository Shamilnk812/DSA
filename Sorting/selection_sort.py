
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i  # Assume the first element is the minimum

        # Find the index of the smallest element in the remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:


list = [64, 12, 25, 12, 22, 11]
selection_sort(list)
print(list)


