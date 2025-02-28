# find factorial of a number

def find_factorail(num):
    if num <= 1 :
        return 1
    return num * find_factorail(num -1)

print(find_factorail(6))

