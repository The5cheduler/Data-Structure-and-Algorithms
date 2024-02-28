# A Single node of a singly Linked List
class Node:
  # constructor
  def __init__(self, data, next = None):
    self.data = data
    self.next = next

# Linked List class with a single head node
class LinkedList:
  def __init__(self):
    self.head = None

# Linked List with Single Node
LL = LinkedList()
LL.head = Node(3)


# Access the LinkedList's Data
head_value = LL.head.data
print(head_value)
