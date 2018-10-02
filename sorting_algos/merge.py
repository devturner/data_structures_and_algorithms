
def merge_sort(unsorted):
    """ Recursive method to break unsorted list down into individual lists
    """
    if len(unsorted) <= 1:
        return unsorted

    split = len(unsorted) // 2
    left = merge_sort(unsorted[:split])
    right = merge_sort(unsorted[split:])

    return merge_sort_two(left, right)


def merge_sort_two(left, right):
    """ Sorts the unsorted parts and puts them back together in a new resutled list (sorted)
    """
    result = []
    while len(left) is not 0 and len(right) is not 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])

    if len(left) == 0:
        result += right

    if len(right) == 0:
        result += left

    return result
