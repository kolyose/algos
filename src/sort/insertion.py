def sort(array):
    """Implement Insertion sort algorithm.

    Complexity:
      O(n**2)

    Arguments:
      - array - a list to sort

    Returns:
      The sorted list.
    """

    for i in range(1, len(array)):
        j = i - 1
        while j >= 0:
            if array[i] > array[j]:
                break
            else:
                j -= 1
        array.insert(j + 1, array.pop(i))

    return array
