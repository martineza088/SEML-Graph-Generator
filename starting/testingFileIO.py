# yo
import networkx as nx
import matplotlib.pyplot as mpt

file = open("testFile.txt", "x")

# this directly writes to the file: file.write("yoooo wassup")

# but this is a more efficient use of resources since it closes the file right after using it: vvv
#with open("testFile.txt", "a") as file:
#    file.write("Yoink")

#but since I need the file to stay open, I'm not gonna use the while-statement above




file.write("ummmmm\n")
file.write("wondering if this'll add")
print("yuhhh it workedddd")

inputFromUser = input("Enter something: ")

print("yey: " + inputFromUser)

floatFromUser = float(input("Enter a number: "))
print("ooh a decimal perhaps? -> " + str(floatFromUser))

#adding input to the file
file.write("\nooh more words -> " + inputFromUser + "\nnumber!: " + str(floatFromUser))

