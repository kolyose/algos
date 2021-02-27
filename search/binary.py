

def search(array, item): 
  startIndex = 0
  length = len(array)
   
  while length > 0:
    index = startIndex + int(length/2)
    if item == array[index]:
      return index

    if item < array[index]:
      length = index - startIndex
    else:
      startIndex = index+1
      length = length - startIndex

  return -1