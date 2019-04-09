"""
Singly Linked List

Test:
 n1=Node(1,None)
Instantiating a node
 n2=Node(1,None)
Instantiating a node
 n3=Node(2,None)
Instantiating a node
 n4=Node(4,None)
Instantiating a node
 n5=Node(8,None)
Instantiating a node
 n6=Node(14,None)
Instantiating a node


# Create List
 L.append(n1)
 L.append(n2)
 L.append(n3)
 L.append(n4)
 L.append(n5)
 L.append(n6)


# Show List Items
L.show_items()


"""


class Node:
  def __init__(self, data, next_node):
    print "Instantiating a node"
    self.data = data
    self.next_node = next_node
  
class List:
  def __init__(self):
    self.root = Node(None, None)
    self.last = self.root
    pass

  def get_root(self,):
    return self.root

  def get_tail(self,):
    return self.last

  def append(self, node):
    tail = self.get_tail()
    # link node to tail; making it the new tail
    tail.next_node = node
    self.last = node
  
  def show_items(self):
    node = self.root
    while node.next_node != None:
      print(node.data)
      node = node.next_node
    print(node.data) # for tail
