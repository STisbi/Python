from timeit import default_timer as timer
from random import randint
import sys


# @brief The driver for QuickSort, partitions the array then recusively sorts the left and right subarrays
#
# @param array The array to be worked on
# @param start The index to start a subarray
# @param end   The index to end a subarray
#
# @return A sorted integer array of given size
def QuickSort(array, start, end):
    
    if(start < end):
        # Get the half way point
        half = Partition(array, start, end)
        
        # Sort the left array
        QuickSort(array, start, half - 1)
        
        # Sort the right array
        QuickSort(array, half + 1, end)
        
    return array


# @brief Iteratively swaps two elements compared to a pivot element
#
# @param array The array to be worked on
# @param start The index to start the swap
# @param end   The index to end the swap
#
# @return An semi-sorted array with elements greater than the pivot the right of it and elements less than the pivot to the left of it
def Partition(array, start, end):
    pivot = array[end]
    left = start - 1
    
    for right in range(start, end):
        if(array[right] <= pivot):
            left += 1
            
            # Swap elements            
            array[left], array[right] = array[right], array[left]
    
    # Swap with the pivot, now between both halves
    array[left + 1], array[end] = array[end], array[left + 1]
    
    return (left + 1)


# @brief Creates an unsorted array of given size.
#
# @param size An optional parameter that specifies the size of the array
#
# @return An unsorted integer array of given size
def createArray(size = 10000):
    # The Numpy library can create a random array of size x in one line
    #    but it doesn't come installed with python
    
    # Initialize the array
    array = [None]*size
    
    # Fill it with random integers from 0 to size
    for value in range(0, size):
        #array[value] = randint(0, size)
        array[value] = size - value
    
    return array


# @brief Gets an array from the user
#
# @return An integer array specified by the user
def userInput():
    print("Input integers individually all on one line without comma's then press enter. Ex: 5 1 3 23 4 543 0 2")
    
    # Get the array as input from the user
    inputArray = [int(x) for x in input().split()]
    
    return inputArray


#######################################################
#                        MAIN                         #
#######################################################
def main(argv):
    if(not argv):
        #inputArray = userInput()
        
        # TODO: Get rid of this double call here, and in the else statement
        # createArray takes an optional - size of array to be created - argument
        #     Default is 1000, 
        inputArray = createArray(1000)
    else:
        # Convert the CL argument from a string list to int list
        inputArray = list(map(int, argv))
        
        # createArray takes an optional - size of array to be created - argument
        #     Default is 1000,
        inputArray = createArray(inputArray[0])
        
    print("The array of size", len(inputArray), "is:", inputArray)
    
    # Get the execution time of QuickSort
    start = timer()
    sortedArray = QuickSort(inputArray, 0, len(inputArray) - 1)
    end = timer()
    
    print("The QuickSort sorted array is:", sortedArray)
    print("The execution time is", end - start, "seconds.")
    

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])