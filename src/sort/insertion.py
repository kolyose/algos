def sort(array):
  """Implement Insertion sort algorithm.
  
  Complexity:
    O(n**2)

  Arguments:
    - array - a list to sort

  Returns:
    The sorted list.
  """
  result = array[0:1]
  
  for i in range(1, len(array)):
    inserted = False
    for j in range(0,len(result)):
      if array[i] <= result[j]:
        result.insert(j, array[i])
        inserted = True
        break
    
    if not inserted:
      result.append(array[i])

  return result