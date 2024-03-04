class Node:
  def __init__(self,item):
    self.left = None
    self.right = None
    self.val = item

def inorder(root):

  if root:
    # Traverse Left
    inorder(root.left)
    # Traverse Root
    print(str(root.val) + '->', end='')
    # Traverse Right
    inorder(root.right)

def postorder(root):

  if root:
    # Traverse Left
    postorder(root.left)
    # Traverse Right
    postorder(root.right)
    # Traverse Root
    print(str(root.val) + '->', end=')

def preorder(root):

  if root:
    # Traverse Root
    print(str(root.val) + '->', '')
    # Traverse Left
    preorder(root.left)
    # Traverse Right
    preorder(root.right)
