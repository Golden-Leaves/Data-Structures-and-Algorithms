class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.is_empty():
            return None
        return self.first.value

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = new_node
            self.last = self.first
        else:
            self.last.next = new_node
            self.last = self.last.next
            
        self.length += 1
        return new_node.value
    
    def dequeue(self):
        if self.is_empty():
            self.last = None
            dequeued_node = None
        else:
            dequeued_node = self.first
            self.first = self.first.next
            
        self.length -= 1
        return dequeued_node.value

    def is_empty(self):
        if self.length == 0:
            return True
        return False
    
    def print_queue(self):
        queue_arr = []
        current_node = self.first
        for i in range(self.length):
            queue_arr.append(current_node.value)
            if current_node.next:
                current_node = current_node.next
        print(queue_arr)
my_queue = Queue()
my_queue.enqueue("Osu!")
my_queue.enqueue("VSCode")
my_queue.enqueue("ChatGPT")
my_queue.dequeue()
my_queue.print_queue()