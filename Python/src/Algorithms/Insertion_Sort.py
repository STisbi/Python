from timeit import default_timer as timer
from random import randint
import sys


# @brief Sorts an array using the insertion sort algorithm
#
# @param array The array to be worked on
#
# @return A sorted integer array
def InsertionSort(array):
    
    # enumerate() for use of index and key
    # Start at the second value and the second index value, otherwise
    #     the first comparison will be the first element to itself
    for index, key in enumerate(array[1:], 1):
        
        # Compare to the key to values before it 
        subIndex = index - 1
        
        # Continue the compare until the start or the compare fails
        while((subIndex >= 0) and (array[subIndex] > key)):
            
            print('Before:   ', array)
            
            # The place in front of the current value is where you put the higher value
            # Because the current position (if the next compare fails) is where the key will go
            array[subIndex + 1] = array[subIndex]
            subIndex -= 1
            
            print('After:    ', array)
        
        array[subIndex + 1] = key
        print('Done:     ', array)         
            
    return array


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
        inputArray = userInput()
        
        # TODO: Get rid of this double call here, and in the else statement
        # createArray takes an optional - size of array to be created - argument
        #     Default is 1000, 
        inputArray = createArray(inputArray[0])
    else:
        # Convert the CL argument from a string list to int list
        inputArray = list(map(int, argv))
        
        # createArray takes an optional - size of array to be created - argument
        #     Default is 1000,
        inputArray = createArray(inputArray[0])
        
    print("The array of size", len(inputArray), "is:", inputArray)
    
    # Get the execution time of MergeSort
    start = timer()
    sortedArray = InsertionSort(inputArray)
    end = timer()
    
    print("The InsertionSort sorted array is:", sortedArray)
    print("The execution time is", end - start, "seconds.")
    

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])