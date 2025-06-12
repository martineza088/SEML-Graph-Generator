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
graphValues = [4, 8, 1, 7, 3, 6, 5, 2]  #[1, 9, 2, 20, 3, 16, 4, 19, 5, 11, 8, 7, 18, 17, 13, 12, 15, 14, 6, 10]


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



# radius of the graph (will have a circular shape) 
r = n/2  # number of nodes & radius: 4 & 2, 6 & 3, 8 & 4, 10 & 5, 14 & 7

SEMLgraph = nx.DiGraph()

# x and y-coordinate arrays
x_cor = []
y_cor = []

i = 0
c = 360/n
while (i <= 360):
    # i is the angle in degrees, will be converted to radians to calculate the cosine value
    i_rad = math.radians(i)

    # multiplying cos(rad(i)) by r to find x-coordinate
    cor1 = r * math.cos(i)
    x_cor.append(cor1)

    cor2 = r * math.sin(i)
    y_cor.append(cor2)

    i += c # increments by c, aka angle of coordinates in degrees


print("end")
# for loop that iterates through the x, y-coordinate arrays (for node location) and values in SEML array 
# for i in range(len(graphValues/2)):
    # SEMLgraph.add_node()
# SEMLgraph.add_node(7,pos=(-4,-2),node_color='gray')





