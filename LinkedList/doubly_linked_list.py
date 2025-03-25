

class Node:
    
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None



class DoublyLinkedList:

    def __init__(self):
        self.head = None


    def insert_values_at_first(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    


    def insert_values_at_end(self,value):
        new_node = Node(value)

        if self.head is None :
            self.head  = new_node
        else:
            node = self.head
            while node.next is not None :
                node = node.next
            node.next = new_node    
    


    def delete_first(self):
        if self.head is None:
            print("Doubly linked list is empty, nothing to delete.")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None



    def delete_last(self):
        if self.head is None:
            print("Doubly linked list is empty, nothing to delete.")
            return
        node = self.head
        while node.next:
            node = node.next
        if node.prev:
            node.prev.next = None
        else:
            self.head = None

    
    def reverse(self):
        if self.head is None:
            return
        
        temp = None
        current = self.head

        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev  

        if temp:
            self.head = temp.prev

    
    def print_list(self):
        node = self.head
        if node is None:
            print('Doubly linked list is empty')
            return

        while node:
            print(node.data,end=' - ')
            node = node.next



    

val = [23,55,22,33,4]
d1 = DoublyLinkedList()
for v in val:
    d1.insert_values_at_end(v)
    
d1.reverse()
d1.print_list()
    