class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.num_nodes = 0
        self.height = 0

    def is_empty(self):
        return self.num_nodes == 0

    def is_leaf(self, node):
        return node.left and node.right is None

    # Get leftmost node in a node's subtree
    def get_leftmost_node(self, node):
        current_node = node
        # Traverse node's left subtree until we hit the bottom
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    # Check if key exists in tree
    def contains(self, key):
        return self.do_contains(self.root, key)

    # Recursive contains helper method
    def do_contains(self, node, key):
        # If traversed to bottom of tree
        if node is None:
            return False

        # If key is less than node key we traverse its left subtree
        if key < node.key:
            return self.do_contains(node.left, key)
        # If key is greater than node key we traverse its right subtree
        elif key < node.key:
            return self.do_contains(node.right, key)

        # If key is node key
        elif key is node.key:
            return True

    # Insert value into bst
    def insert(self, key):
        # If tree is empty, set root to value
        if self.num_nodes == 0:
            self.root = BSTNode(key)
            self.num_nodes += 1
            return

        # If key exists in tree, don't insert it
        if self.contains(key):
            return

        # If root exists, recurse through tree and insert
        self.num_nodes += 1
        return self.do_insert(self.root, key)

    # Recursive insert helper method
    def do_insert(self, node, key):
        # If key is less than node key
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
                return
            return self.do_insert(node.left, key)

        # If key is greater than node key
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key)
                return

        return self.do_insert(node.right, key)

    def delete(self, key):
        # If tree is empty, return
        if self.num_nodes == 0:
            return

        # If key exists in tree, delete the key
        if self.contains(key):
            self.num_nodes -= 1
            return self.do_delete(self.root, key)

    def do_delete(self, node, key):
        if node is None:
            return

        # Traverse until we find node to be deleted
        if key < node.key:
            node.left = self.do_delete(node.left, key)
        if key > node.key:
            node.right = self.do_delete(node.right, key)

        # If node to be deleted is found
        if key is node.key:
            # Right subtree exists
            if node.right is None:
                left_root = node.left
                node = None

                return left_root

            # Left subtree exists
            elif node.left is None:
                right_root = node.right
                node = None

                return right_root

            # If node has two children
            else:
                # Get leftmost node in the node's right subtree
                leftmost_node = self.get_leftmost_node(node.right)

                # Swap the node and leftmost node's key
                node.key = leftmost_node.key

                # Delete leftmost node in the node's right subtree
                node.right = self.do_delete(node.right, leftmost_node.key)
