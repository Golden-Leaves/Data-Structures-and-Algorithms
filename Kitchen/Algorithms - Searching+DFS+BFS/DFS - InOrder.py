class Node:
    def __init__(self, value):
        self.left: Node | None = None
        self.right: Node | None = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                if value < currentNode.value:
                    # Left
                    if not currentNode.left:
                        currentNode.left = newNode
                        return self
                    currentNode = currentNode.left
                else:
                    # Right
                    if not currentNode.right:
                        currentNode.right = newNode
                        return self
                    currentNode = currentNode.right
        return self

    def lookup(self, value):
        if not self.root:
            return False
        currentNode = self.root
        while currentNode:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            elif currentNode.value == value:
                return currentNode
        return None

    def remove(self, value):
        if not self.root:
            return False
        currentNode = self.root
        parentNode = None
        while currentNode:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif currentNode.value == value:
                # We have a match, get to work!

                # Option 1: No right child:
                if currentNode.right is None:
                    if parentNode is None:
                        self.root = currentNode.left
                    else:
                        # if parent > current value, make current left child a child of parent
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left
                        # if parent < current value, make left child a right child of parent
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.left

                # Option 2: Right child which doesnt have a left child
                elif currentNode.right.left is None:
                    if parentNode is None:
                        self.root = currentNode.left
                    else:
                        currentNode.right.left = currentNode.left

                        # if parent > current, make right child of the left the parent
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.right

                        # if parent < current, make right child a right child of the parent
                        elif currentNode.value > parentNode.value:
                            parentNode.right = currentNode.right

                # Option 3: Right child that has a left child
                else:
                    # find the Right child's left most child
                    leftmost = currentNode.right.left
                    leftmostParent = currentNode.right
                    while leftmost.left is not None:
                        leftmostParent = leftmost
                        leftmost = leftmost.left

                    # Parent's left subtree is now leftmost's right subtree
                    leftmostParent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right

                    if parentNode is None:
                        self.root = leftmost
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = leftmost
                        elif currentNode.value > parentNode.value:
                            parentNode.right = leftmost

                return True
        # if we fall out of the loop, not found
        return False

    def BreadthFirstSearch(self):
        currentNode = self.root
        lst = []
        queue = []
        queue.append(currentNode)

        while len(queue) > 0:
            currentNode = queue.pop(0)  # JS shift()
            lst.append(currentNode.value)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return lst

    def BreadthFirstSearchR(self, queue, lst):
        if not len(queue):
            return lst
        currentNode = queue.pop(0)
        lst.append(currentNode.value)

        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)

        return self.BreadthFirstSearchR(queue, lst)

def traverse_inorder(node: Node,result:list):
    if node is None:
        return result
    traverse_inorder(node.left,result) # type: ignore
    result.append(node.value)
    traverse_inorder(node.right,result) # type: ignore
    return result
# Build tree
tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

print('BFS', tree.BreadthFirstSearch())
print('BFS', tree.BreadthFirstSearchR([tree.root], []))
print(traverse_inorder(tree.root,[])) #type: ignore

#     9
#  4     20
#1  6  15  170

def traverse(node):
    tree_dict = {'value': node.value}
    tree_dict['left'] = None if node.left is None else traverse(node.left)
    tree_dict['right'] = None if node.right is None else traverse(node.right)
    return tree_dict
