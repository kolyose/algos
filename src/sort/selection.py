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

  for i in range(0, length - 1):
    min_index = i
    for j in range(i+1, length):
      if array[j] < array[min_index]:
        min_index = j
    
    if min_index != i:
      temp = array[i]
      array[i] = array[min_index]
      array[min_index] = temp

  return array

