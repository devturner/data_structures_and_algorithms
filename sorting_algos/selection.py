

def selection_sort(to_sort):
    for i in range(len(to_sort)):
        lowest_position = i
        for j in range(i + 1, len(to_sort)):
            if to_sort[lowest_position] > to_sort[j]:
                lowest_position = j
        to_sort[i], to_sort[lowest_position] = to_sort[lowest_position], to_sort[i]
    return to_sort
