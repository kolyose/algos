def search(sorted_array, item): 
  """Implement Binary Search algorithm.

  Arguments:
    - sorted_array - a sorted list to search in
    - item - an element to look for

  Returns:
    The index of the item once it's found in the list, -1 otherwise
  """
  start_index = 0
  end_index = len(sorted_array)
   
  while start_index < end_index:
    index = int((start_index + end_index)/2)
    if item == sorted_array[index]:
      return index

    if item < sorted_array[index]:
      end_index = index
    else:
      start_index = index+1
      
  return -1