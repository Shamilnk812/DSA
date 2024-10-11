

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

    def pre_order(self) :
        print(self.key, end=' ')
        if self.lchild :
            self.lchild.pre_order()
        if self.rchild :
            self.rchild.pre_order() 

arr = [25,10,40,8,3,50]

b1 = BST(15)      
for i in arr :
    b1.insert_values(i)
b1.pre_order()
b1.delete_values(40)
print('')
b1.pre_order()