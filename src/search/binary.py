def search(sorted_array, item): 
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