class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("the stack is empty")
            return "none"
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
            return self.head
    def add_at_the_bigining(self,data):
        new_Node = Node(data)
        new_Node.ref = new_Node
        self.head = new_Node

    def add_at_the_end(self,data):
        new_Node = Node(data)
        if self.head is None:
            print("this is empty")
            return 

        else:
            n = self.head
            while n is not None:
                n = n.ref
            n = new_Node
            return self.head

    def remove_at_the_big(self):
        if self.head is None:
            print("your node is empty") 
            return
        self.head = self.head.ref

    def remove_at_the_end(self):
        if self.head is None:
            print("your noe is empty")
            return 

        else:
            n = self.head

            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

sll = LinkedList()
sll.add_at_the_bigining(200)
sll.add_at_the_end(100)
sll.print_ll()
