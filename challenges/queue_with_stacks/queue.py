from .node import Node
from .stack import Stack


class Queue(object):
    def __init__(self):
        """ Create a new queue and give it some default values
            length = 0
            optionally, accept an iterable and create new nodes for them
        """
        self._length: int = 0
        self.stack_1 = Stack()
        self.stack_2 = Stack()



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
        """takes any value as an argument and adds that value to the back of the queue via a stacks push
        """
        self.stack_1.push(value)
        self._length += 1

    def dequeue(self):
        """removes & returns the Node at the front of the queue via a stacks pop
        """
        if not self.stack_1._length == 0:
            while self.stack_1._length > 0:
                self.stack_2.push(self.stack_1.pop())
            
            front = self.stack_2.pop()
            self._length -= 1
            
            while self.stack_2._length > 0:
                self.stack_1.push(self.stack_2.pop())
            
            return front
