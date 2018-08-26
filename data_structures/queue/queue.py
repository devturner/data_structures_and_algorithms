from .node import Node

class Queue(object):
    def __init__(self):
        """ Create a new queue and give it some default values
            top = None
            length = 0
            optionally, accept an iterable and create new nodes for them
        """
        self.front = None
        self.back = None
        self._length: int = 0

        if iterable is None:
            iterable = []

        for value in iterable:
            self.insert(value)

    def __str__(self):
        """ Return the string representation of a queue
        """
        return f'Front: {self.front} | Back: {self.back} | Length: {self._length}'

    def __repr__(self):
        """ Return the queue object in a readable way
        """
        return f'<Stack | Front: {self.front} | Back: {self.back} | Length: {self._length}>'

    def __len__(self):
        """ Returns the length of the queue
        """
        return self._length

    def __iter__(self):
        if self.front:
            self._current = self.head
        return self

    def enqueue(self, val):
        """takes any value as an argument and adds that value to the back of the queue
        """
        self.back = Node(val, self.back)
        self._length += 1

    def dequeue(self):
        """removes & returns the Node at the front of the queue
        """
        old_front = self.front
        self.front = _next
        self._length -= 1
        return old_front

