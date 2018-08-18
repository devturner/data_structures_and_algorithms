# given [1,2,3,4,5] 7 find the index or return -1

def find_binary_index(list, key):
    low = 0
    high = len(list) - 1
    mid = get_mid(low, high)
    while low <= high:
        if list[high] == key:
            return(high)
        elif list[low] == key:
            return(low)
        elif list[mid] > key:
            high = mid - 1
            mid = get_mid(low, high)
        elif list[mid] < key:
            low = mid + 1
            mid = get_mid(low, high)
        elif list[mid] == key:
            return mid
    
    return -1


def get_mid(low, high):
    mid = (low + high) // 2
    return mid
