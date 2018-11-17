import sys

# Nearly all functions use this
global edgeWeights


# @brief The main algorithm for finding the shortest path
#
# @return The shortest path
def Dijkstra(source):
    # Giant value to simulate infinity
    infinity = sys.maxsize
    
    vertexList = CreateVertexList()
    vertexQueue = vertexList
    vertexQueue.remove(source)
    vertexQueue.insert(0, source)
    adjMatrix  = CreateAdjacencyMatrix(vertexList)
    
    #DEBUGprint("Vertices:", vertexList)
    PrintAdjacenyMatrix(adjMatrix)
    
    # The table for keeping track of total distances
    distances = {}
    
    # Table for keeping track of a vertices' parents
    parents = {}
    
    # Iterate through every vertex
    for vertex in vertexList:
        # Initialize all vertices to no parents
        parents[vertex]    = ''
        
        # The source is the starting point so its value needs to be 0
        if vertex == source:
            distances[vertex] = 0
        else:
            distances[vertex] = infinity
     
    #DEBUGprint("Distances:", distances, "\nParent:   ", parents)
    position = 0
    
    
    for index, vertex in enumerate(vertexQueue):
        if index != 0:
            vertexQueue.remove(vertexQueue[index - 1])
        for edge in edgeWeights:
            if (vertex in edge) and (vertex in vertexQueue):
                if edge[0] == vertex:
                    position = 1
                else:
                    position = 0
                
                path = edge[2] + distances[vertex]
                
                #print("V:", vertex, "\nQ:", vertexQueue, "\nE:", edge, "\nP:", path)
                #print("Distances:", distances, "\nParent:   ", parents)
            
                if path < distances[edge[position]]:
                    distances[edge[position]] = path
                    parents[edge[position]] = vertex
                    #print("Distances:", distances, "\nParent:   ", parents)
        
        # The next vertex to be considered has to be the one with the smallest path value
        MaintainPriorityQueue(vertexQueue, distances, source)
        
    print("Distances:", distances, "\nParents:  ", parents)


# @brief Maintains the priority queue
def MaintainPriorityQueue(vertexQueue, distances, source):
    minimumValue = sys.maxsize
    priorityVertex = ''
    
    # Iterate through only vertices in the queue
    for vertex in vertexQueue:
        # Find vertex with the smallest distance priorityVertex and that is not the source
        if (distances.get(vertex) < minimumValue) and (vertex != source):
            minimumValue = distances.get(vertex)
            priorityVertex = vertex
    
    #DEBUGprint("M:", priorityVertex, "\nM:", vertexQueue)
    
    # Make sure that priorityVertex is in the queue
    if priorityVertex in vertexQueue:
        # TODO: I'm sure there is a cleaner way to reorder the list
        vertexQueue.remove(priorityVertex)
        vertexQueue.insert(1, priorityVertex)


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
        #UserInput()
        
        edgeWeights = [[ 'a', 'b', 10],
                       [ 'a', 'c', 20],
                       [ 'b', 'c',  5],
                       [ 'b', 'd', 16],
                       [ 'c', 'd', 20]]
    else:
        edgeWeights = [[ 'a', 'b', 10],
                       [ 'a', 'c', 20],
                       [ 'b', 'c',  5],
                       [ 'b', 'd', 16],
                       [ 'c', 'd', 20]]
    
    #DEBUG print("Edge Weights:", edgeWeights)
        
    Dijkstra('c')
    

# The 0th argument is the file name
if __name__ == "__main__":
    main(sys.argv[1:])