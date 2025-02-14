def merge_sorted(arr_i, arr_j):
    result = []
    i = 0
    j = 0

    while i < len(arr_i) and j < len(arr_j):
        if arr_i[i] > arr_j[j]:
            result.append(arr_j[j])
            j += 1
        else:
            result.append(arr_i[i])
            i += 1

    rest = [*arr_i[i:], *arr_j[j:]]
    result.extend(rest)

    return result


from math import floor


def sort(array):
    """Implement Merge sort algorithm.

    Complexity:
      O(n * log(n))

    Arguments:
      - array - a list to sort

    Returns:
      The sorted list.
    """
    length = len(array)
    if length < 2:
        return array

    middle_index = floor(length / 2)

    left = sort(array[0:middle_index])
    right = sort(array[middle_index:])

    return merge_sorted(left, right)
