def BubbleSort():
    array = [5, 2, 3, 1, 4, 6]
            
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
    
    print('Final: ', array)


#######################################################
#                        MAIN                         #
#######################################################
def main():
    BubbleSort()

if __name__ == "__main__":
    main()