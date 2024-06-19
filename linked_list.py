
### Implementación de una Singly Linked List

#### Definición del Nodo

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



#### Definición de la Lista Enlazada

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Usage example
linked_list = SinglyLinkedList()
linked_list.insert_at_beginning(1)
linked_list.insert_at_beginning(2)
linked_list.insert_at_end(3)
linked_list.print_list()  # Output: 2 -> 1 -> 3 -> None
linked_list.delete_node(1)
linked_list.print_list()  # Output: 2 -> 3 -> None
print(linked_list.search(3))  # Output: True



