Class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

Class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self, head: Optinal[Node]) -> Optional[Node]:
        if not head or not head.next:
            return head

        # Initialize previous pointer
        previous = None
        # Initialize Current Pointer as head
        current = head
        # Run while loop till current is Null
        while current:
            # Intilize Next Pointer as next pointer of current
            next = current.next
            # Now assign the previous pointer to current
            current.next = previous
            # Assign the current pointer to previous
            previous = current
            # Assign Previous pointer to next
            current = next
        # Return the Previous Node
        retunr previous