def sort(array):
    """Implement selection sort algorithm.

    Complexity:
      O(n**2)

    Arguments:
      - array - a list to sort

    Returns:
      The sorted list.
    """
    length = len(array)

    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array
