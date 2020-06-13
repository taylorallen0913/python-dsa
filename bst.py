class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.num_nodes = 0
        self.height = 0

    def is_empty(self):
        return self.num_nodes is 0

    def get_num_nodes(self):
        return self.num_nodes

    def get_height(self):
        return self.height

    # TODO: Check for uniqueness before adding

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
            return
        self.do_insert(self.root, value)

    def do_insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
                return
            return self.do_insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = BSTNode(value)
                return
            return self.do_insert(node.right, value)
