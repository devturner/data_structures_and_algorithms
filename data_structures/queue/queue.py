from .node import Node


class Queue(object):
    def __init__(self, iterable=None):
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

    def enqueue(self, value):
        """takes any value as an argument and adds that value to the back of the queue
        """
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
        else:
            get_back = self.front
            while get_back._next:
                get_back = get_back._next
            get_back._next = new_node
            self.back = get_back._next

        self._length += 1

    def dequeue(self):
        """removes & returns the Node at the front of the queue
        """
        try:
            old_front = self.front
            self.front = old_front._next
            self._length -= 1
            return old_front
        except AttributeError:
            print('The queue is empty')
