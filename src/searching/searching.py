def linear_search(arr, target):
    for i, n in enumerate(arr):
        if n == target:
            return i
    return -1


# Write an iterative implementation of Binary Search
import math

def binary_search(arr, target):
    lower = 0
    upper = len(arr) - 1
    while lower <= upper:
        mid = int(math.floor((upper + lower) / 2))
        if target < arr[mid]:
            upper = mid - 1
        elif target > arr[mid]:
            lower = mid + 1
        elif target == arr[mid]:
            return mid


    return -1  # not found
