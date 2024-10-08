"""
For those who need a refresher:
A graph is a non-linear data structure that can have a finite number of connections
The goal of this project is to apply my Linear Algebra, Discrete Mathematics, Python, Data Structures, and Algorithms skills

A vertex is an object that has data
An edge connects two vertices A and B
A path is a sequence of edges to get from vertex A to vertex B

For now, this implementation will only include simple graphs and psuedographs:

simple graphs do not support multiple edges or edges where the start and end vertices are the same (loops)
and psuedographs are simple graphs that have loops

An adjacency matrix is a 2D int square array where each element indicates the number of edges connecting vertex A to vertex B 

"""

# converts an adjacency list representation of a graph to its adjacency matrix representation
def toMatrix(graph : dict) -> list:
    adjMatrix = []
    matrixLen = len(graph)
    # the "elements" list is there so we can add the corresponding zeroes into the matrix
    elements = []
    
    counter : int = 0
    # First I will make the matrix without customizing it
    # since range for loops are not supported for dictionaries I added a separate index to keep track of what row we are on
    for vertex in graph:
        # add an empty list for each vertex in the graph (it doesn't matter whether they have connections or not)
        adjMatrix.append([])
        elements.append(vertex)
        for i in range(0,matrixLen):
            adjMatrix[counter].append(0)
        counter += 1
    
    
    counter = 0
    for vertex in graph:
        for i in range(0,matrixLen):
            # we traverse through all elements to find matches and add 1 to the position if there are any matches
            if(graph.get(vertex).count(elements[i]) == 1):
                adjMatrix[counter][i] = 1
        counter += 1
    
    # return the final list
    return adjMatrix

# Matrix Multiplication is useful in finding the number of paths between two vertices (even though I will be multiplying the matrix by itself, this saves lots of time by not rewriting code)
def multiplyMatrix(matrix1 : list, matrix2 : list) -> list:
    product = []
    if(not canMultiplyMatrices(matrix1,matrix2)):
        print('Sorry. The two matrices cannot be multiplied. The number of ROWS in the Second matrix should be the same as the number of COLUMNS in the First matrix')
        return []
    rows = len(matrix1)
    columns = len(matrix2[0])

    for i in range(0,rows):
        product.append([])
        for j in range(0,columns):
            # this will be resetted every time we are done adding the final position in each cell
            sum = 0
            # k's stopping point can either be rows or columns as those are always the same
            for k in range(0,rows):
                sum += matrix1[i][k]*matrix2[k][j]
                pass
            product[i].append(sum)
    
    return product

# this program only works if 2D lists are inputted as parameters
def canMultiplyMatrices(matrix1 : list, matrix2 : list) -> bool:
    if(len(matrix1)==0 or len(matrix2)==0):
        return False
    # the number of COLUMNS in the FIRST matrix have to be the same as the number of ROWS in the SECOND matrix
    if(len(matrix2)!=len(matrix1[0])):
        return False
    
    return True

# depth first search (from first)
def dfs(graph : dict, start) -> None:
    if(not start in graph):
        print('Sorry, but the graph does not contain '+str(start))
        return None
    # python does not have a built in stack for some reason so I used a list that behaves like a stack
    stack = [start]
    # lists can take more time so I used a set to keep track of visited elements
    visited = set()
    # the starting node appears in the stack initially
    while(len(stack)>0):
        current = stack.pop()
        # if we have not printed out something, we do it and then set it as visited so that it does not print again
        if(not current in visited):
            print(current)
            visited.add(current)  
        # the reverse is done so that the traversal seems logical
        # a for loop is done to accept all the neighbors
        for neighbor in reversed(graph[current]):
            if neighbor not in visited:
                stack.append(neighbor)

# breadth first search (from first)
def bfs(graph : dict, start) -> None:
    if(not start in graph):
        print('Sorry, but the graph does not contain '+str(start))
        return None
    queue = [start]
    visited = set()
    while(len(queue)>0):
        # queue is FIFO so we add from one side and remove from the other
        current = queue.pop(0)
        if(not current in visited):
            print(current)
            visited.add(current) 
        for element in graph[current]:
            if(element not in visited):
                queue.append(element)

def numPaths(graph : dict, pathLength : int, start, end) -> int:
    # as mentioned above, we will use matrix exponentiation m^n where m is the matrix and n is the exponent (which is the length of each path)
    graphAsMatrix : list = toMatrix(graph)
    finalMatrix : list = graphAsMatrix
    
    for i in range(0,pathLength):
        finalMatrix = multiplyMatrix(finalMatrix,graphAsMatrix)
    
    elements = []
    for vertex in graph:
        elements.append(vertex)
    if(elements.count(start)==0 or elements.count(end)==0):
        print('Sorry, one the elements do not exist')
        return -1
    # duplicates do not matter since I am using a dictionary
    row = elements.index(start)
    col = elements.index(end)
    return finalMatrix[row][col]

# undirected graph using adjacency list
testGraph1 = {
    'A' : ['B','C'],
    'B' : ['A','B','C'],
    'C' : ['A','B','C'],
    'D' : [],
}
# directed graph using adjacency list
testGraph2 = {
    'A' : ['B','C','D','F'],
    'B' : ['A'],
    'C' : ['C','F'],
    'D' : ['B','C','F'],
    'E' : ['B','E','F'],
    'F' : ['A','B','C','D','F'],
}


print("CONVERTING ADJACENCY LISTS TO ADJACENCY MATRICES:")
print(toMatrix(testGraph1))
print(toMatrix(testGraph2))

matrix1 = [
    [1,5,3],
    [4,6,12],
    [-2,5,1]
]
matrix2 = [
    [-5,8],
    [1,6],
    [-1,-9]
]
matrix3 = [
    [3,2,1,6,8],
    [-1,-5,-2,8,-12]
]

print("CAN MULTIPLY MATRICES (Using test matrices):")
print(canMultiplyMatrices(matrix1,matrix2)) # true
print(canMultiplyMatrices(matrix1,matrix3)) # false
print(canMultiplyMatrices(matrix2,matrix3)) # true

print(multiplyMatrix(matrix1,matrix2))
print(multiplyMatrix(matrix1,matrix3))
print(multiplyMatrix(matrix1,matrix1))

print("NUMBER OF PATHS")
print(numPaths(testGraph1,2,'A','C'))
print(numPaths(testGraph2,5,'F','B'))

print("DEPTH FIRST SEARCH")
dfs(testGraph1,'A')
dfs(testGraph1,'E')
dfs(testGraph2,'B')
dfs(testGraph2,'G')

print("BREADTH FIRST SEARCH")
bfs(testGraph1,'A')
bfs(testGraph1,'E')
bfs(testGraph2,'B')
bfs(testGraph2,'G')