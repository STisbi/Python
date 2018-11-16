from timeit import default_timer as timer
from random import randint
import sys


# @brief Delegates to the bubble sort algorithm of choice
#
# @param array The array to be worked on
#
# @return A sorted integer array
def BubbleSort(array):
    
    BubbleSortBook(array)
    #BubbleSortOriginal(array)
    
    return array


# @brief The version of bubble sort from the algorithms book
#
# @param array The array to be worked on
#
# @return A sorted integer array
def BubbleSortBook(array):
    
    for i in range(0, len(array)):
        for j in range (len(array) - 1, i, -1):
            
            print('i:', i, 'j:', j, array)
            print('Comparing:', array[j], '<', array[j-1])
            
            if array[j] < array [j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                
    return array


# @brief A naive version of bubble sort
#
# @param array The array to be worked on
#
# @return A sorted integer array
def BubbleSortOriginal(array):
    
    index = 0
    skipped = 0
    
    while True:
        print('Before:', array)
        
        # If true, swap the values
        if(array[index] > array[index + 1]):
            temp = array[index + 1]
            array[index + 1] = array[index]
            array[index] = temp
        else:
            skipped += 1 
            
        print('After: ', array)
        
        index += 1
        
        # Once we've reached the end, check for a sorted array
        if(index == len(array) - 1):
            # If we've skipped all the values in the array, it must be sorted
            if(skipped == len(array) - 1):
                break
            # Otherwise, reset the index and the skipped counts
            else:
                skipped = 0
                index = 0
    
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
    sortedArray = BubbleSort(inputArray)
    end = timer()
    
    print("The BubbleSort sorted array is:", sortedArray)
    print("The execution time is", end - start, "seconds.")
    

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])