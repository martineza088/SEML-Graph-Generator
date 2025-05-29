# suppose this is your line from the txt file
gString = "[1, 12, 2, 7, 3, 9, 11, 10, 5, 4, 6, 8]  k= 0" #might not be exact since I'm not sure what the format is

#for in in range(len(gString))
   # if (gString[i] == '') ##LEFT OFF HEREEEEEEEEEEE TRYING TO FIGURE OUT HOW TO PARSE TOKENS CORRECTLY TO CREATE THE EDGE AND VERTEX ARRAYS (JUST REALIZED THAT I FORGOT TO THINK ABOUT DIVIDING THE ARRAY IN TWO FOR VERTEX VS EDGE VALUES)
    
values = []
for i in range(len(gString)):
    char = gString[i]
    match char:
        case ']':
            break
        case '[':
            continue
        case ',':
            continue
        case ' ':
            continue
        case _:
          values.append(char) 
          continue

print(values)

# parses individual characters and DOESN'T parse numbers as a whole (ex: 1, 2 instead of 12)
# gonna use read instead
# note: i could also use the readlines(#) to potentially control the number of characters that are read (continue looping until something other than a number is reached?)

file1 = open('testFile.txt', 'r')
#print("after read function: " + str(file1.read()))
#print("after readline function: " + str(file1.readline()))
#print("after readlines function: " + str(file1.readlines()))


# randomChar = str(gString.read())
# print("randomChar: " + randomChar)
#print(file1.readline())

#print(file1.readlines())
#print(file1.readlines())

txtContent = file1.readlines()
print(txtContent) 


#let's say this is the original array
testArray = [1, 9, 2, 20, 3, 16, 4, 19, 5, 11, 8, 7, 18, 17, 13, 12, 15, 14, 6, 10]

#splitting the array into seperated vertex and edge arrays
vertices = []
edges = []
for i in range(len(testArray)):
    length = len(testArray)
    if (i < length/2):
        vertices.append(testArray[i])
    else:
        edges.append(testArray[i])

print("This is vertices -> " + str(vertices))
print("This is edges -> " + str(edges))


vHead = []
vTail = []

for i in range(len(vertices)):
    if (i % 2 == 0): #if even, its a head vertex. else, it's a tail vertex
        vHead.append(vertices[i])
    else:
        vTail.append(vertices[i]) 

print("This is vHead -> " + str(vHead))
print("This is vTail -> " + str(vTail))


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
#LEFT OFF HEREEEEE ->>> https://www.geeksforgeeks.org/split-and-parse-a-string-in-python/ <- looking at the split function instead cuz it might work better at parsing strings
# ALSO its time to run Alley's code cuz there's more output that I haven't even looked at yet (*-*')
