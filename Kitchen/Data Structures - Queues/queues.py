class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)
    
    def peek(self):
        print(self.top.value)

    def push(self, value):
        new_node = Node(value)
        
        if not self.bottom:
            self.bottom = new_node
            self.top = self.bottom
            self.length += 1
            return
        
        self.top.next = new_node
        self.top = new_node
        self.length += 1

    def pop(self):
        current_node = self.top
        
       
    
    def print_stack(self): #Debug
        stack_arr = []
        current_node = self.bottom
        for i in range(self.length):
            stack_arr.append(current_node.value)
            if current_node.next:
                current_node = current_node.next
        print(stack_arr)
            
    
my_stack = Stack()
my_stack.push("Google")
my_stack.push("Osu!")
my_stack.push("AOEII")
my_stack.peek()
print(my_stack.pop())
my_stack.print_stack()