class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(data=value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data=value)

    def length(self) -> int:
        if not self.head:
            return 0

        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count