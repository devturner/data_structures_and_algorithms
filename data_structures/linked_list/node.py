class Node(object):
    def __init__(self, val, _next=None):
        self.val = val
        self._next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return f'<Node | Val: {self.val} | Next: {self._next}>'