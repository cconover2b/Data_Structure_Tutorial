'''
Create and populate a linked list with the given values.
Reverse the linked list and print out the reversed linked list. 
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
  def __init__(self, nodes=None):
    self.head = None
    if nodes is not None:
        node = Node(data=nodes.pop(0))
        self.head = node
        for elem in nodes:
            node.next = Node(data=elem)
            node = node.next

  def reverse(self):
    """
    Reverses the linked list
    """
    prev = None
    node = self.head
    while(node is not None):
      next = node.next
      node.next = prev
      prev = node
      node = next
    self.head = prev
  
  def add_beginning(self, node):
    """
    Inserts a node at the beginning of the linked list.
    """
    node.next = self.head
    self.head = node

  def __repr__(self):
    """
    This stands for representation and is used to get a printable representation of an object.
    """
    # First node is the head node
    node = self.head

    # Create an empty linked list
    all_nodes = []

    # As long as the first node is not empty
    # Add node data to list
    while node is not None:
        all_nodes.append(str(node.data))
        node = node.next
    return " ".join(all_nodes)

print('=========== Test: Reverse Linked List ===========')
my_ll = LinkedList()
my_ll.add_beginning(Node(134))
my_ll.add_beginning(Node(2))
my_ll.add_beginning(Node(44))
my_ll.add_beginning(Node(23))
my_ll.add_beginning(Node(75))
my_ll.add_beginning(Node(3))
my_ll.add_beginning(Node(68))
print (f'Given Linked List: {my_ll}')
my_ll.reverse()
print (f'Reversed Linked List: {my_ll}')
# Expected Results
# Given Linked List: 68 3 75 23 44 2 134
# Reversed Linked List: 134 2 44 23 75 3 68