
def linear_search(lst,target):
    for i in range(len(lst)):
        if lst[i] == target :
            return i + 1
    return -1



lst = [2,84,45,63,12]
target = 12
result = linear_search(lst,target)
if result != -1 :
    print(f"item found at {result} position")
else :
    print('not found !')   