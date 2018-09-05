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
