from timeit import default_timer as timer
from random import randint
import sys


# @brief The driver for MergeSort, partitions the array then recusively sorts the left and right subarrays
#
# @param array The array to be worked on
# @param start The index to start a subarray
# @param end   The index to end a subarray
#
# @return A sorted integer array of given size
def MergeSort(array, start, end):
    
    if(start < end):
        # Calculate halfway point of array
        half = int((start + end) / 2) 
        
        # Divide left half of array
        MergeSort(array, start, half)
        
        # Divide right half of array
        MergeSort(array, half + 1, end)
        
        # Merge the two halves
        Merge(array, start, half, end)
        
    return array


# @brief Iteratively merges two sorted arrays
#
# @param array The array to be worked on
# @param start The index to start a merge
# @param half  The index for the half way point of the array
# @param end   The index to end a merge
#
# @return The sorted sub-array from index start to index end
def Merge(array, start, half, end):
    # Calculate the size of each half
    # Plus 1 to accommodate uneven sized arrays
    # Halving an uneven array gives .5, converting to int truncates that
    # Ex. Array size 3, half is 1.5, int truncates to 1
    nLeft = half - start + 1
    nRght = end - half
    
    # Create the arrays and add one for the sentinel values
    lArray = [None]* int((nLeft + 1))
    rArray = [None]* int((nRght + 1))
    
    # Populate the arrays, again plus 1 handles the uneven sizes
    lArray = array[start:half + 1]
    rArray = array[half + 1: end + 1]
    
    # Sentinel values
    lArray.append(sys.maxsize)
    rArray.append(sys.maxsize)
    
    #print('lArray:', lArray, 'rArray', rArray)
    
    lIndex = 0
    rIndex = 0
    
    # Plus 1 ensures if both arrays have size 1, both values get added to array
    for index in range(start, end + 1):
        if(lArray[lIndex] < rArray[rIndex]):
            array[index] = lArray[lIndex]
            lIndex += 1
        else:
            array[index] = rArray[rIndex]
            rIndex += 1
    

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
        array[value] = randint(0, size)
    
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
        inputArray = createArray(2048)
    else:
        # Convert the CL argument from a string list to int list
        inputArray = list(map(int, argv))
        
        # createArray takes an optional - size of array to be created - argument
        #     Default is 1000,
        #inputArray = createArray(inputArray[0])
        
    print("The array of size", len(inputArray), "is:", inputArray)
    
    # Get the execution time of MergeSort
    start = timer()
    sortedArray = MergeSort(inputArray, 0, len(inputArray) - 1)
    end = timer()
    
    print("The MergeSort sorted array is:", sortedArray)
    print("The execution time is", end - start, "seconds.")
    

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])