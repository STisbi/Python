from timeit import default_timer as timer
from random import randint
import sys


def HeapSort(array):
    
    BuildMaxHeap(array)
    
    return array


def BuildMaxHeap(array):
    
    length = len(array)
    
    for index in range(length, -1, -1):
        print("BuildMaxHeap: MaxHeapfiy:    ", array, length, index)
        MaxHeapify(array, length, index)
    
    for index in range(length - 1, 0, -1):
        print("Extract Before:              ", array[index], array[0])
        array[index], array[0] = array[0], array[index]
        print("Extract After:               ", array[index], array[0])
        
        print("BuildMaxHeap: MaxHeapify:    ", array, index, 0)
        MaxHeapify(array, index, 0)
    
    return array


def MaxHeapify(array, length, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    
    print("MaxHeapify: Start:           ", array, length, index)
    
    print("Compare: Left:               ", left, length, index, left)
    if (left < length) and (array[index] < array[left]):
        print("Largest = Left:              ", largest, left)
        largest = left
    
    print("Compare: Right:              ", right, length, largest, right)    
    if (right < length) and (array[largest] < array[right]):
        print("Largest = Right:             ", largest, right)
        largest = right
        
    print("Compare: largest:            ", largest, index)
    if (largest != index):
        print("Swap:                        ", array[index], array[largest])
        array[index], array[largest] = array[largest], array[index]
        
        print("MaxHeapify: Middle:          ", array, length, largest)
        
        MaxHeapify(array, length, largest)
    
    
    print("MaxHeapify: End:             ", array)
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
        #array[value] = size - value
    
    return [12, 11, 13, 5, 6, 7]


# @brief Gets an array from the user
#
# @return An integer array specified by the user
def userInput():
    
    size = int(input("Enter the size of the unsorted array to create: "))
    
    return size


#######################################################
#                        MAIN                         #
#######################################################
def main(argv):
    if(not argv):

        inputArray = createArray(userInput())
    else:
        # createArray takes an optional - size of array to be created - argument
        #     Default is 1000,
        inputArray = createArray(int(argv[0]))
        
    print("The array of size", len(inputArray), "is:", inputArray)
    
    # Get the execution time of QuickSort
    start = timer()
    sortedArray = HeapSort(inputArray)
    end = timer()
    
    print("The HeapSort sorted array is:", sortedArray)
    print("The execution time is", end - start, "seconds.")
    

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])