import sys

# Nearly all functions use this
global edgeWeights


# @brief The main algorithm for finding the shortest path
#
# @return The shortest path
def Dijkstra():
    vertexList = CreateVertexList()
    adjMatrix  = CreateAdjacencyMatrix(vertexList)
    
    PrintAdjacenyMatrix(adjMatrix)


# @brief Creates the adjaceny matrix
#
# @return The adjacency matrix
def CreateAdjacencyMatrix(vertexList):
    # Create the NxN matrix, with N = length of vertexList
    adjMatrix = [[0]*(len(vertexList)) for i in range(len(vertexList))]
    
    # Iterate row by row
    for index, head in enumerate(vertexList):
        # Iterate column by column
        for subindex, tail in enumerate(vertexList):
            # Self loops are not allowed
            if index != subindex:
                if(CheckEdgeExists(head, tail)):
                    adjMatrix[index][subindex] = GetEdgeWeight(head, tail)
                    
    return adjMatrix


# @brief Print the adjacency matrix
def PrintAdjacenyMatrix(adjMatrix):  
    for row in adjMatrix:
        print(row)


# @brief Creates a list of all unique vertices in the graph
#
# @return A list of all vertices in the graph
def CreateVertexList():
    # Empty list to hold unique vertices
    vertexList = []
    
    for edge in edgeWeights:
        # The last element is the weight
        for vertex in edge[:-1]:
            # Append only unique vertices
            if vertex not in vertexList:
                vertexList.append(vertex)
                
    #DEBUG print("Vertex List:", vertexList)
    
    return vertexList
    

# @brief Checks if the specified edge exists
#
# @param head The head of the edge
# @param tail The tail of the edge
#
# @return True if the edge exists
def CheckEdgeExists(head, tail):
    exists = False
    
    # Check every edge
    for edge in edgeWeights:
        # Parentheses are needed
        if (head in edge) and (tail in edge):
            exists = True
            break
            
    return exists 


# @brief Gets the weight of the edge specified
#
# @param head The head of the edge
# @param tail The tail of the edge
#
# @return The weight of the edge
def GetEdgeWeight(head, tail): 
    # Check every edge  
    for edge in edgeWeights:
        # Parentheses are needed
        if (head in edge) and (tail in edge):
            # Element 3 is the weight
            return edge[2]


# @brief Gets an array from the user
#
# @return An integer array specified by the user
def UserInput():
    print("Enter edge as VERTEX VERTEX WEIGHT; with a space between each character.")
    print("Example: A B 1")
    print("Press enter after entering an edge. Enter as many edges as desired.")
    print("Enter \"done\" when finished entering edges.")
    

    #inputArray = [int(x) for x in input().split()]
    
    #return inputArray


#######################################################
#                        MAIN                         #
#######################################################
def main(argv):
    global edgeWeights
    
    if(not argv):
        UserInput()
        edgeWeights = [[ 97,  98, 1],
                       [ 97,  99, 6],
                       [ 98, 100, 2],
                       [ 98, 101, 7],
                       [ 99, 101, 1],
                       [100, 101, 1]]
    else:
        # 97 is ascii for 'a'
        edgeWeights = [[ 97,  98, 1],
                       [ 97,  99, 6],
                       [ 98, 100, 2],
                       [ 98, 101, 7],
                       [ 99, 101, 1],
                       [100, 101, 1]]
    
    #DEBUG print("Edge Weights:", edgeWeights)
        
    Dijkstra()
    

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])