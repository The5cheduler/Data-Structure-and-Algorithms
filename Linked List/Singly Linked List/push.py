class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def push(self, data):
    new_node = Node(data) # initialize new node with data
    new_node.next = self.head # assign current node's next pointer set to self.head
    self.head = new_node # set haed pointer to newly created node
