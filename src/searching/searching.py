# STRETCH: implement Linear Search				
def linear_search(arr, target):
  # TO-DO: add missing code
  # print('Target', target)
  # print(arr)
  target_position = None

  for i in range(0, len(arr)):
    # print('arr[i]', arr[i])
    if arr[i] == target:
    #   print('Target found', arr[i], i)
      target_position = i

  if target_position:
    # print('Returning', target_position)
    return target_position
  else:
    # print('Not Found')
    return -1

# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0 
  high = len(arr)-1

  # TO-DO: add missing code

  while low <= high:
    middle = (low+high)//2
    # print('Middle is now: ', middle)

    if (arr[middle] == target):
      # print('Target found: ', middle)
      return middle

    elif arr[middle] < target:
        low = middle + 1
        # print('Low is now: ', low)

    else:
        high = middle - 1
        # print('High is now: ', high)

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls

  if (high >= low): 
    if (arr[middle] == target):
      return middle
    
    elif arr[middle] < target:
      return binary_search_recursive(arr, target, middle+1, high)

    else:
      return binary_search_recursive(arr, target, low, middle-1)
  else:
    return -1
    

