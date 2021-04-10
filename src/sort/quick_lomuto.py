from src.sort.util import swap

def partition(array, start, end):
  pivot = array[end]
  swap_index = start

  for i in range(start, end+1):
    if array[i] < pivot:
      swap(array, i, swap_index)
      swap_index += 1
  
  swap(array, swap_index, end)
  return swap_index

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

  if end == None:
    end = len(array) - 1

  if start >= end:
    return array


  partition_index = partition(array, start, end)
  sort(array, start, partition_index-1)
  sort(array, partition_index+1, end)

  return array
