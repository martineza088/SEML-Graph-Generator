# creating a file for automatic coordinate assignment (rather than hard-coding)
# should be able to automatically graph a given array of values for a valid SEML graph (following this format: [v1, v2, v3, v4,... e1, e2, e3, e4...] )
import networkx as nx
import matplotlib.pyplot as mp
#importing math library to calculate sine and cosine values
import math as math

#creating this variable for convenience and for more readable code
pi = math.pi # PIF (place in function)
print("pi:", pi)
#provided array:
graphCases = []
caseNum = 4

# retrieving graphs from txt file and generating an array that will be used to generate graphs
    # graph values 
#requires a filePath to read a txt <- will be a parameter for the function as well
filePath1 = r"C:\Users\alyan\Downloads\Research\SEML Research (Summer '24 & '25)\SEML-Graph-Generator\User Interface\testUserInput.txt"



# Helper method for the splitContent function
# returns false if element is a non-integer, true if it can be casted as an integer (question: is it an integer?  answer: T/F)
def intCheck(element):
    intStatus = True
    # testing out try-block: https://www.programiz.com/online-compiler/6GwF7XyQRNSby
    try:
        potentialInt = int(element)
    except: # if there's an error
        intStatus = False
    return intStatus

# NOT BEING USED
# checks an entire array to see if it contains purely integer values , returns True if all elements are integers, and False if it contains an noninteger
def intArrayCheck(array):
    intStatus = True
    nonIntIndex = -1 
    for i in range(len(array)):
        if (not(intCheck(array[i]))):
            intStatus = False
            # LEFT OF HEREEE : TRYING TO MAKE IT SO THAT IT'LL RETURN THE INDEX WHERE IT FINDS THE NONINT AND RETURNS IT ALONG WITH INT STATUS
            nonIntIndex = i
            return intStatus, nonIntIndex
            break
    
    return intStatus, nonIntIndex

# NOT BEING USED
# takes an array that only contains values that can each be successfully casted into an integer as input. It creates a new array containing the casted version of each value in the original array
def intArrayGen(nonIntArray):
    castedArray = []
    for i in range(len(nonIntArray)):
        castedValue = int(nonIntArray[i])
        castedArray.append(castedValue)
    
    return castedArray


# Takes in an array containing elements that each have a line of file input and returns an array containing subarrays of graph values formatted as valid input for the graph generation functions
# Steps: goes through each element in readLineOutput and does 2 things: 
# 1 - Removes all elements that aren't an int and that aren't a comma   
# 2 - Adds the final integer to the k-values array (removes it from its initial location so that it isn't included in the graph values) 
# output will contain two arrays, one containing graph values in a valid format for the graphGen function and another containing k-values for each graph
def splitContent(readLineOutput):
    kValues = [] # will store the k-values for each graph
    formattedInput = [] # the list containing split, integer elements from readLineOutput
    # pre-structuring formattedInput to be subarrays that can be added to later on
    for i in range(len(readLineOutput)):
        formattedInput.append([])
    print("formattedInput after prestructuring: ", formattedInput)
    
    for i in range(len(readLineOutput)):
        lineElement = readLineOutput[i]   # edit line element to only include non-integers
        elementList = list(lineElement)  # list version of the lineElement string (transforming immutable string into mutable object)
        print("Element list: ", elementList)
        for j in range(len(lineElement)):
            if (intCheck(elementList[j]) or elementList[j] == ',' or elementList[j] == '-' or elementList[j] == '='):
                continue
            else: # if a nonint is found or if a k is detected
                print("this element is being replaced at i =", i, "and j =", j, ": ", elementList[j])
                elementList[j] = ''
        removedNonIntsString = ''.join(elementList) # join the element list
        splitByEqual = removedNonIntsString.split('=') # LEFT OFF HEREEEE (outdated): split by '=' BEFORE nonints are removed from the string
        splitList = removedNonIntsString.split(',') # splits the string by commas and turns it into an array
        print("splitList at i = ", i, " ->", splitList)
        print("This is splitByEqual: ", splitByEqual) #LEFT OFF HEREEE (outdated): trying to figure out how to properly split the array by the '='
        print("This is splitByEqual[-1]: ", splitByEqual[-1])
        kValues.append(int(splitByEqual[-1]))
        print("This is kValues at i =", i, " ->", kValues)

        # remove the last element of splitByEqual and split the content of the first index [0] by ','
        splittingIndex0 = splitByEqual[0].split(',')
        print("This is splittingIndex0: ", splittingIndex0)

        for j in range(len(splittingIndex0)):
            passFailIntCheckValue = splittingIndex0[j]
            if (intCheck(splittingIndex0[j])):
                formattedInput[i].append(int(splittingIndex0[j]))
            else: 
                print("\n\n\nThe following value cannot be read as an integer: ", passFailIntCheckValue, "\n\n\n")

    ''' This code might not be necessary to include in the function
    print("This is formattedInput ->", formattedInput)
    # will remove all the last elements in each subarray from formattedInput and add it to the kValues array
    for i in range(len(formattedInput)):
        kValues.append(formattedInput[i][-1])
        # LEFT OF HEREEEE -> will make formattedInput immutable (string) first by using join function and then will follow same process as above to remove last element by index (removing [-1])
        formattedInput[i][-1] = ''
        #listCast = formattedInput

        # making this immutable to remove the right value (done to avoid a bug caused by having 2 of the same value)
    print("Element list AFTER removing nonints and joining char's -> ", elementList)

    '''
    return formattedInput, kValues


# returns a 2D array containing all the SEML graph values from the txt file in the proper format and a 1D array containing the k-values for each graph
def readFile(filePath):
    file = open(filePath)
    c1 = 0
    readLineOutput = [] # readLineOutput will contain an array of elements from each line of the txtFilePath txt (opens and reads file)
    fileLine = file.readline()
    readLineOutput.append(fileLine)

    # loops infinitely until there are no more arrays to read (or it won't continue if the file is empty)
    while ((fileLine != '') and (fileLine != '\n')):
        fileLine = file.readline()
        if (fileLine != ''):
            readLineOutput.append(fileLine)
        print("Second attempt at file content reading: ", str(readLineOutput))
    file.close()

    SEML_graphValues, SEML_kValues = splitContent(readLineOutput) # splits and edits/reformats readLineOutput to be valid input for functions that create the graph
    return SEML_graphValues, SEML_kValues




readLineOutput = readFile(filePath1)



graphValuesFormatted, valuesOfK = readFile(filePath1)        # TESTING readFile FUNCTION FUNCTIONALITY (NOTE: TESTING FUNCTION FUNCTIONALITY lines should all either be commented out or deleted at the same time since they are all being used interconnectedly right now)

print("\n\nFinal values returned by splitContent: valuesOfK -> ", valuesOfK, "\ngraphValuesFormatted -> ", graphValuesFormatted, "\n\n")    # TESTING readFile FUNCTION FUNCTIONALITY
#FOR_RUN elements = splitContent(readLineOutput)

toExecute1 = 1






#------------------------------------------------------

# This is where I initially started testing using cases, shouldn't need it anymore
#graphValues = graphCases[caseNum]
#print("Reading from the following: ", graphValues)

# TESTING graphGen FUNCTION FUNCTIONALITY
graphValues = graphValuesFormatted[0]           # TESTING graphGen FUNCTION FUNCTIONALITY
#n = number of nodes in the graph (will use numNodes instead)
numNodes = len(graphValues)/2



# filePath = r"C:\Users\alyan\Downloads\Research\SEML Research (Summer '24 & '25)\SEML-Graph-Generator\starting\SEMLvalueSorting.py"
# exec(filePath)
# print(filePath)

# Classifies the node values from the formatted array as either vertices or edges. It also determines whether a value is a head or tail value.   
# param graphValues: a properly formatted array of graph values
# returns: 4 arrays of categorized values and the value of r (determined by the number of nodes in the array)
def sortNodeValues(graphValues, n):
    from SEMLvalueSorting import VEarrayGen #using a function from another file
    vertices, edges = VEarrayGen(graphValues)
    print("Vertices -> ", vertices, "Edges -> ", edges) #printcheck

    from SEMLvalueSorting import V_HeadTailGen 
    vHead, vTail = V_HeadTailGen(vertices, edges)
    print("vHead -> ", vHead, "vTail -> ", vTail)
    # radius of the graph (will have a circular shape) 
    r = n/2  # number of nodes & radius: 4 & 2, 6 & 3, 8 & 4, 10 & 5, 14 & 7
    return vertices, edges, vHead, vTail, r



# Function that automatically calculates the coordinates of each node in a graph with n nodes. Returns these coordinates.
# param n: the number of nodes in the graph 
# param r: the radius of the graph (distance from the center to one of the nodes), should come from the sortNodeValues function
def coordinateGen(n, r):
    # x and y-coordinate arrays
    x_cor = []
    y_cor = []

    anglesDeg = [] # stores the angles where the nodes are all located (in order), # TESTING coordinateGen FUNCTION FUNCTIONALITY

    i = 0
    c = 360/n
    while (i < 360):
        # i is the angle in degrees, will be converted to radians to calculate the cosine value
        anglesDeg.append(i) # # TESTING coordinateGen FUNCTION FUNCTIONALITY
        print("This is the value of i: ", i)
        i_rad = math.radians(i)
        # print("i in radians: ", i_rad)
        # multiplying cos(rad(i)) by r to find x-coordinate
        #print("math.cos(i),  -> ")
        cor1 = r * math.cos(i_rad)
        x_cor.append(cor1)

        cor2 = r * math.sin(i_rad)
        y_cor.append(cor2)

        i += c # increments by c, aka angle of coordinates in degrees

    print("x_cor -> ", x_cor, " | y_cor -> ", y_cor)
    print("This is anglesDeg: ", anglesDeg) 
    return x_cor, y_cor, anglesDeg


# Groups the x and y coordinates for each node into a touple. It also assigned directed edges to certain nodes to follow the properties of an SEML graph
# param x_cor/y_cor: an array of the assigned x-coordinates/y-coordinates for each node
# param vertices: an array containing the values of each vertex node in the graph
# param vHead/vTail: arrays containing values that are considered either a head or tail vertex
def groupingCoordinates (graphObject, x_cor, y_cor, vertices, vHead, vTail):

    print("Coordinates in proper formats: ") #printing coordinates + formatting them into tuples
    coordinateTuples = []
    for i in range(len(x_cor)):
        print("Node " + str(vertices[i]) + " is at (" + str(x_cor[i]) + ", " + str(y_cor[i]) + ")")
        coordinateTuples.append((x_cor[i], y_cor[i]))

    print("Coordinate tuples: ", coordinateTuples)

    # for loop that iterates through the x and y-coordinate arrays (for node location) and values in SEML array (FOR NODES ONLY)
    for i in range(len(vertices)):
        # SEMLgraph.add_node(7,pos=(-4,-2),node_color='gray') <- command format for below
        graphObject.add_node(vertices[i], pos = (x_cor[i], y_cor[i]), node_color = 'gray')


    edgeTuples = []
    for i in range(0, len(vTail)):  # ex: i = 0, len(vTail) = 5
        newTuple1 = (vTail[i], vHead[i])   # (vTail[0], vHead[0])
        newTuple2 = (vTail[i], vHead[(i+1) % len(vHead)])   # (vTail[0], vHead[1])
        edgeTuples.append(newTuple1)
        edgeTuples.append(newTuple2)

    print("edgeTuples -> ", edgeTuples)

    return coordinateTuples, edgeTuples

# Adds directed edges to the graph object, does it in a pattern consistent with SEML graph properties
# param graphName: the name of the graph object
# param edgeTuples: a tuple that will determine where directed edges will go and what direction they will face
'''
def addEdges(graphName, edgeTuples):
    toExecute =  graphName + ".add_edges_from(" + str(edgeTuples) + ")"  #TODO: TEST IF THIS LINE OF CODE WOULD WORK (would make it so that the function is more generalizable, so the graph can be named anything and nodes will still be added to it)
    #toExecute = "SEMLgraph.add_edges_from(" + str(edgeTuples) + ")" 
    exec(toExecute)
'''

def addEdges(graphObject, edgeTuples):
    stringEdgeTuples = str(edgeTuples)
    print("This is edgeTuples: ", edgeTuples)
    print("This is stringEdgeTuples: ", stringEdgeTuples)
    graphObject.add_edges_from(edgeTuples)


# adding edge values to the graph

# finding value of radius for graph nodes
def findRadius(point1Tuple, point2Tuple):
    x_point1 = point1Tuple[0]
    y_point1 = point1Tuple[1]

    x_point2 = point2Tuple[0]
    y_point2 = point2Tuple[1]

    d = math.sqrt(math.exp2(x_point2 - x_point1) + math.exp2(y_point2 - y_point1)) #euclidean distance of two points
    r = d/2
    print("This is the radius: ", r)
    return r


# Helper method for nodeMidpoint function, finds node coordinate midpoints for origin values
# param point1Tuple/point2Tuple: the coordinates of the both nodes this function is finding the midpoint of
# returns: the coordinates of the midpoint
def findMidpoint(point1Tuple, point2Tuple):
    x_point1 = point1Tuple[0]
    y_point1 = point1Tuple[1]

    x_point2 = point2Tuple[0]
    y_point2 = point2Tuple[1]

    midpointCoord = ((x_point2 + x_point1)/2, (y_point2 + y_point1)/2)
    return midpointCoord

# Identifies the midpoint of all given coordinate tuples, going around 
# the whole array in a circle to also find the midpoint of the first and last element as well
# param coordinateTuples: the array of coordinates to find the midpoints of
# returns: an array containing all the midpoint coordinates found from the given node coordinates 
def nodeMidpoint(coordinateTuples):
    nodeMidpoints = []
    for i in range(len(coordinateTuples)):
        currentCoord1 = coordinateTuples[i]
        currentCoord2 = coordinateTuples[(i+1)%(len(coordinateTuples))]
        
        midpoint = findMidpoint(currentCoord1, currentCoord2)
        nodeMidpoints.append(midpoint)
    print("These are the node midpoints: ", nodeMidpoints)
    return nodeMidpoints



# applying origin and angle formula
# requires an array/list of the angles in degrees of each of the nodes in the graph
# param anglesDeg: , should come from coordinatesGen
def edgeAngleGen(anglesDeg):
    edgeAngleArray = []
    for i1 in range(len(anglesDeg)):
        i2 = (i1 + 1) % (len(anglesDeg)) # index of the angle of the second node
        
        if (i2 != 0):
            edgeAngle = (anglesDeg[i1] + anglesDeg[i2])/2
        else:
            edgeAngle = (anglesDeg[i1] + 360)/2
        print("Edge angles at i1 = ", i1, ": ", edgeAngle)
        edgeAngleArray.append(edgeAngle)
    return edgeAngleArray

# Helper method for edgeCoordArrayGen, 
# params r and angle: float values used to calculate coordinates
# param origin: a tuple with decimal values representing origin point  
def edgeCoordGen(r, angle, origin):
    h = origin[0]
    k = origin[1]
    x_edgeCoord = (r * math.cos(math.radians(angle)) + h)
    y_edgeCoord = (r * math.sin(math.radians(angle)) + k)

    edgeCoord = (x_edgeCoord, y_edgeCoord)
    return edgeCoord

# Creates an array of edge coordinate tuples and adds these edges to the graph object
# param r: float value, should come from the loop of graphGen AFTER passing coordinate values into findRadius function
# param edgeAngleArray: an array of the angle assigned to each edge, should come from edgeAngleGen
def edgeCoordArrayGen(r, edges, nodeMidpoints, edgeAngleArray, graphObject):
    edgeCoordPoints = []
    # generating all edge coordinate points
    for i in range(len(nodeMidpoints)):
        coord = edgeCoordGen(r, edgeAngleArray[i], nodeMidpoints[i])
        edgeCoordPoints.append(coord)

    print("These are the edge coordinates: ", edgeCoordPoints)

    # for loop that iterates through edge coordinate array (EDGES ONLY)
    for i in range(len(edgeCoordPoints)):
        # SEMLgraph.add_node(7,pos=(-4,-2),node_color='gray') <- command format for below
        graphObject.add_node(edges[i], pos = edgeCoordPoints[i], node_color = 'gray')
        #    SEMLgraph.add_node(edges[i], pos = (edgeCoordPoints[i][0], edgeCoordPoints[i][1]), node_color = 'gray')


# Creates the actual PNG's of the graphs
def graphPNG(graphObject, i):
    position = nx.get_node_attributes(graphObject, 'pos')
    node_color = nx.get_node_attributes(graphObject, 'node_color')
    title = "SEML Graph #" + str(i)

    mp.title(title)
    nx.draw(graphObject, position, node_color = 'gray', with_labels = True)

    mp.savefig(title + ".jpg")
    #next two functions are executed to clear the recently created graphs (to prepare to create new graphs)
    mp.clf()
    graphObject.clear()
    print("SEML Graph #", i, "has been generated\n\n")

# A single function that generates all the graphs in the txt file found in txtFilePath
def graphGen(txtFilePath):
    SEML_GRAPH = nx.DiGraph()
    SEML_graphValues, SEML_kValues = readFile(txtFilePath) 
    graphName = "SEML_GRAPH"
    # create a loop that iterates through the 2D array containing formatted graph values
    for i in range(len(SEML_graphValues)):
        currentGraph = SEML_graphValues[i]
        n = len(currentGraph)/2
        
        # calling sortNodeValues
        vertices, edges, vHead, vTail, r = sortNodeValues(currentGraph, n)

        # calling coordinateGen
        x_cor, y_cor, anglesDeg = coordinateGen(n, r)

        #calling groupingCoordinates
        coordinateTuples, edgeTuples = groupingCoordinates(SEML_GRAPH, x_cor, y_cor, vertices, vHead, vTail)

        #calling addEdges
        addEdges(SEML_GRAPH, edgeTuples)

        # calling findRadius, updating the value of r
        r = findRadius((x_cor[0], y_cor[0]), (x_cor[1], y_cor[1]))

        # calling nodeMidpoint
        nodeMidpoints = nodeMidpoint(coordinateTuples)

        # calling edgeAngleGen
        edgeAngleArray = edgeAngleGen(anglesDeg)

        # calling edgeCoordArrayGen
        edgeCoordArrayGen(r, edges, nodeMidpoints, edgeAngleArray, SEML_GRAPH)

        # calling graphPNG
        graphPNG(SEML_GRAPH, i)    
    return 1


# moment of truth: 
print("\n\n\nVVVVVVVVVVVVVVVVV THIS IS GRAPH GEN VVVVVVVVVVVVVVVVVVVVVVVV\n\n\n")
graphGen(filePath1)
print("\n\n\n^^^^^^^^^^^^^^^^^ THIS IS GRAPH GEN ^^^^^^^^^^^^^^^^^^^^^^^^\n\n\n")







#STRINGS TO AVOID CREATING GRAPHS

'''
position = nx.get_node_attributes(SEMLgraph, 'pos')
node_color = nx.get_node_attributes(SEMLgraph, 'node_color')

# title = "Testing Automatic w/ edges for test case #" + str(caseNum)
title = []
title.append("Testing Automatic w edges for test case #" + str(caseNum))
title.append("Graph " + str(caseNum) + " of [INSERT AMOUNT OF VALID GRAPHS ] - k = " + str(k))

# change index to choose title for graphs (MAKE SURE TO ALSO CHANGE LINE 222)
mp.title(title[0])
nx.draw(SEMLgraph, position, node_color = 'gray', with_labels = True)

# CHANGE LINES 222 AND 216  
mp.savefig(title[0] + ".jpg")
#next two functions are executed to clear the recently created graphs (to prepare to create new graphs)
mp.clf()
SEMLgraph.clear()
print("done")
'''