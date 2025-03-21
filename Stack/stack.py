
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# Reverse a string using a stack

def reverse_strings(strr) :
    stack = Stack()
    for char in strr:
        stack.push(char)
    
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()    

    return reversed_str





def is_valid_parentheses(strr):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in strr:
        if char in bracket_map.values():  # If it's an opening bracket, push to stack
            stack.append(char)
        elif char in bracket_map.keys():  # If it's a closing bracket
            if not stack or stack.pop() != bracket_map[char]:  # Check if top matches
                return False
        else:
            return False  
        
    return len(stack) == 0  


print(is_valid_parentheses("({[]})"))  
print(is_valid_parentheses("({[)]}"))  
print(is_valid_parentheses("((()))"))  

