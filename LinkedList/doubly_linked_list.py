

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
    d1.insert_values_at_first(v)
d1.print_list()    
    