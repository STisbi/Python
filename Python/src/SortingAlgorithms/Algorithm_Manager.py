from random import randint
import sys

from Algorithms.Sort import Sort

class Algorithm_Manager():
    

    
    # @brief Creates an unsorted array of given size.
    #
    # @param size An optional parameter that specifies the size of the array
    #
    # @return An unsorted integer array of given size
    def createArray(self, size = 10000):
        # The Numpy library can create a random array of size x in one line
        #    but it doesn't come installed with python
        
        # Initialize the array
        array = [None]*size
        
        # Fill it with random integers from 0 to size
        for value in range(0, size):
            array[value] = randint(0, size)
            #array[value] = size - value
        
        return array
    
    
    # @brief Gets the size for an array from the user
    #
    # @return The size of the array to be created by the user
    def userInput(self):
        # Get the array as input from the user
        #inputArray = [int(x) for x in input().split()]
        size = int(input("Input as an integer, the size of the unsorted array to create: "))
        
        return size


#######################################################
#                        MAIN                         #
#######################################################
def main(argv):
    algMgr = Algorithm_Manager()
    
    if(not argv):
        # createArray takes an optional - size of array to be created - argument
        #     Default is 1000, 
        inputArray = algMgr.createArray(algMgr.userInput())
    else:
        # createArray takes an optional - size of array to be created - argument
        #     Default is 1000,
        inputArray = algMgr.createArray(int(argv[0]))
        
    algorithm = Sort()
    sortedArray = algorithm.sort("Insertion Sort", inputArray)
        
    print("The array of size", len(inputArray), "is:", inputArray)
    
    print("The sorted array is:", sortedArray)

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])