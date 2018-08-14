def insert_shift_array(input_list, element):
    mid = (len(arr) // 2) - 1
    new_list = []
    counter_new = 0
    counter_old = 0
	while counter_old < len(arr):
		if counter_old == mid:
			new_list[counter_new] = element
            mid = -1
            counter_new += 1
        else:
            new_list[counter_new] = counter_old
            counter_new += 1
            counter_old += 1
    return new_list
    print(new_list)


test = [1, 2, 3]
element = 7

insert_shift_array(test, element)