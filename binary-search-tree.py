class Node:
    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

class BST:
    def __init__(self):
        self.root = None


    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left_child is None:
                        current_node.left_child = new_node
                        break
                    else: 
                        current_node = current_node.left_child
                else:
                    if current_node.right_child is None:
                        current_node.right_child = new_node
                        break
                    else: 
                        current_node = current_node.right_child

    def search(self, value):
        current_node = self.root
        while current_node is not None:
            if current_node.value == value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return None

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left_child)
            print(node.value)
            self.inorder_traversal(node.right_child)                                    
