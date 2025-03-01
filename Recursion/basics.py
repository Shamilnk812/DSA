# find factorial of a number

def find_factorail(num):
    if num <= 1 :
        return 1
    return num * find_factorail(num -1)

def find_sum_of_an_array(arr,n):
    if n <= 0:
        return 0
    return arr[n-1] + find_sum_of_an_array(arr,n-1)


def is_palidrome(strr):
    if len(strr) <= 1 :
        return True
    if strr[0] != strr[-1]:
        return False
    return is_palidrome(strr[1:-1])


def reverse_string(strr):
    # base case
    if len(strr) <= 0 :
        return strr
    
    return reverse_string(strr[1:]) + strr[0]


def find_min_value(arr, i=0, min_val=None):
    if i == len(arr):
        return min_val
    if min_val is None or arr[i] < min_val:
        min_val = arr[i]
    return find_min_value(arr,i+1,min_val)    
    

def find_max_value(arr, i=0, max_val=None):
    if i == len(arr):
        return max_val
    if max_val is None or arr[i] > max_val:
        max_val = arr[i]
       
    return find_max_value(arr,i+1,max_val)


print(find_factorail(6))
print(find_sum_of_an_array([1,2,3,4,5],len([1,2,3,4,5])))
print(is_palidrome('maaaaam'))
print(reverse_string('abcdef'))
print(find_max_value([4,222,112,12]))
print(find_min_value([32,1,33,-5,54]))
