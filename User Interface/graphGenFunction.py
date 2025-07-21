# creating a file for automatic coordinate assignment (rather than hard-coding)
# should be able to automatically graph a given array of values for a valid SEML graph (following this format: [v1, v2, v3, v4,... e1, e2, e3, e4...] )
import networkx as nx
import matplotlib.pyplot as mp
#importing math library to calculate sine and cosine values
import math as math

# value of k will be a global variable, default value will be 0 (will change later on)
k = 0


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
# takes in an array containing elements that each have a line of file input
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

# returns false if element contains a non-integer, true if it can be casted as an integer
def intCheck(element):
    intStatus = True
    # testing out try-block: https://www.programiz.com/online-compiler/6GwF7XyQRNSby
    try:
        potentialInt = int(element)
    except: # if there's an error
        intStatus = False
    return intStatus

# will continue with third implementation of splitContent, but will use outside functions to determine if elements of splitElements contain non-int characters, then will remove these non-int characters if present
def splitContent(readLineOutput):
    elements = []
    splitElements = []
    for i in range(0, len(readLineOutput)):
        splitElements.append(readLineOutput[i].split(','))
        elements.append([]) # preloading elements array with an amount of empty subarrays that matches # of lines in the input file (to make it easier to )
    print("splitElements: ", splitElements)
    print("elements after preloading empty arrays: ", elements)

    for i in range(0, len(splitElements)): # check if any of the elements contain a non-int value using the intCheck function
        splitElementsSubarray = splitElements[i]


        # if the intCheck function returns true, call the removeNonInts function on this value, then append the value to the array that will be returned
        # if it returns false, append value to the array anyways
         
elements = splitContent(readLineOutput)

toExecute1 = 1

# [INSERT ARRAY OF VALUES HERE]

# transform this into an array of file contents (each element is a line in the file)
    # track the value of k !!
print("The value of element: ", elements)
k = 0


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