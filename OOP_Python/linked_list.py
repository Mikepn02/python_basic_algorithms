class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        current = self.head
        while current:
            print(current.data,end="-> ")
            current = current.next # actually this is to call the next data in th node
        print(None)
    
    def insert(self, data):
     new_node = Node(data)  # Create a new node with the provided data
     if not self.head:  # If the linked list is empty
        self.head = new_node  # Make the new node the head of the linked list
     else:
        current = self.head  # Start from the head of the linked list
        while current.next:
            current = current.next  # Move to the last node in the linked list
        current.next = new_node  # Add the new node to the end of the linked list

    def delete(self,data):
        if not self.head: 
            return
        if self.head.data == data: #this is to check if the data to be deleted in node matches with the data in the node
           self.head = self.head.next
           return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
        current = current.next # this set current to none to mean that the value of current is completely deleted

    def search(self , data):
        current = self.head
        while current:
            if current.data == data:
             return True
            current = current.next
        return False
ll = LinkedList()
ll.insert(5)
ll.insert(10)
ll.insert(15)
ll.display()  # Output: 5 -> 10 -> 15 -> None

ll.delete(10)
ll.display()  # Output: 5 -> 15 -> None

print(ll.search(15))  # Output: True
print(ll.search(10))  # Output: False
