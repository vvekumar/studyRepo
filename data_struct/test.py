from linked import *

def test_linked():
    """test for linked"""

    # Create nodes
    n1 = Node(1, None)
    n2 = Node(2, None)
    n3 = Node(3, None)
    n4 = Node(4, None)
    n5 = Node(5, None)

    # Create empty list
    L = List()

    # Link nodes
    L.append(n1);
    L.append(n2);
    L.append(n3);
    L.append(n4);
    L.append(n5);

    # Show List
    # L.show_items()


    # Call reverse
    # L2= L.reverse()
    L2 = L
    L2.reverse_linear()
    print "L2:"
    print L2.show_items()

    print "Done"

if __name__ == '__main__':
    test_linked()