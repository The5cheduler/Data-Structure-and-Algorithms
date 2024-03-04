class Node:
  def __init__(self, item):
    self.item = item
    self.left_child = None
    self.right._child = None

class Tree:
  def isFullBinaryTree(root:Node):

    if root is None:
      return True

    if root.left_child is None and root.right_child is None:
      return True

    if root.left_child is not None and root.right_child is not None:
      return (isFullBinaryTree(root.left_child) and isFullBinaryTree(root.right_child))
    return False
