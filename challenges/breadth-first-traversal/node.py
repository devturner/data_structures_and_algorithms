class Node:
    def __init__(self, value, data=None, left=None, right=None):
        self.value = value
        # self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'<Node | Val: {self.value} | Right: {self.right} | Left: {self.left} >'


class Queue_Node:
    def __init__(self, val, _next=None):
        """ Make a new node
        """
        self.val = val
        self._next = _next

    def __str__(self):
        """ Return the string representation of a nodes value
        """
        return f'{self.val}'

    def __repr__(self):
        """ Return the node object in a readable way
        """
        return f'<Node | Val: {self.val} | Next: {self._next}>'
