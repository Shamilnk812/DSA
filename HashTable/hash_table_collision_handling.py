class Node:

    def __init__(self,key,value):
        self.key = key 
        self.value = value 
        self.next = None


class HashTableCollisionHandling:

    def __init__(self):
        self.size = 10
        self.table = [None] * self.size
    
    def hash_function(self,key):
        h = 0
        for char in key :
            h += ord(char)
        return h % self.size
    
    def insert_values(self,key,value):
        h = self.hash_function(key)
        current = self.table[h]

        if current is None:
            self.table[h] = Node(key,value)
        else:
            while current is not None:
                if current.key == key :
                    current.value = value
                    return  
                if current.next is None:
                    break  
                current = current.next
                
            current.next = Node(key,value)        


    def display(self):
        for index,head in enumerate(self.table):
            print(f'index {index} : ',end='  ')
            current = head 
            while current is not None:
                print(f' ({current.key} - {current.value}) ',end='  ->  ')
                current = current.next
            print('None')


    def get_values(self,key):
        h = self.hash_function(key)
        current = self.table[h]
        while current is not None:
            if current.key == key :
                return current.value
            current = current.next


    def delete_values(self,key):
        h = self.hash_function(key)
        current = self.table[h]
        prev = None
        while current is not None:
            if current.key == key :
                if prev is None :
                    self.table[h] = current.next
                else :
                    prev.next = current.next
                return
            prev = current
            current = current.next


h1 = HashTableCollisionHandling()
h1.insert_values('jan 1',400)
h1.insert_values('jan 2',5000)
h1.insert_values('jan 6',111)
h1.insert_values('jan 17',566)

h1.insert_values('jan 17',556656565)
h1.delete_values('jan 6')
h1.display()
print('---------')
print(h1.get_values('jan 15'))