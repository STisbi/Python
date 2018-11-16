import sys
from collections import OrderedDict

global x
global y

# Increases the maximum recursion size
#sys.setrecursionlimit(5000)

def LRS(str1, str2):
    #print("Debug:", "String 1:", str1)
    #print("Debug:", "String 2:", str2) 
    
    # Length of string will be length of row and column in table
    # Plus 1 for the 0 values
    x = len(str1) + 1
    y = len(str2) + 1
    
    # Initialize the table to None
    table = [[None]*(x) for i in range(y)] 
    
    
    # Fill the first row and column with 0's
    '''for i in range(0, y):
        for j in range(0, x):
            if(i == 0 or j == 0):
                table[i][j] = 0'''
    
    #printTable(table, x, y)
    
    # Create the table, think y vs x axis, y is left side, x is across the top
    for i in range(0, y):
        for j in range(0, x):
            # Fill the first row and column with 0's
            if(i == 0 or j == 0):
                table[i][j] = 0
            # Ignore the first row and column
            if(i != 0) and (j != 0):
                # Compare the individual characters
                # The i != j takes care of matching indices
                if(str2[i - 1] == str1[j - 1] and i != j):
                    # Diagonal top left
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    # Greater of left or top value
                    table[i][j] = max(table[i][j - 1], table[i - 1][j])
    
    printTable(table, x, y)
    
    LCS = ""

    # The for loop has issues because it automatically decrements
    '''# Start at the bottom right of the table
    for i in range(y - 1, -1, -1):
        for j in range(x - 1, -1, -1):
            print(table[i][j], str2[i - 1], str1[j - 1], i, j)
            # Stop when the value of a cell is 0
            if(table[i][j] == 0):
                return LCS
            # If cell value is not equal to the cell to the top or to the left
            # that character is part of the LCS
            if(table[i][j] != max(table[i][j - 1], table[i - 1][j])):
                LCS = str1[j - 1] + LCS
                print(table[i][j], table[i][j - 1], table[i - 1][j], i, j, LCS)
                # Decrement the counts
                i -= 1
                j -= 1
                # Check if the new cell location is 0
                if(table[i][j] == 0):
                    return LCS
                print(i, j)
                
                
            # If the cell value came from the left, go left
            if(table[i][j] == table[i][j - 1]):
                print("left", table[i][j - 1])
                j -= 1
                continue
            # If the cell value came from the top, go up
            if(table[i][j] == table[i - 1][j]):
                print("up", table[i - 1][j])
                break'''
    i = y - 1
    j = x - 1
    
    # While loop used instead because i and j decrements actually hold
    while i != 0:
        while j != 0:
            print(table[i][j], str2[i - 1], str1[j - 1], i, j)
            # Stop when the value of a cell is 0
            if(table[i][j] == 0):
                return LCS
            # If cell value is not equal to the cell to the top or to the left
            # that character is part of the LCS
            if(table[i][j] != max(table[i][j - 1], table[i - 1][j])):
                LCS = str1[j - 1] + LCS
                print(table[i][j], table[i][j - 1], table[i - 1][j], i, j, LCS)
                # Decrement the counts
                i -= 1
                j -= 1
                # Check if the new cell location is 0
                if(table[i][j] == 0):
                    return LCS
                print(i, j)
            # If the cell value came from the left, go left
            if(table[i][j] == table[i][j - 1]):
                print("left", table[i][j - 1])
                j -= 1
                continue
            # If the cell value came from the top, go up
            if(table[i][j] == table[i - 1][j]):
                print("up", table[i - 1][j])
                i -= 1
                break                    
    
    return LCS


def printLRS(str, X):
    for index, value in enumerate(str):
        for subindex, subvalue in enumerate(str[index + 1:]):
            if value == subvalue:
                print(value, end="")

    print()
    
def LRSBruteForce(str1, str2, len1, len2): 
    if (len1 == 0) or (len2 == 0): 
        return 0
    if (str1[len1-1] == str2[len2-1]) and (len1 != len2): 
        global x
        x = str1[len1-1] + x
        return 1 + LRSBruteForce(str1, str2, len1-1, len2-1)
    else: 
        return max(LRSBruteForce(str1, str2, len1, len2-1), LRSBruteForce(str1, str2, len1-1, len2))
    '''if (x == 0) or (y == 0):
        return 0
    if (x > 0) and (y > 0) and (str1[x] == str2[y]):
        return LRSBruteForce(str1, str2, len(str1) - 1, len(str2) - 1) + 1
    if (x > 0) and (y > 0) and (str1[x] != str2[y]):
        return max(LRSBruteForce(str1, str2, len(str1) - 1, len(str2)), 
                   LRSBruteForce(str1, str2, len(str1), len(str2) - 1))'''



def printTable(table, x, y):
    print("Debug:", "printTable x =", x, "y = ", y)
    for i in range(0, y):
        for j in range(0, x):
            print(table[i][j], " ", end='')
        print()

def main(argv):
    global x
    x = ""
    
    if(not argv):
        lrsInput = "sethtisbi"
    else:
        # argv is a string list
        lrsInput = argv[0]
    
    # Like LCS but here the string is both x and y columns
    #lrs = LRS(lrsInput, lrsInput)
    lrs = LRSBruteForce(lrsInput, lrsInput, len(lrsInput), len(lrsInput))
    
    print(x)
    # Removes duplicates from the total
    print("".join(OrderedDict.fromkeys(x)))

    print("The longest repeated subsequence of", lrsInput, "is", lrs)
    

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])