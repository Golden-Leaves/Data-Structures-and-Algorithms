class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.array = []


    def __str__(self):
        return str(self.__dict__)
    
    def peek(self):
        if self.is_empty():
            print(None)
        print(self.array[-1])

    def push(self, value):
        self.array.append(value)
        return value    

    def pop(self):
        if self.is_empty():
            return None
        self.array.pop()
    
    def is_empty(self):
        if self.length == 0:
            return True
        return False
    
    def print_stack(self): #Debug
        stack_arr = []
        current_node = self.top
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