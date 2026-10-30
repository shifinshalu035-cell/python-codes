def search(self, target):
    n = self.head

    while n is not None:
        if n.data == target:
            print("Value found!")
            return True

        n = n.ref

    print("Value not found!")
    return Falsel