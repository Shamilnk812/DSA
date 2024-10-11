def selection_sort(list):

    for i in range(len(list)):
        # Find the minimum value in the remaining unsorted portion of the list
        min_val = min(list[i:])
        
        # Find the index of the minimum value in the unsorted portion
        min_index = list.index(min_val, i)  # Use the start parameter to avoid searching the whole list
        
        # Swap the current element with the minimum value found
        list[i], list[min_index] = list[min_index], list[i]


list = [64, 25, 12, 22, 11]
selection_sort(list)
print(list)


