
def quicksort(unsorted, start, end):
    """ Quicksort, take in an unsorted list, and with the helper, sort that list and return it
    """
    if start < end:
        pivot = partition(unsorted, start, end)

        quicksort(unsorted, start, pivot - 1)
        quicksort(unsorted, pivot + 1, end)

    return unsorted


def partition(unsorted, start, end):
    """ Helper function for quick sort
    """
    sorted = False
    pivot = unsorted[start]
    left = start + 1
    right = end

    while not sorted:
        while left <= right and unsorted[left] <= pivot:
            left += 1
        while unsorted[right] >= pivot and right >= left:
            right -= 1

        if right < left:
            sorted = True
        else:
            left_list_temp = unsorted[left]
            unsorted[left] = unsorted[right]
            unsorted[right] = left_list_temp

    left_list_temp = unsorted[start]
    unsorted[start] = unsorted[right]
    unsorted[right] = left_list_temp

    return right
