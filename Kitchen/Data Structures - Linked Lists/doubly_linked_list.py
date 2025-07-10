from runtime_utils import track_time
class Node():
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None
class DoublyLinkedList(): #Singly and Doubly sounds goofy ngl
    def __init__(self,value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
        
    def __str__(self):
        return str(self.__dict__)
    
    def append(self,value): 
        self.tail.next = Node(value) 
        previous_node = self.tail
        self.tail = self.tail.next
        self.tail.previous = previous_node
        self.length += 1
    
    def prepend(self,value):
        new_node = Node(value) #Andrei's method
        new_node.next = self.head
        
        if self.length == 0:
            self.tail = new_node
        else:
            self.head.previous = new_node
            
        self.head = new_node
        
    def insert(self,idx,value): 
        current_node = self.head
        if idx == 0:
            self.prepend(value)
            self.length += 1
            return
            
            
        for i in range(idx - 1): #Traversal
            current_node = current_node.next
        
        next_node = current_node.next
        current_node.next = Node(value)
        current_node.next.next = next_node
        current_node.next.next.previous = current_node.next #I'm sorry to the linked list gods 🙏🙏, im too lazy to implement new_node
        print(current_node.data)
        
        self.length += 1
        
        
    def delete(self,idx):
        current_node = self.head
        if idx == 0:
            self.head = self.head.next
            self.head.previous = None
            if self.length == 1:
                self.tail = None
            self.length -= 1
            return
                
        for i in range(idx - 1): #Traversal
            current_node = current_node.next
        next_node = current_node.next.next #The node right after the deleted node
        next_node.previous = current_node
        current_node.next = next_node #Dereferences the node you wanna delete
        self.length -= 1
        return
    def print_list(self):
        linked_list_array = []
        current_node = self.head
        for i in range(my_linked_list.length):
            node = current_node
            linked_list_array.append(node.data)
            current_node = node.next
        print(linked_list_array)
        
my_linked_list = DoublyLinkedList(10)
my_linked_list.append(12)
my_linked_list.append(20)
my_linked_list.append(120)
my_linked_list.append(232)
my_linked_list.append(52)
my_linked_list.prepend(121)
my_linked_list.insert(2,1)
my_linked_list.delete(3)
my_linked_list.print_list()
