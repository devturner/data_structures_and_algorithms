from .stack import Stack


def multi_braket_validation(in_string):
    """ Validates that the string, if contianing brakets closes them correctly. 
        Input: string
        Output: Boolean
    """
    openings = ['[', '(', '{']
    closings = [']', ')', '}']
    stack = Stack()
    for i in range(len(in_string)):
        if in_string[i] in openings:
            stack.push(in_string[i])
        if in_string[i] in closings:
            if len(stack) == 0:
                return False
            elif openings[closings.index(in_string[i])] != stack.top.val:
                return False
            else:
                stack.pop()
    if len(stack) > 0:    
        return False
    
    return True
        