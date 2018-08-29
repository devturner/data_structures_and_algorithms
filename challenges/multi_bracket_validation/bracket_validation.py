from .stack import Stack


def multi_braket_validation(in_string):
    openings = ['[', '(', '{']
    closings = [']', ')', '}']
    stack = Stack()

    for i in range(len(in_string)):
        print(in_string[i])
        if in_string[i] in openings:
            # import pdb; pdb.set_trace()
            stack.push(in_string[i])
            if in_string[i] in closings:
                if len(stack) == 0:
                    return False
                elif openings[closings.index(in_string[i])] != stack.top.val:
                    return False
                else:
                    stack.pop()
    # import pdb; pdb.set_trace()

    if len(stack) > 0:    
        return False
    
    return True
        