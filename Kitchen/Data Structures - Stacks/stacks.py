class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        pass

    def push(self, value):
        new_node = Node()
        if not self.bottom:
            self.bottom = new_node
            self.top = self.bottom
        self.top.next = new_node
        self.top = new_node

    def pop(self):
        pass
    
my_stack = Stack()
my_stack.push("Google")
my_stack.push("Osu!")
my_stack.push("AOEII")