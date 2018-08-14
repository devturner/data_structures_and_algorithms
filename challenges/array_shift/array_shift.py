def insert_shift_array(input_list, element):
    if (len(input_list) % 2) == 0:
        mid = (len(input_list) // 2)
    else:
         mid = (len(input_list) // 2) + 1

    new_list = []
    counter_old = 0
    
    while counter_old < len(input_list):
        if counter_old == mid:
            new_list  += [element]
            mid = -1
        else:
            new_list  += [input_list[counter_old]]
            counter_old += 1
    return new_list
    


# test = [4,8,15,23,42]
# element = 7
# print([4,8,15,7,23,42])
# insert_shift_array(test, element)