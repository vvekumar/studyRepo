"""
Singly Linked List

Test:
n1=Node(1,None)
Instantiating a node
n2=Node(1,None)
Instantiating a node
n3=Node(2,None)
Instantiating a node
n4=Node(4,None)
Instantiating a node
n5=Node(8,None)
Instantiating a node
n6=Node(14,None)

Instantiating a node


# Create List
L.append(n1)
L.append(n2)
L.append(n3)
L.append(n4)
L.append(n5)
L.append(n6)


# Show List Items
L.show_items()


"""

import copy


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

  def unlink(self, node):
    """delete a particular node"""
    next_ptr = node.next_node
    data = node.data



  def pop(self):
    # remove self.last()
    node = self.root
    print "In pop.."
    # Find last element
    while node.next_node != None:
      print(node.data)
      curr = node
      node = node.next_node

    # update + return as necessary
    if 'curr' in locals():
      curr.next_node = None
      self.last = curr
    else:
      # root element case, so None-out root
      root = self.root
      self.root = Node(None, None)
      return root
    return node  # popped node


  def show_items(self):
    node = self.root
    while node.next_node != None:
      print(node.data)
      node = node.next_node
    print(node.data) # for tail


  def reverse(self):
    """reverse a list"""

    """
    Flow :
    1 -> 2 -> 3 -> 4 -> NULL

    Create a new list L2:
    iterate L1 (from end)
    L2.append(L1[i])
    """
    L2 = List()
    while True:
      popped = self.pop()
      print "popped: ", popped.data
      if not popped.data is None:
        L2.append(popped)
        print "In reverse.."
        L2.show_items()
      else :
        print "break from reverse.."
        break
    return L2


  def reverse_linear(self):
    """reverse a list in linear time(hint : use swap + temp Node)"""
    temp = Node(None, None)
    prev = Node(None, None)

    head = self.root
    while head.next_node != None:
      temp = copy.copy(head)
      # print "Curr", head.data
      # print "Head(next)(old)", head.next_node.data

      head.next_node = prev
      # print "Head(next)(new)", head.next_node.data
      prev = copy.copy(head)
      head = temp.next_node
      # print "New Head", head.data
      # print "****"

    # print "Curr", head.data
    # print "Head(next)(old)", head.next_node
    head.next_node = prev # for last element
    # print "Head(next)(new)", head.next_node.data
    self.root = head
