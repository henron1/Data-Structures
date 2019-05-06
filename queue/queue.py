class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node
  
  def set_next(self, new_next):
    self.next_node = new_next
    

class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = list()

  def enqueue(self, item):
    self.storage.insert(0, item)
    self.size += 1
  
  def dequeue(self):
    pass

  def len(self):
    pass
