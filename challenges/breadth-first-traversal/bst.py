from node import Node


class BinaryTree:
    def __init__(self, iterable=None):
        self.root = None
        if iterable is None:
            iterable = []
        for item in iterable:
            self.insert(item)

    def __str__(self):
        return f'Root: {self.root}'

    def __repr__(self):
        return f'<BinaryTree | Root: {self.root} >'

    def in_order(self, callable=lambda node: print(node)):
        """Go left, visit, then go right
        """
        def _walk(node=None):
            if node is None:
                return

            # Go left
            if node.left:
                _walk(node.left)

            # Visit
            callable(node)

            # Go right
            if node.right:
                _walk(node.right)

        _walk(self.root)

    def pre_order(self, callable=lambda node: print(node)):
        """Visit, go left, then right
        """
        def _walk(node=None):
            if node is None:
                return

            # Visit
            callable(node)

            # Go left
            if node.left:
                _walk(node.left)

            # Go right
            if node.right:
                _walk(node.right)

        _walk(self.root)

    def post_order(self, callable=lambda node: print(node)):
        """Go left, then right, Visit
        """
        def _walk(node=None):
            if node is None:
                return

            # Go left
            if node.left:
                _walk(node.left)

            # Go right
            if node.right:
                _walk(node.right)

            # Visit
            callable(node)

        _walk(self.root)

    def insert(self, value):
        """ insert a new node into the tree. Your insertion should follow an O(log n) search solution to find the correct place for inserting the new node.
        """
        if self.root is None:
            self.root = Node(value)
            return
        
        current_node = self.root
        new_node = Node(value)
        while current_node:
            if value == current_node.value:
                raise ValueError('Value already in tree')
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return self
                else:
                    current_node = current_node.left
            elif value > current_node.value:
                if current_node.right is None:
                    current_node.right = new_node
                    return self
                else:
                    current_node = current_node.right
