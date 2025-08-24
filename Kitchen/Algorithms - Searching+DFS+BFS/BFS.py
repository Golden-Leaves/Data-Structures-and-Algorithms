class Node:
    def __init__(self, value):
        self.left: Node | None = None
        self.right: Node |None = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if current_node.value > value:
                    # Left
                    if current_node.left is None:
                        current_node.left = new_node
                        return self
                    current_node = current_node.left
                else:
                    # Right
                    if current_node.right is None:
                        current_node.right = new_node
                        return self
                    current_node = current_node.right

    def lookup(self, value):
        if self.root is None:
            return False
        current_node = self.root

        while current_node:
            if current_node.value > value:
                # Left
                current_node = current_node.left
            elif current_node.value < value:
                # Right
                current_node = current_node.right
            elif current_node.value == value:
                return current_node
        return False

    def remove(self, value):
        if self.root is None:
            return False
        current_node = self.root
        parent_node = None
        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            elif current_node.value == value:
                # We have a match, get to work!

                # Option 1: No right child:
                if current_node.right is None:
                    if parent_node is None:
                        self.root = current_node.left
                    else:
                        # if parent > current value, make current left child a child of parent
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.left

                        # if parent < current value, make left child a right child of parent
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.left

                # Option 2: Right child which doesn’t have a left child
                elif current_node.right.left is None:
                    current_node.right.left = current_node.left
                    if parent_node is None:
                        self.root = current_node.right
                    else:
                        # if parent > current, make right child of the left the parent
                        if current_node.value < parent_node.value:
                            parent_node.left = current_node.right

                        # if parent < current, make right child a right child of the parent
                        elif current_node.value > parent_node.value:
                            parent_node.right = current_node.right

                # Option 3: Right child that has a left child
                else:
                    # find the Right child's left most child
                    leftmost = current_node.right.left
                    leftmost_parent = current_node.right
                    while leftmost.left is not None:
                        leftmost_parent = leftmost
                        leftmost = leftmost.left

                    # Parent's left subtree is now leftmost's right subtree
                    leftmost_parent.left = leftmost.right
                    leftmost.left = current_node.left
                    leftmost.right = current_node.right

                    if parent_node is None:
                        self.root = leftmost
                    else:
                        if current_node.value < parent_node.value:
                            parent_node.left = leftmost
                        elif current_node.value > parent_node.value:
                            parent_node.right = leftmost
                return True
    def breadth_first_search(self):
        if not self.root:
            return []
        current_node = self.root
        result = []
        queue = []
        queue.append(current_node)
        while queue:
            current_node : Node = queue.pop(0) #You can implement a linked list here for O(1)
              
            result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result

# def traverse(node):
#     tree = {"value": node.value}
#     tree["left"] = None if node.left is None else traverse(node.left)
#     tree["right"] = None if node.right is None else traverse(node.right)
#     return tree
def traverse_inorder(node: Node,result:list):
    if node is None:
        return result
    traverse_inorder(node.left,result) # type: ignore
    result.append(node.value)
    traverse_inorder(node.right,result) # type: ignore
    return result
tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.remove(170)
print(tree.breadth_first_search())
print(traverse_inorder(tree.root,[])) # type: ignore
# import json
# print(json.dumps(traverse(tree.root)))
# print(tree.lookup(20))
# #     9
# #  4     20
# #1  6  15  170
