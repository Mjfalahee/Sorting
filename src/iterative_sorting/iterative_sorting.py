# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # print(arr)
    for i in range(0, len(arr) - 1):
        cur_index = i
        # print('Current Index', cur_index)
        # print('Current Element', arr[cur_index])
        smallest_index = cur_index
        # print('Smallest Index', smallest_index)
        # print('Smallest Element', arr[smallest_index])
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                # print('conditional index', smallest_index)
                # print('conditional element', arr[smallest_index])

        # TO-DO: swap

        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        # print(arr)




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    nosorts = False
    # print(arr)
    while nosorts != True:
        nosorts = True
        for i in range(0, len(arr)-1):
            if (arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # print(arr)
                nosorts = False
                # print('No Sorts', nosorts)
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr