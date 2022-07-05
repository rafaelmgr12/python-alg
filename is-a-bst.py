""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check(root, min_val, max_val):
    if root is None:
        return True
    if root.data < min_val or root.data > max_val:
        return False
    return check(root.left, min_val, root.data-1) and check(root.right, root.data+1, max_val)
def check_binary_search_tree_(root):
    return check(root, 0 , 10**4)
