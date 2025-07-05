# creating a file for automatic coordinate assignment (rather than hard-coding)
# should be able to automatically graph a given array of values for a valid SEML graph (following this format: [v1, v2, v3, v4,... e1, e2, e3, e4...] )
import networkx as nx
import matplotlib.pyplot as mp
#importing math library to calculate sine and cosine values
import math as math

#creating this variable for convenience and for more readable code
pi = math.pi 
print("pi:", pi)
#provided array:
graphCases = [[4, 8, 1, 7, 3, 6, 5, 2], [1, 6, 2, 10, 3, 12, 5, 4, 8, 7, 9, 11], # 4 vertices, 6 vertices
              [8, 14, 7, 15, 3, 16, 1, 12, 4, 5, 6, 10, 11, 13, 9, 2], #[8, 7, 3, 1, 14, 15, 16, 12, 4, 5, 6, 10, 11, 13, 9, 2], # 8 vertices
              [1, 9, 2, 20, 3, 16, 4, 19, 5, 11, 8, 7, 18, 17, 13, 12, 15, 14, 6, 10], # 10 vertices
              [1, 12, 2, 15, 3, 28, 4, 26, 5, 21, 6, 25, 7, 27, 9, 8, 11, 10, 23, 22, 20, 19, 14, 13, 17, 16, 18, 24], # 14 vertices
              [1, 36, 2, 33, 3, 18, 4, 23, 5, 22, 6, 35, 7, 28, 8, 32, 9, 34, 31, 30, 27, 26, 11, 10, 15, 14, 13, 12, 25, 24, 17, 16, 20, 19, 21, 29]] # 18 vertices
caseNum = 0
graphValues = graphCases[caseNum]
print("Reading from the following: ", graphValues)


#n = number of nodes in the graph
n = len(graphValues)/2

#testing the math library vvvvvvvvvvvvv
# the input for cos(x) function MUST BE IN RADIANS

# treating x1 as if its in radians
x1 = pi/3       # pi/3 because in radians, this is equal to a 60 degree angle. 
stringX1 = "pi/3"
print("cos(", stringX1, ") = ", math.cos(x1))

# treating x as if its in degrees
x = 60
xRad = math.radians(x)
print("cos(", x, ") = ", math.cos(xRad))

#testing ^^^^^^^^

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
#requires an array/list of the angles in degrees of each of the nodes in the graph 
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

#title = "Testing Automatic w/ edges for test case #" + str(caseNum)
title = "Testing Automatic w edges for test case #" + str(caseNum)
mp.title(title)
nx.draw(SEMLgraph, position, node_color = 'gray', with_labels = True)

mp.savefig(title + ".jpg")
#next two functions are executed to clear the recently created graphs (to prepare to create new graphs)
mp.clf()
SEMLgraph.clear()
print("done")
#'''