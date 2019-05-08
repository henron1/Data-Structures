class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value: # is current node less than new node?
      if not self.left: # if not left child node
        self.left = BinarySearchTree(value) # insert new node
      else:
        self.left.insert(value)
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
      

  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass