from .animal import Animal


class Animal_Shelter(object):
    def __init__(self):
        """ Create a new shelter and give it some default values
            front = None
            back = None
            length = 0
        """
        self.front = None
        self.back = None
        self._length = 0

    def __str__(self):
        """ Return the string representation of a queue
        """
        return f'Front: {self.front} | Back: {self.back} | Length: {self._length}'

    def __repr__(self):
        """ Return the queue object in a readable way
        """
        return f'<Animal Shelter | Front: {self.front} | Back: {self.back} | Length: {self._length}>'

    def __len__(self):
        """ Returns the length of the queue
        """
        return self._length

    def enqueue(self, type):
        """takes any value as an argument and adds that value to the back of the queue
        """
        new_animal = Animal(type)
        if self.front is None:
            self.front = new_animal
        else:
            get_back = self.front
            while get_back._next:
                get_back = get_back._next
            get_back._next = new_animal
            self.back = get_back._next

        self._length += 1

    def dequeue(self, pref=None):
        """removes & returns the animal at 
            the front of the queue if no pref is given or
            returns the oldest pref if provided
        """
        
        if pref is None:
            try:
                old_front = self.front
                self.front = old_front._next
                self._length -= 1
                # import pdb; pdb.set_trace()
                return old_front
            
            except AttributeError:
                print('The queue is empty')
        
        if pref == 'cat' or pref == 'dog':
            cur_animal = self.front
            if pref == cur_animal.type:
                return self.dequeue()
            
            import pdb; pdb.set_trace()
            while cur_animal.type != pref:
                cur_animal = cur_animal._next
            output = cur_animal
            
        self._length -= 1
        return output
