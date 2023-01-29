class Node:

    def __init__(self, value):
        self.value = value
        self.leftchild = None
        self.rightchild = None

    class Node:
        def __init__(self):
            self.root = None

    def get_left(self):
        return self.leftchild

    def get_right(self):
        return self.rightchild

    def set_left(self, node):
        self.leftchild = node
        return node

    def set_right(self, node):
        self.rightchild = node
        return node

    def set_value(self, newvalue):
        if self.value == None:
            self.value = newvalue

    def get_value(self, node): #equivalent to search method
        if self.value == node:
            print("This node already exists.")
            return
        if node < self.value:
            if self.leftchild:
                self.leftchild.get_value(node)
            else:
                print("Node not found.")
        else:
            if self.rightchild:
                self.rightchild.get_value(node)
                return
            else:
                print("Node not found..")

    def add_node(self, node):
        if self.value == None:
            self.value = node
            return
        if self.value == node:
            return
        if node < self.value:
            if self.leftchild:
                self.leftchild.add_node(node)
            else:
                self.leftchild = Node(node)
        else:
            if self.rightchild:
                self.rightchild.add_node(node)
            else:
                self.rightchild = Node(node)



root = Node(50)
elements = {21,57,3,4,6,10,12,23}
for items in elements:
    root.add_node(items)
root.get_value(10)
root.set_value(18)