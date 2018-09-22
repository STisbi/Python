from timeit import default_timer as timer
from random import randint
import sys

gArray = [5, 4, 2, 6, 1, 3, 7]

def MergeSort(aArray, start, end):
    
    if(start < end):
        # Calculate halfway point of array
        half = int((start + end) / 2) 
        
        # Divide left half of array
        MergeSort(aArray, start, half)
        
        # Divide right half of array
        MergeSort(aArray, half + 1, end)
        
        # Merge the two halves
        Merge(aArray, start, half, end)
        
    return aArray


def Merge(aArray, start, half, end):
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
    lArray = aArray[start:half + 1]
    rArray = aArray[half + 1: end + 1]
    
    # Sentinel values
    lArray.append(sys.maxsize)
    rArray.append(sys.maxsize)
    
    #print('lArray:', lArray, 'rArray', rArray)
    
    lIndex = 0
    rIndex = 0
    
    # Plus 1 ensures if both arrays have size 1, both values get added to aArray
    for index in range(start, end + 1):
        if(lArray[lIndex] < rArray[rIndex]):
            aArray[index] = lArray[lIndex]
            lIndex += 1
        else:
            aArray[index] = rArray[rIndex]
            rIndex += 1
    
def createArray():
    limit = 1500
    
    array = [None]*limit
    
    for value in range(0, limit):
        array[value] = randint(0, limit)
    
    return array


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
        inputArray = createArray()
    else:
        inputArray = list(map(int, argv))
        inputArray = createArray()
    
    # Get the execution time
    start = timer()
    
    # The array with 1000, 1500, or 2000 elements 
    inputArray = createArray()
    
    print("The array of size", len(inputArray), "is:    ", inputArray)
    
    # Call MergeSort and print the sorted array
    print("The MergeSort sorted array is:", MergeSort(inputArray, 0, len(inputArray) - 1))
    end = timer()
    
    print("The execution time is", end - start, "seconds.")
    

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])