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

#Left off here ->>> https://www.geeksforgeeks.org/split-and-parse-a-string-in-python/ <- looking at the split function instead since it might work better at parsing strings