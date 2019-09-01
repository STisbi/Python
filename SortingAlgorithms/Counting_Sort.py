from timeit import default_timer as timer
from random import randint
import sys


# @brief Algorithm for counting sort
#
# @param inputArray The array to be sorted
# @param max The range of numbers in which the array varies from
#
# @return A sorted array
def CountingSort(inputArray, maxValue):
    # This will be the returned array
    sortedArray = [0]*len(inputArray)
    
    # The array holds the total count for values
    countArray = [0] * maxValue
    
    # Fill the array of total values
    for value in inputArray:
        # Minus 1 because 0 based
        countArray[value] += 1
        
    # Sum each position using previous values
    for index in range(1, len(countArray)):
        countArray[index] += countArray[index - 1]
    
    # Sort the array
    for value in inputArray:
        if(countArray[value] != 0):
            # -1 because 0 based
            sortedArray[countArray[value] - 1] = value
            countArray[value] -= 1
    

    return sortedArray
    

# @brief Creates an unsorted inputArray of given size.
#
# @param size An optional parameter that specifies the size of the inputArray
#
# @return An unsorted integer inputArray of given size    
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
        inputArray = createArray(100)
    else:
        # Convert the CL argument from a string list to int list
        inputArray = list(map(int, argv))
        
        # createArray takes an optional - size of array to be created - argument
        #     Default is 1000,
        #inputArray = createArray(inputArray[0])
        
    print("The array of size", len(inputArray), "is:", inputArray)
    
    # Get the execution time of MergeSort
    start = timer()
    # The second parameter does not truly depend on the array length
    #    as the range of values in the array can be from 0 to 100
    #    Ex: [0, 100, 2]
    sortedArray = CountingSort(inputArray, len(inputArray) + 1)
    end = timer()
    
    print("The CoutingSort sorted array is:", sortedArray)
    print("The execution time is", end - start, "seconds.")
    

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])