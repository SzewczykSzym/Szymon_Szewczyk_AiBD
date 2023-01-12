from copy import copy

def bubble_sort(arr):
    copy_arr = copy(arr)
    # copy not to change entered array
    n = len(copy_arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if copy_arr[j] > copy_arr[j + 1]:
                swapped = True
                copy_arr[j], copy_arr[j + 1] = copy_arr[j + 1], copy_arr[j]
        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return copy_arr
    return copy_arr