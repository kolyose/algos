
def merge(arr_i, arr_j):
  result = []
  i=0
  j=0
  len_i = len(arr_i)
  len_j = len(arr_j)

  while True:
    if i == len_i:
      result.extend(arr_j[j:])
      return result
    
    if j == len_j:
      result.extend(arr_i[i:])
      return result

    if arr_i[i] > arr_j[j]:
      result.append(arr_j[j])
      j+=1
    else:
      result.append(arr_i[i])
      i+=1


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
  if (length < 2): 
    return array

  middle_index = floor(length/2)
  
  left = sort(array[0:middle_index])
  right = sort(array[middle_index:])
  
  return merge(left, right)
