class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("the node is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_at_the_bigining(self,data):
        new_Node = Node(data)
        new_Node.ref = self.head  
        self.head = new_Node

ll1 = LinkedList()
ll1.print_ll()
ll1.add_at_the_bigining(49)
ll1.add_at_the_bigining(90)

ll1.add_at_the_bigining(80)
ll1.print_ll()

