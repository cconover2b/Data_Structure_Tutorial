'''
For this problem, your goal is to take an array and convert it into a balanced BST.
'''

class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node(object):
        """
        Each node of the BST will have data and links to the 
        left and right sub-array. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None
        
def array_to_bst(array):
    # If array is none then return None
    if not array:
        return None
    # Find the middle of the array
    middle = len(array)//2
    node = BST.Node(array[middle])
    node.left = array_to_bst(array[:middle])
    node.right = array_to_bst(array[middle+1:])
    return node

def order(node): 
    if not node: 
        return      
    print(node.data)
    order(node.left) 
    order(node.right)   

print("=========== ARRAY 1 TESTS ===========")
array = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(array)
result = array_to_bst(array)
print("\nArray to a height balanced BST:")
print(order(result))
'''
Expected Results:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

Array to a height balanced BST:
7
4
2
1
3
6
5
11
9
8
10
13
12
None
'''

print("\n=========== ARRAY 2 TESTS ===========")
array1 = [10, 20, 30, 40, 50, 60]
print(array1)
result1 = array_to_bst(array1)
print("\nArray to a height balanced BST:")
print(order(result1))
'''
Expected Results:
[10, 20, 30, 40, 50, 60]

Array to a height balanced BST:
40
20
10
30
60
50
None
'''

print("\n=========== ARRAY 3 TESTS ===========")
array2 = [x for x in range(25)]
print(array2)
result2 = array_to_bst(array2)
print("\nArray to a height balanced BST:")
print(order(result2))
'''
Expected Results:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

Array to a height balanced BST:
12
6
3
1
0
2
5
4
9
8
7
11
10
19
16
14
13
15
18
17
22
21
20
24
23
None
'''