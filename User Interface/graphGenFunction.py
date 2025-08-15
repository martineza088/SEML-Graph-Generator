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

# create a single function that generates the whole graph using only an array and the value of k # TODO: will need to add a parameter and a procedure to deal with the value of k
def graphGen(array, txtFilePath):
    readLineOutput = readFile(txtFilePath) # readLineOutput will contain an array of elements from each line of the txtFilePath txt (opens and reads file)
    elements = splitContent(readLineOutput) # splits and edits/reformats readLineOutput to be valid input for functions that create the graph

    return 1


# create a loop that iterates through the array generated using values provided in the txt




# returns array containing elements from each line of the file
def readFile(filePath):
    file = open(filePath)
    c1 = 0
    readLineOutput = []
    fileLine = file.readline()
    readLineOutput.append(fileLine)

    # loops infinitely until there are no more arrays to read (or it won't continue if the file is empty)
    while ((fileLine != '') and (fileLine != '\n')):
        fileLine = file.readline()
        if (fileLine != ''):
            readLineOutput.append(fileLine)
        print("Second attempt at file content reading: ", str(readLineOutput))
    file.close()
    return readLineOutput

readLineOutput = readFile(filePath1)
# takes in an array containing elements that each have a line of file input and returns an array containing subarrays of graph values formatted as valid input for the graph generation functions
#def splitContent(readLineOutput):
 #   elements = []
  #  for i in range(0, len(readLineOutput)):
   #     elements.append(readLineOutput[i].split(','))
    #    print("Added the following element on iteration #", i, ": ", elements[i])
   # return elements

#def splitContent(readLineOutput):# <- PROBLEM: splits values that have more than one digit (ex: '1', '0' instead of '10')
 #   elements = []
  #  for i in range(0, len(readLineOutput)):
   #     elements.append([])
    #    readArray = readLineOutput[i]
     #   for j in range(0, len(readArray)):
      #      if ((readArray[j] != '[') and (readArray[j] != ']') and (readArray[j] != ',') and (readArray[j] != ' ')):
       #         if (readArray[j] == 'k'):
        #            break
         #       elements[i].append(int(readArray[j]))
        #elements.append(readLineOutput[i].split(','))
       # print("Added the following element on iteration #", i, ": ", elements[i])
   # return elements

# working on first implementation of splitContent except this time I'll read from the arrays that result from splitting all the elements in readLineOutput with a ','
# PROBLEM: does not organize elements in the array as intended, elements continue to contain non-integer values so they cannot be casted as integers
# def splitContent(readLineOutput):
  #  elements = []
    # splitElements = []
    # for i in range(0, len(readLineOutput)):
     #   splitElements.append(readLineOutput[i].split(','))
      #  elements.append([])
   # print("splitElements: ", splitElements)
   # print("elements after preloading empty arrays: ", elements)
   # for i in range(0, len(splitElements)):
    #    splitElementsEntry = splitElements[i]
     #   print("This is splitElementsEntry: ", splitElementsEntry)
      #  for j in range(0, len(splitElementsEntry)):
        #    if ((splitElementsEntry[j] != '[') and (splitElementsEntry[j] != ']') and (splitElementsEntry[j] != ',') and (splitElementsEntry[j] != ' ')):
            #    if (splitElementsEntry[j] == 'k'):
                #    break
               # elements[i].append(splitElementsEntry[j]) #elements[i].append(int(splitElementsEntry[j]))
      #  print("Added the following element on iteration #", i, ": ", elements[i], '\n')
   # return elements

# returns false if element is a non-integer, true if it can be casted as an integer (question: is it an integer?  answer: T/F)
def intCheck(element):
    intStatus = True
    # testing out try-block: https://www.programiz.com/online-compiler/6GwF7XyQRNSby
    try:
        potentialInt = int(element)
    except: # if there's an error
        intStatus = False
    return intStatus

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


# takes an array that only contains values that can each be successfully casted into an integer as input. It creates a new array containing the casted version of each value in the original array
def intArrayGen(nonIntArray):
    castedArray = []
    for i in range(len(nonIntArray)):
        castedValue = int(nonIntArray[i])
        castedArray.append(castedValue)
    
    return castedArray

# FOR_RUN def removeNonInts(array):
    # FOR_RUN for i in range(len(array)):
       # FOR_RUN  arrayElement = array[i]
        # FOR_RUN if (arrayElement.__contains__('k'))
        # FOR_RUN if(intCheck(array[i])):
        # FOR_RUN     continue
        # FOR_RUN else:

# will continue with third implementation of splitContent, but will use outside functions to determine if elements of splitElements contain non-int characters, then will remove these non-int characters if present
# FOR_RUN def splitContent(readLineOutput):
    # FOR_RUN elements = []
    # FOR_RUN kValues = []
    # FOR_RUN splitElements = []
    # FOR_RUN for i in range(0, len(readLineOutput)):
        # FOR_RUN splitElements.append(readLineOutput[i].split(','))
        # FOR_RUN elements.append([]) # preloading elements array with an amount of empty subarrays that matches # of lines in the input file 
        # FOR_RUN kValues.append([]) 
    # FOR_RUN print("splitElements: ", splitElements)
    # FOR_RUN print("elements after preloading empty arrays: ", elements)

    # FOR_RUN for i in range(0, len(splitElements)): # check if any of the elements contain a non-int value using the intCheck function
        # FOR_RUN splitElementsSubarray = splitElements[i]  # contains an subarray of separated elements 
        # FOR_RUN print("This is splitElementsSubarray: ", splitElementsSubarray)
        
        # FOR_RUN elements[i], kValues[i] = removeNonInts(splitElementsSubarray)
            


        # if the intCheck function returns true, call the removeNonInts function on this value, then append the value to the array that will be returned (elements array)
        # if it returns false, append value to the array anyways

# 4th draft of splitContent function -> go through each element in readLineOutput and do 2 things: 
# 1 - Remove all elements that aren't an int and that aren't a comma   
# 2 - Add the final integer to the k-values array (remove it from its initial location so that it isn't included in the graph values) 
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
        print("This is splitByEqual: ", splitByEqual) #LEFT OFF HEREEE : trying to figure out how to properly split the array by the '='
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
            else: #TESTING
                print("\n\n\nTHE FOLLOWING VALUE DID NOT PASS THE TEST: ", passFailIntCheckValue, "\n\n\n")

    print("This is formattedInput ->", formattedInput)
    # will remove all the last elements in each subarray from formattedInput and add it to the kValues array
    for i in range(len(formattedInput)):
        kValues.append(formattedInput[i][-1])
        # LEFT OF HEREEEE -> will make formattedInput immutable (string) first by using join function and then will follow same process as above to remove last element by index (removing [-1])
        formattedInput[i][-1] = ''
        #listCast = formattedInput

        # making this immutable to remove the right value (done to avoid a bug caused by having 2 of the same value)
    print("Element list AFTER removing nonints and joining char's -> ", elementList)

splitContent(readLineOutput)
#FOR_RUN elements = splitContent(readLineOutput)

toExecute1 = 1

# [INSERT ARRAY OF VALUES HERE]

# transform this into an array of file contents (each element is a line in the file)
    # track the value of k !!
# FOR_RUN print("The value of element: ", elements)


graphValues = graphCases[caseNum]
print("Reading from the following: ", graphValues)


#n = number of nodes in the graph
n = len(graphValues)/2



# filePath = r"C:\Users\alyan\Downloads\Research\SEML Research (Summer '24 & '25)\SEML-Graph-Generator\starting\SEMLvalueSorting.py"
# exec(filePath)
# print(filePath)
from SEMLvalueSorting import VEarrayGen #using a function from another file
vertices, edges = VEarrayGen(graphValues)
print("Vertices -> ", vertices, "Edges -> ", edges) #printcheck

from SEMLvalueSorting import V_HeadTailGen 
vHead, vTail = V_HeadTailGen(vertices, edges)
print("vHead -> ", vHead, "vTail -> ", vTail)
# radius of the graph (will have a circular shape) 
r = n/2  # number of nodes & radius: 4 & 2, 6 & 3, 8 & 4, 10 & 5, 14 & 7

SEMLgraph = nx.DiGraph()

# x and y-coordinate arrays
x_cor = []
y_cor = []

anglesDeg = [] # stores the angles where the nodes are all located (in order)

i = 0
c = 360/n
while (i < 360):
    # i is the angle in degrees, will be converted to radians to calculate the cosine value
    anglesDeg.append(i)
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

print("Coordinates in proper formats: ") #printing coordinates + formatting them into tuples
coordinateTuples = []
for i in range(len(x_cor)):
    print("Node " + str(vertices[i]) + " is at (" + str(x_cor[i]) + ", " + str(y_cor[i]) + ")")
    coordinateTuples.append((x_cor[i], y_cor[i]))

print("Coordinate tuples: ", coordinateTuples)

# for loop that iterates through the x and y-coordinate arrays (for node location) and values in SEML array (FOR NODES ONLY)
for i in range(len(vertices)):
    # SEMLgraph.add_node(7,pos=(-4,-2),node_color='gray') <- command format for below
    SEMLgraph.add_node(vertices[i], pos = (x_cor[i], y_cor[i]), node_color = 'gray')


edgeTuples = []
for i in range(0, len(vTail)):  # ex: i = 0, len(vTail) = 5
    newTuple1 = (vTail[i], vHead[i])   # (vTail[0], vHead[0])
    newTuple2 = (vTail[i], vHead[(i+1) % len(vHead)])   # (vTail[0], vHead[1])
    edgeTuples.append(newTuple1)
    edgeTuples.append(newTuple2)

print("edgeTuples -> ", edgeTuples)

toExecute = "SEMLgraph.add_edges_from(" + str(edgeTuples) + ")" 
exec(toExecute)

print("This is anglesDeg: ", anglesDeg) # declared in line 65


# adding edge values to the graph

# finding value of radius for graph nodes
def findRadius(point1Tuple, point2Tuple):
    x_point1 = point1Tuple[0]
    y_point1 = point1Tuple[1]

    x_point2 = point2Tuple[0]
    y_point2 = point2Tuple[1]

    d = math.sqrt(math.exp2(x_point2 - x_point1) + math.exp2(y_point2 - y_point1)) #euclidean distance of two points
    r = d/2
    return r

r = findRadius((x_cor[0], y_cor[0]), (x_cor[1], y_cor[1]))
print("This is the radius: ", r)


# finding node coordinate midpoints for origin values

def findMidpoint(point1Tuple, point2Tuple):
    x_point1 = point1Tuple[0]
    y_point1 = point1Tuple[1]

    x_point2 = point2Tuple[0]
    y_point2 = point2Tuple[1]

    midpointCoord = ((x_point2 + x_point1)/2, (y_point2 + y_point1)/2)
    return midpointCoord

nodeMidpoints = []
for i in range(len(coordinateTuples)):
    currentCoord1 = coordinateTuples[i]
    currentCoord2 = coordinateTuples[(i+1)%(len(coordinateTuples))]
    
    midpoint = findMidpoint(currentCoord1, currentCoord2)
    nodeMidpoints.append(midpoint)
print("These are the node midpoints: ", nodeMidpoints)

# applying origin and angle formula
# requires an array/list of the angles in degrees of each of the nodes in the graph 
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

edgeAngleArray = edgeAngleGen(anglesDeg)

# r and angle are decimal values, origin is a tuple with decimal values 
def edgeCoordGen(r, angle, origin):
    h = origin[0]
    k = origin[1]
    x_edgeCoord = (r * math.cos(math.radians(angle)) + h)
    y_edgeCoord = (r * math.sin(math.radians(angle)) + k)

    edgeCoord = (x_edgeCoord, y_edgeCoord)
    return edgeCoord

edgeCoordPoints = []
# generating all edge coordinate points
for i in range(len(nodeMidpoints)):
    coord = edgeCoordGen(r, edgeAngleArray[i], nodeMidpoints[i])
    edgeCoordPoints.append(coord)

print("These are the edge coordinates: ", edgeCoordPoints)


# for loop that iterates through edge coordinate array (EDGES ONLY)
for i in range(len(edgeCoordPoints)):
    # SEMLgraph.add_node(7,pos=(-4,-2),node_color='gray') <- command format for below
    SEMLgraph.add_node(edges[i], pos = edgeCoordPoints[i], node_color = 'gray')
    #    SEMLgraph.add_node(edges[i], pos = (edgeCoordPoints[i][0], edgeCoordPoints[i][1]), node_color = 'gray')



#STRINGS TO AVOID CREATING GRAPHS
#'''
position = nx.get_node_attributes(SEMLgraph, 'pos')
node_color = nx.get_node_attributes(SEMLgraph, 'node_color')

# title = "Testing Automatic w/ edges for test case #" + str(caseNum)
title = []
title.append("Testing Automatic w edges for test case #" + str(caseNum))
title.append("Graph " + str(caseNum) + " of [INSERT AMOUNT OF VALID GRAPHS ] - k = " + str(k))

# change index to choose title for graphs (MAKE SURE TO ALSO CHANGE LINE 222)
mp.title(title[0])
nx.draw(SEMLgraph, position, node_color = 'gray', with_labels = True)

# CHANGE LINES 222   AND 216  
mp.savefig(title[0] + ".jpg")
#next two functions are executed to clear the recently created graphs (to prepare to create new graphs)
mp.clf()
SEMLgraph.clear()
print("done")
#'''