def partition(array, start, end):
    partition_index = start

    for i in range(start + 1, end + 1):
        if array[i] < array[partition_index]:
            array.insert(partition_index, array.pop(i))
            partition_index += 1

    return partition_index


def sort(array, start=0, end=None):
    """Implement Quick sort algorithm (Lomuto partition scheme).

    Complexity:
      O(n * log(n))

    Arguments:
      - array - a list to sort
      - start - starting index within the array. If not specified the first index is going to be used.
      - end - ending index within the array. If not specified the last index is going to be used.

    Returns:
      The sorted list.
    """

    if end is None:
        end = len(array) - 1

    if start < end:
        partition_index = partition(array, start, end)
        sort(array, start, partition_index - 1)
        sort(array, partition_index + 1, end)

    return array
