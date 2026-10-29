class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("your node is empty")
            return "None"

        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

    def add_at_the_bigining(self,data):
        new_Node = Node(data)
        self.head.ref = new_Node
        self.head = new_Node
        return self.head

    def add_at_the_end(self,data):
        new_Node = Node(data)
        if self.head is None:
            n = self.head
            while n is not None:
                n = n.ref
            n = new_Node
            return self.head

ll1 = LinkedList()
ll1.add_at_the_bigining(30)
ll1.add_at_the_bigining(90)
ll1.add_at_the_bigining(80)
ll1.add_at_the_end(90)
ll1.add_at_the_end(80)
ll1.print_ll()


                