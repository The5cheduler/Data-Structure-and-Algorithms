class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(data=value)
        else:
            current = self.head
            while current:
                current = current.next
            current.next = Node(data=value)

    def search(self, value):
        if self.head is None: return False

        current = self.head
        while current:
            if current.data == value:
                return True
        return False
