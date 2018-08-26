from .node import Node

class Stack(object):
    def __init__(self):
        """ Create a new stack and give it some default values
            top = None
            length = 0
            optionally, accept an iterable and create new nodes for them
        """
        self.top = None
        self._length: int = 0

        if iterable is None:
            iterable = []

        for value in iterable:
            self.insert(value)

    def __str__(self):
        """ Return the string representation of a stack
        """
        return f'Top: {self.top} | Length: {self._length}'

    def __repr__(self):
        """ Return the stack object in a readable way
        """
        return f'<Stack | Top: {self.top} | Length: {self._length}>'

    def __len__(self):
        """ Returns the length of the stack
        """
        return self._length

    # def __iter__(self):
    #     if self.head:
    #         self._current = self.head
    #     return self

    def push(self, val):
        """takes any value as an argument and adds that value to the top of the stack
        """
        self.top = Node(val, self.top)
        self._length += 1
        return self.top

    def pop(self):
        """removes & returns the Node at the top of the stack
        """
        tmp = self.top
        self.top = tmp._next
        tmp._next = None

        self._length -= 1
        return tmp.value

    def peek(self):
        """returns the Node at the top of the stack
        """
        return self.top
