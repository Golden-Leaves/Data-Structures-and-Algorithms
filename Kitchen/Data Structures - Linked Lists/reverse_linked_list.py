from runtime_utils import track_time
class Node():
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None
class LinkedList(): #Using this for the sake of simplicity
    def __init__(self,value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
        
    def __str__(self):
        return str(self.__dict__)
    
    def append(self,value): #Wowzers
        self.tail.next = Node(value) #This pointer somehow doesnt disappear
        current_node = self.tail.next
        self.tail = current_node
        self.length += 1
    
    def prepend(self,value):
        previous_head = self.head
        self.head = Node(value)
        self.head.next = previous_head
        self.length += 1
        
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
        self.length += 1
        
        
    def delete(self,idx):
        current_node = self.head
        if idx == 0:
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
                
        for i in range(idx - 1): #Traversal
            current_node = current_node.next
        next_node = current_node.next.next #The node right after the deleted node
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
        
    def reverse(self): #owo that sleep sure was something
        current_node = self.head
        previous_node = None
        next_node = current_node.next
        # for i in range(self.length): #Okay my version is ass
        #     if not self.head.next:
        #         return self.head
        #     if current_node == self.head:
        #         current_node.next = None
        #         previous_node = current_node
        #         current_node = next_node
        #         next_node = current_node.next
        #         continue
        #     print(current_node.data)
        #     current_node.next = previous_node   
        #     previous_node = current_node
        #     current_node = next_node
        #     if not current_node is None:
        #         next_node = current_node.next
        
        first = self.head
        second = first.next

        while second:
            temp = second.next     # Save third node
            second.next = first    # Reverse the pointer
            first = second         # Advance first
            second = temp          # Advance second

        self.head.next = None      # Original head becomes tail
        self.head = first          # Reassign head to the new front
        return self.print_list()

        self.head = self.tail    
        self.tail = current_node    
        
        
        
my_linked_list = LinkedList(10)
my_linked_list.append(12)
my_linked_list.append(20)
my_linked_list.append(120)
my_linked_list.append(232)
my_linked_list.append(52)
my_linked_list.prepend(121)
my_linked_list.insert(2,1)
my_linked_list.delete(3)
my_linked_list.reverse()
my_linked_list.print_list()
