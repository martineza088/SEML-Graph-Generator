# creating a file for automatic coordinate assignment (rather than hard-coding)
# should be able to automatically graph a given array of values for a valid SEML graph (following this format: [v1, v2, v3, v4,... e1, e2, e3, e4...] )

#importing math library to calculate sine and cosine values
import math as math

#creating this variable for convenience and for more readable code
pi = math.pi 
print("pi:", pi)
#provided array:
graphValues = [4, 8, 1, 7, 3, 6, 5, 2]

#n = number of nodes in the graph
n = len(graphValues)/2

#testing the math library

x = (3*pi)/2
stringX = "(3*pi)/2"
print("cos(", stringX, ") = ", math.cos(x))