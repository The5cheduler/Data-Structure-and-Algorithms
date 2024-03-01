class Node:
    def __init__(self, data = None, next = None):
        self.data =  data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def delete_tail(self):
        if self.head is None or self.head.next is None:
            return None

        current_head = self.head

        while current_head.next.next is not None:
            current_head = current_head.next

        current_head.next = None

        return self.head

    def deleteNode(self, node):
      node.val, node.next = node.next.val, node.next.next

    def print_ll(self):
        while value is not None:
            print(self.head.data, end="=>")
            self.head = self.head.next

# Main function
if __name__ == "__main__":
    # Initialize an array with integer values
    arr = [2, 5, 8, 7]

    # Create the linked list with nodes initialized with array values
    ll = LinkedList()
    for value in arr:
        ll.append(value)

    # Delete the tail of the linked list
    ll.delete_tail()

    # Print the modified linked list
    ll.print_ll()
