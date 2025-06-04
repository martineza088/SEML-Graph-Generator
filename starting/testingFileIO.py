# testing input/output in python
import networkx as nx
import matplotlib.pyplot as mpt

file = open("testFile.txt", "x")

# this directly writes to the file: file.write("yoooo wassup")

# but this is a more efficient use of resources since it closes the file right after using it: vvv
#with open("testFile.txt", "a") as file:
#    file.write("why hello")

#but since I need the file to stay open, I'm not gonna use the while-statement above




file.write("hmmmmm\n")
file.write("checking output")
print("it worksss")

inputFromUser = input("Enter something: ")

print("Your input: " + inputFromUser)

floatFromUser = float(input("Enter a number: "))
print("a decimal  -> " + str(floatFromUser))

#adding input to the file
file.write("\nmore words -> " + inputFromUser + "\nnumber!: " + str(floatFromUser))

