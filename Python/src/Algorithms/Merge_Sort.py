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
    lArray.append(999)
    rArray.append(999)
    
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
    


#######################################################
#                        MAIN                         #
#######################################################
def main():
    print('Original:', gArray)
    print('Sorted:  ', MergeSort(gArray, 0, len(gArray) - 1))

if __name__ == "__main__":
    main()