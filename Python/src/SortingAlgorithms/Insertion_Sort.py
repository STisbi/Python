from Algorithms import Sort

class InsertionSort(Sort):
    
    
    def __init__(self):
        print("Insertion Sort")
    
    
    # @brief Sorts an array using the insertion sort algorithm
    #
    # @param array The array to be worked on
    #
    # @return A sorted integer array
    def sort(self, algorithm, array):
        print("implementation", algorithm)
        
        # enumerate() for use of index and key
        # Start at the second value and the second index value, otherwise
        #     the first comparison will be the first element to itself
        for index, key in enumerate(array[1:], 1):
            
            # Compare to the key to values before it 
            subIndex = index - 1
            
            # Continue the compare until the start or the compare fails
            while((subIndex >= 0) and (array[subIndex] > key)):
                
                #print('Before:   ', array)
                
                # The place in front of the current value is where you put the higher value
                # Because the current position (if the next compare fails) is where the key will go
                array[subIndex + 1] = array[subIndex]
                subIndex -= 1
                
                #print('After:    ', array)
            
            array[subIndex + 1] = key
            #print('Done:     ', array)         
                
        print( array)
    
