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
            
    return merged_arr

# print(merge([0,2,4,6], [1,3,5,7]))
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # print(arr)
    length = len(arr)
    #base-case len(arr) <= 1
    if len(arr) <= 1:
        return arr
    else:
        first_half = arr[:length//2]
        second_half = arr[length//2:]

        arr1 = merge_sort(first_half)
        arr2 = merge_sort(second_half)

        return merge(arr1, arr2)

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
