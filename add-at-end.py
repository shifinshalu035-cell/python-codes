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

        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def add_at_the_bigining(self,data):
        new_Node = Node(data)
        new_Node.ref = self.head
        self.head = new_Node
        return self.head

    def add_at_the_end(self,data):
        new_Node = Node(data)
        if self.head is None:
            print("the node is emty in this case")
            return "noun"
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_Node
            return self.head
    def remove_at_the_big(self):
     if self.head is None:
        print("the list is empty")
        return
    self.head =self.head.ref

sll = LinkedList()
sll.add_at_the_bigining(90)
sll.add_at_the_end(900)
sll.remove_at_the_big()

sll.print_ll()
