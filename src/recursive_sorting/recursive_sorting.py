# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(0, elements): 
        if ((len(arrA) > 0) and (len(arrB) > 0)): #this is only done if there are values to compare

            if arrA[0] < arrB[0]:
                value = arrA.pop(0)
                merged_arr[i] = value

            elif arrB[0] < arrA[0]: 
                value = arrB.pop(0)
                merged_arr[i] = value

        else: #if one list is empty, see which one it is and put the last values from the remaining list into the merged one.
            if (len(arrA) == 0):
                value = arrB.pop(0)
                merged_arr[i] = value
            else:
                value = arrA.pop(0)
                merged_arr[i] = value
            
    print('merged', merged_arr)
    return merged_arr

merge([1,3,4,7], [2,5,6,8])
# TO-DO: implement the Merge Sort function below USING RECURSION
# base case is an array of size 1
# divide everything up
# sort those
def merge_sort( arr ):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
