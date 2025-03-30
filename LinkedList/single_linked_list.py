
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

    
#------------ DELETION  -----------

    def delete_first_element(self):
        if self.head is None :
            print('linked list is empty')
        else:
            self.head = self.head.next
    

    def delete_last_element(self):
        if self.head is None:
            print('linked list is empty')
        else:
            current_node = self.head
            prev = None
            while current_node.next is not None:
                prev = current_node
                current_node = current_node.next
            
            if prev is None :
                self.head = self.head.next
            else:
                prev.next = current_node.next    
    

    def delete_any_node(self,target):

        current_node = self.head
        prev = None
        while current_node:
            if current_node.data == target:
                if prev is None:
                    self.head = self.head.next
                else:
                    prev.next = current_node.next
                return
            prev = current_node
            current_node = current_node.next
        print(f'{target} give target is not present')                


    # Reverse linked list
    def reverse(self):
        current_node = self.head
        prev = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_node
        
        self.head = prev
    

#------------ Sorting -----------
    # find the middle element
    def find_middle(self,head):
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow    

   
    def merge_two_sorted_part(self,left,right):
        if not left :
            return right
        if not right:
            return left
        
        if left.data < right.data:
            result = left
            result.next = self.merge_two_sorted_part(left.next,right)
        else:
            result = right
            result.next = self.merge_two_sorted_part(left,right.next)

        return result        


    def merge_sort(self,head):
        if not head or head.next is None:
            return head
        
        middle = self.find_middle(head)
        new_head = middle.next
        middle.next = None

        left_side = self.merge_sort(head)
        right_side = self.merge_sort(new_head)

        return self.merge_two_sorted_part(left_side,right_side)


    def sort(self):
        self.head = self.merge_sort(self.head)

    # remove duplicates 

    def remove_duplicates(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next



l1 = SinglyLinkedList()
arr = [2,4,6,6,8,10,10]
for i in arr :
    l1.add_last(i)

l1.remove_duplicates()
l1.print_list()
