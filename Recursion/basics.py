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




print(find_factorail(6))
print(find_sum_of_an_array([1,2,3,4,5],len([1,2,3,4,5])))
print(is_palidrome('maaaaam'))