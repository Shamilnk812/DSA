def merge_sort(list):
    # Base case: if the list has more than one element, it needs to be sorted
    if len(list) > 1:
        # Find the middle point and divide the list into two halves
        mid = len(list) // 2
        left_sublist = list[:mid]   # Left half
        right_sublist = list[mid:]  # Right half

        # Recursively call merge_sort on both halves
        merge_sort(left_sublist)
        merge_sort(right_sublist)

        # Initialize indices for iteration
        i = j = k = 0

        # Merge the sorted halves
        # Compare elements of the left and right sublists and merge them in sorted order
        while len(left_sublist) > i and len(right_sublist) > j:
            if left_sublist[i] < right_sublist[j]:
                list[k] = left_sublist[i]  # Take element from the left sublist
                i += 1  # Move the index of left sublist forward
            else:
                list[k] = right_sublist[j]  # Take element from the right sublist
                j += 1  # Move the index of right sublist forward
            k += 1  # Move the main list index forward

        # If there are remaining elements in the left sublist, add them
        while len(left_sublist) > i:
            list[k] = left_sublist[i]
            i += 1
            k += 1

        # If there are remaining elements in the right sublist, add them
        while len(right_sublist) > j:
            list[k] = right_sublist[j]
            j += 1
            k += 1


list = [75, 25, 100, 50]

merge_sort(list)
print(list)
