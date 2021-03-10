def sort(array):
  """Implement Bubble Sort algorithm.

    Arguments:
      - array - a list to sort

    Returns:
      The sorted list
  """
  for i in range(len(array)-1, 0, -1):
    j = 0
    has_value_bubbled = False
    
    while j < i:
      if array[j] > array[j+1]:
        has_value_bubbled = True
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
      j+=1
    
    if not has_value_bubbled:
      break
  
  return array