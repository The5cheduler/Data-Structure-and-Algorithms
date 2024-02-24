from typing import List

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def construct(self, array: List[]) -> Node:
        # Check if array is empty
        if not array:
            return None

        # Create head node with first element
        self.head = Node(array[0])
        current = self.head

        # Iterate through rest of array
        for num in array[1:]:

            # Create new node for each element
            current.next = Node(num)

            # Advance current pointer
            current = current.next

        # Return head node
        return self.head

