
class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.next = None

class SinglyLinkedList:

    def __init__(self) -> None:
        self.head = None 

    def print_list(self) :
        if self.head is None :
            print('Linked list is empty !')
        else :
            current_node = self.head
            while current_node is not None :
                print(current_node.data,end=" - ")
                current_node = current_node.next 
            print(None)        
    

# -----------  INSERTION ----------
            
    def add_first(self, data):
        new_node = Node(data) 
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data) :
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
        else :
            current_node = self.head
            while current_node.next is not None :
                current_node = current_node.next 
            current_node.next = new_node
    

    # Add a new node with data before the node with value x.
    def add_before_node(self, data, x):
       
        if self.head is None:
            print("Linked list is empty!")
            return

        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == x:
                break
            current_node = current_node.next

        if current_node.next is None:
            print(f"{x} is not present in the linked list.")
        else:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

    
    # Add a new node with data after node with value x.
    def add_after_node(self, data, x):
        current_node = self.head
        while current_node is not None:
            if current_node.data == x:
                break
            current_node = current_node.next

        if current_node is None:
            print(f"{x} is not present in the linked list.")
        else:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

    

        

                
l1 = SinglyLinkedList()
arr = [2,3,5,7]
for i in arr :
    l1.add_last(i)

l1.add_before_node(111,6)
l1.print_list()