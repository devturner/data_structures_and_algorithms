class Animal(object):
    def __init__(self, type, _next=None):
        """ Make a new Animal
        """
        self.type = type
        self._next = _next

    def __str__(self):
        """ Return the string representation of a nodes value
        """
        return f'{self.type}'

    def __repr__(self):
        """ Return the node object in a readable way
        """
        return f'<Node | type: {self.type} | Next: {self._next}>'
