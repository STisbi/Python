def InsertionSort():
    
    array = [5, 2, 4, 6, 1, 3]
    
    # enumerate() for use of index and key
    # Start at the second value and the second index value 
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
            
    
                
            
    print('Finished: ', array)


#######################################################
#                        MAIN                         #
#######################################################
def main():
    InsertionSort()

if __name__ == "__main__":
    main()