#let's say this is the original array
testArray = [1, 9, 2, 20, 3, 16, 4, 19, 5, 11, 8, 7, 18, 17, 13, 12, 15, 14, 6, 10]

#splitting the array into seperated vertex and edge arrays
def VEarrayGen(array):
    vertices = []
    edges = []
    for i in range(len(array)):
        length = len(array)
        if (i < length/2):
            vertices.append(array[i])
        else:
            edges.append(array[i])
    return vertices, edges

vertices, edges = VEarrayGen(testArray)
print("This is vertices -> " + str(vertices))
print("This is edges -> " + str(edges))


def V_HeadTailGen(vertices, edges):
    vHead = []
    vTail = []

    for i in range(len(vertices)):
        if (i % 2 == 0): #if even, its a head vertex. else, it's a tail vertex
            vHead.append(vertices[i])
        else:
            vTail.append(vertices[i]) 
    
    return vHead, vTail

vHead, vTail = V_HeadTailGen(vertices, edges)
print("This is vHead -> " + str(vHead))
print("This is vTail -> " + str(vTail))

#   @return a boolean, true if the given SEML graph is valid, false otherwise
def SEMLgraphValidity(array):
    vertices, edges = VEarrayGen(array)
    vHead, vTail = V_HeadTailGen(vertices, edges) 
    # code block that does calculates the sums for each head vertex and its edge value
    sum = [] # array of (headVertex + edgeLabel) values
    numV = int(len(vertices)/2) #variable used for the following loop
    print("Value of numV -> " + str(numV)) #
    for v in range(numV):
        vIndex = (v+1)%numV #makes sure that second head vertex is added first and the first head vertex is added last (to follow the formatting of the SEML graph values in Alley's code output)
        for i in range(2):
            appending = vHead[vIndex] + edges[((2*v) + i + 1) % len(edges)] #adding the head vertex and its associated edge label
            sum.append(appending)

    print("Final sum array -> " + str(sum))
    # code block that calculates the subtractive edge weight
    subWeight = []
    for v in range(numV):
        vIndex = (v+1)%numV
        for i in range(2):
            appending = sum[((2*v) + i + 1) % len(edges)] - vTail[vIndex] # subtracting tail vertex from the sum (head vertex + edge label) 
            subWeight.append(appending)

    print("Final subtractive edge weight array -> " + str(subWeight))

    # code block that checks to see if the SEML graph is valid based on whether or not all subtractive edge weights in the graph match
    graphValidity = True
    for i in range(1, len(subWeight)):
        if(subWeight[0] == subWeight[i]):
            continue
        else:
            print("Elements don't match: " + str(subWeight[0]) + " and " + str(subWeight[i])) 
            graphValidity = False

    if (graphValidity == True):
        print("Graph is Valid")
    else: 
        print("Graph is Not Valid")

    return(graphValidity)