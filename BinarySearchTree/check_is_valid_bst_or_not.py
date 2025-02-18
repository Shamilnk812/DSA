

class BST:
    def __init__(self,value=None):
        self.value = value
        self.lchild = None
        self.rchild = None


    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.value,end=' - ')   
        if self.rchild:
            self.rchild.in_order() 

# check whether given bst is valid or not !
def is_valid(root,min_val=float('-inf'),max_val=float('inf')):
    if root is None:
        return True
    
    if not (min_val < root.value < max_val):
        return False
    
    return (is_valid(root.lchild,min_val,root.value)
            and is_valid(root.rchild,root.value,max_val))



root = BST(10)
root.lchild = BST(5)
root.rchild = BST(15)
root.lchild.lchild = BST(2)
root.lchild.rchild = BST(7)
root.rchild.lchild = BST(12)
root.rchild.rchild = BST(20)
root.in_order()
print('----------')
print(is_valid(root))