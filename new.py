
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("The list is empty")
            return

        n = self.head
        while n is not None:
            print(n.data)
            n = n.ref

    def add_at_the_bigining(self, data):
        new_Node = Node(data)
        new_Node.ref = self.head
        self.head = new_Node
        return self.head

    def add_at_the_end(self, data):
        new_Node = Node(data)

        if self.head is None:
            self.head = new_Node
            return self.head

        n = self.head
        while n.ref is not None:
            n = n.ref

        n.ref = new_Node
        return self.head

    def remove_at_the_big(self):
        if self.head is None:
            print("The list is empty")
            return

        self.head = self.head.ref

    def remove_at_the_end(self):
        if self.head is None:
            print("The list is empty")
            return

        if self.head.ref is None:
            self.head = None
            return

        n = self.head

        while n.ref.ref is not None:
            n = n.ref

        n.ref = None


sll = LinkedList()

sll.add_at_the_bigining(90)
sll.add_at_the_end(100)
sll.add_at_the_end(110)

print("Before deleting the last node:")
sll.print_ll()

sll.remove_at_the_end()

print("After deleting the last node:")
sll.print_ll()
