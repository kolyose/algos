def sort(array):
    """Implement Bubble Sort algorithm.

    Arguments:
      - array - a list to sort

    Returns:
      The sorted list
    """
    for i in range(len(array) - 1, 0, -1):
        has_value_bubbled = False
        j = 0
        while j < i:
            if array[j] > array[j + 1]:
                has_value_bubbled = True
                array[j], array[j + 1] = array[j + 1], array[j]
            j += 1

        if not has_value_bubbled:
            break

    return array
