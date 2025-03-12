

class BST :
    def __init__(self,data) :
        self.key = data
        self.lchild = None
        self.rchild = None

    def insert_values(self, data):
        if self.key is None :
            self.key = data
            return
        if data < self.key :
            if self.lchild :
                self.lchild.insert_values(data)
            else :
                self.lchild = BST(data)
        else :
            if self.rchild :
                self.rchild.insert_values(data)
            else :
                self.rchild = BST(data)

    def search_value(self, data) :
        if self.key is None :
            print('Tree is empty !')
            return
        if self.key == data :
            print(data, 'is found')
            return
        if data < self.key :
            if self.lchild :
                self.lchild.search_value(data)
            else :
                print(data,'is not found!')
        else :
            if self.rchild :
                self.rchild.search_value(data)
            else :
                print(data, 'is not found!')

    def delete_values(self, data) :
        if self.key is None :
            print('Tree is empty !')
            return

        if data < self.key :
            if self.lchild :
                self.lchild = self.lchild.delete_values(data)
            else :
                print(data, 'is not present') 
        elif data > self.key :
            if self.rchild :
                self.rchild = self.rchild.delete_values(data)
            else :
                print(data, 'is not present')

        else :
            if self.lchild is None :
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None :
                temp = self.lchild
                self = None
                return temp

            node = self.rchild
            while node.lchild :
                node = node.lchild
            self.key = node.key 
            self.rchild = self.rchild.delete_values(node.key)
        return self
    

    # Pre-order traversal (Root -> Left -> Right)
    def pre_order(self):
        print(self.key, end=' ')
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()

    # In-order traversal (Left -> Root -> Right)
    def in_order(self):
        if self.lchild:
            self.lchild.in_order()
        print(self.key, end=' ')
        if self.rchild:
            self.rchild.in_order()

    # Post-order traversal (Left -> Right -> Root)
    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key, end=' ')          

    # Finding the minimum value
    def find_min(self):
        current = self
        while current.lchild :
            current = current.lchild
        return current.key    
    
    # Finding the maximum value
    def find_max(self):
        current = self
        while current.rchild:
            current = current.rchild 
        return current.key    
    

    def find_second_smallest_values(self):
        current_node = self
        parent = None
        while current_node and current_node.lchild:
            parent = current_node
            current_node = current_node.lchild

        if current_node.rchild:
            node = current_node.rchild
            while node.lchild:
                node = node.lchild
            return node.key    
        return parent.key         


    def find_second_largest_value(self):
        current_node = self
        parent_node = None
        while current_node and current_node.rchild:
            parent_node = current_node
            current_node = current_node.rchild

        if current_node.lchild:
            node = current_node.lchild
            while node.lchild:
                node = node.lchild
            return node.key

        return parent_node.key        
    

    # Level order traversal 
    def level_order_traversal(self):  
        if self is None:
            return
        
        queue = [self]  # Initialize queue
        
        while queue:
            current_node = queue.pop(0)  # Dequeue first element
            print(current_node.key, end=" - ") 
            
            # Enqueue left and right children if they exist
            if current_node.lchild:
                queue.append(current_node.lchild)
            if current_node.rchild:
                queue.append(current_node.rchild)

    
    # Height of BST
    def height_of_tree(self):
        # if self is None:
        #     return -1
        
        left_height = self.lchild.height_of_tree() if self.lchild else -1
        right_heiht = self.rchild.height_of_tree() if self.rchild else -1

        return max(left_height,right_heiht) + 1

    
    # Kth smallest value
    def find_kth_smallest_value(self,k):
        count = 0
        result = None

        def helper_func(node):
            nonlocal count , result
            if node is None or result is not None:
                return
            
            helper_func(node.lchild)
            count += 1
            if count == k :
                result =  node.key
                return
            helper_func(node.rchild)

        helper_func(self)
        return result
    



# functoin for find height of BST
def h_of_tree(node):
    if node is None:
        return -1 
    
    left_height = h_of_tree(node.lchild)
    right_height = h_of_tree(node.rchild)
    return max(left_height,right_height) + 1






arr = [25,100,40,8,3,200,50,-1,45]

b1 = BST(30)      
for i in arr :
    b1.insert_values(i)
b1.pre_order()

print(b1.height_of_tree())
print(h_of_tree(b1))
print(b1.find_kth_smallest_value(3))