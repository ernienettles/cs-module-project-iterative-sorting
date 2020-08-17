# TO-DO: Complete the selection_sort() function below
def selection_sort(array):
    # Outer loops that represents each passthrough of selection sort
    for i in range(0, len(array) - 1):
        cur_index = i + 1
        # Keep track of the index containing the lowest value we encounter
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # Inner loop that starts at i + 1
        for cur_index in range(0, len(array) - 1):
            # Checks each element of the array that has not yet been sorted and looks 
            # for the lowest number it found so far in the smallest_index variable
            if array[cur_index] < array[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here

        # Checks to see if the lowest number is already in it's correct place
        if smallest_index != i:
            temp = array[i]
            array[i] = array[smallest_index]
            array[smallest_index] = temp
    return array


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here


    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
