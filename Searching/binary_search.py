def binary_search(lst, target):
    # Initialize the left and right pointers
    left = 0
    right = len(lst) - 1

    # Continue searching while left pointer is less than or equal to the right pointer
    while left <= right:
        # Find the middle index
        mid = (left + right) // 2
        
        # If target is found at mid, return the 1-based index
        if lst[mid] == target:
            return mid + 1
        
        # If target is smaller, discard the right half
        elif lst[mid] > target:
            right = mid - 1
        
        # If target is larger, discard the left half
        else:
            left = mid + 1

    # Return -1 if target is not found
    return -1



lst = [2, 4, 6, 8, 10]
target = 8

result = binary_search(lst, target)

if result != -1:
    print(f'Item {target} found at position {result}')
else:
    print(f'Item {target} not found!')
