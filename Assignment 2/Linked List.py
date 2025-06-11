class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def show(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next

    def delete(self, index):
        if self.head is None:
            print("Error: List is empty")
            return
        if index <= 0:
            print("Error: Invalid index")
            return
        if index == 1:
            print(f"Deleted: {self.head.data}")
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 2):
            if current.next is None:
                print("Error: Index out of range")
                return
            current = current.next
        if current.next is None:
            print("Error: Index out of range")
        else:
            print(f"Deleted: {current.next.data}")
            current.next = current.next.next

# Implement
ll = LinkedList()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.show()
ll.delete(3)
ll.show()
ll.delete(10)
ll2 = LinkedList()
ll2.delete(1)
