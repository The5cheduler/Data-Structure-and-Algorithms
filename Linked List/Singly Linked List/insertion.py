Class Node:
def __init__(self, data = None, next =None):
  self.data = None
  self.next = None

Class LinkedList:
  def __init__(self):
    seld.head = None

  def insert(self, data):
    new_node = Node(data) # initialize node class with data and assign it to new node
    if(self.head): # check if self.head has value
      current = self.head # as self.head already has value create new pointer current to store self.head
      while(current.next): 
        current = current.next
      current.next = new_node
    else:
      self.head = new_node

  def print(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next
