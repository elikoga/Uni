"""

binary tree in python

"""

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.parent = None

  # for print

  def __repr__(self):
    return "(N: " + str(self.value) + ")"

class BinarySearchTreeWithPreviousAndNext:
  """
  We'll maintain a dict `prev` and `next`
  """
  def __init__(self):
    self.root = None
    self.prev = {}
    self.next = {}

  def insert(self, value):
    node_x = self.root
    node_y = None
    node_z = Node(value)
    while node_x != None:
      node_y = node_x
      if value < node_x.value:
        node_x = node_x.left
      else:
        node_x = node_x.right
    node_z.parent = node_y
    if node_y == None:
      self.root = node_z
      self.prev[node_z] = None
      self.next[node_z] = None
    else:
      if node_z.value < node_y.value:
        node_y.left = node_z
        self.next[self.prev[node_y]] = node_z
        self.prev[node_z] = self.prev[node_y]
        self.prev[node_y] = node_z
        self.next[node_z] = node_y
      else:
        node_y.right = node_z
        self.prev[self.next[node_y]] = node_z
        self.next[node_z] = self.next[node_y]
        self.next[node_y] = node_z
        self.prev[node_z] = node_y

  def search(self, value):
    node_x = self.root
    while node_x != None:
      if value == node_x.value:
        return node_x
      if value < node_x.value:
        node_x = node_x.left
      else:
        node_x = node_x.right
    return None

  def delete(self, node_z):
    """
    node_z is the node to delete
    """
    if node_z.left == None or node_z.right == None:
      node_y = node_z
    else:
      node_y = self.next[node_z]
    if self.prev[node_y] != None:
      self.next[self.prev[node_y]] = self.next[node_z]
    if self.next[node_y] != None:
      self.prev[self.next[node_y]] = self.prev[node_z]
    if self.prev[node_z] != None:
      self.next[self.prev[node_z]] = self.next[node_z]
    if self.next[node_z] != None:
      self.prev[self.next[node_z]] = self.prev[node_z]
    if node_y.left != None:
      node_x = node_y.left
    else:
      node_x = node_y.right
    # node_x is the child of node_y and takes node_y's place
    if node_x != None:
      node_x.parent = node_y.parent
    # parent of node_y is now parent of node_x
    if node_y.parent == None:
      self.root = node_x
    # if node_y was root, node_x is now root
    else:
      # since it wasn't a root, it had a parent
      if node_y == node_y.parent.left:
        node_y.parent.left = node_x
      else:
        node_y.parent.right = node_x
      # node_x is now the child of node_y's parent
    if node_y != node_z:
      node_z.value = node_y.value
      # node_z is now node_y


    return node_y




  def output_in_order(self):
    """
    uses self.next
    starts at leftmost value
    """
    output = []
    node_x = self.root
    while node_x.left != None:
      if node_x.left != None:
        node_x = node_x.left
    while node_x != None:
      output.append(node_x.value)
      node_x = self.next[node_x]
    return output

import random

if __name__ == "__main__":
  # values = [5, 3, 7, 2, 4, 6, 8]
  # values = [1,2,1]
  # values is 10 random values
  values = [random.randint(0, 1000) for i in range(40)]
  print(values)
  bst = BinarySearchTreeWithPreviousAndNext()
  for value in values:
    bst.insert(value)
  first_value = values[0]
  # delete in list and tree
  values.remove(first_value)
  bst.delete(bst.search(first_value))
  output = bst.output_in_order()
  print(output)
  values.sort()
  print(values)
  # print if both are equal
  print(output == values)
