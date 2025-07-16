import json
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self,value):
        self.root = Node(value)

    def insert(self, value):
        if self.root == None:
            return
        new_node = Node(value)
        current_node = self.root

        while current_node:
            if new_node.value < current_node.value:
                if current_node.left == None:
                    current_node.left = new_node
                    return
                current_node = current_node.left
                
            else:
                if current_node.right == None:
                    current_node.right = new_node
                    return
                current_node = current_node.right
      
              
                    
    def lookup(self, value):
        if self.root == None:
            return
        current = self.root
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return current
         
        return None
    #This only works for blaanced BSTs(im too lazy to implement the other cases)
    def remove(self, value): #Go right then left til leaf?
        if self.root is None:#Wtf did i cook
            return
        current_node = self.root
        parent_node = None
        while current_node:#Traverse
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
                
            else:#Node found
                if not current_node.left: #Checks if its a leaf(instant deletion)
                    print(parent_node.left.value)
                    if parent_node.left.value == current_node.value:
                        parent_node.left = None
                    else:
                        parent_node.right = None
                    return
                        
                else:
                    replacement_node = current_node.right
                    while replacement_node.left:#Right -> left(until leaf)
                        replacement_node = replacement_node.left
                        
                    replacement_node.right = current_node.right
                    replacement_node.left = current_node.left
                    if parent_node.left.value == current_node.value:
                        parent_node.left = replacement_node
                    else:
                        parent_node.right = replacement_node
                    return

def traverse(node):
    tree = {"value": node.value}
    tree["left"] = None if node.left is None else traverse(node.left) #Recursively traverses left until leaf
    tree["right"] = None if node.right is None else traverse(node.right) #Same thing but right
    return tree

# Usage
tree = BinarySearchTree(10)
tree.insert(50)
tree.insert(25)
tree.insert(75)
tree.insert(12)
tree.insert(37)
tree.insert(62)
tree.insert(87)
tree.insert(6)
tree.insert(18)
tree.insert(31)
tree.insert(43)
tree.insert(56)
tree.insert(68)
tree.insert(81)
tree.insert(93)
tree.remove(81)
# tree.remove(170)

print(json.dumps(traverse(tree.root)))
print(tree.lookup(15))
