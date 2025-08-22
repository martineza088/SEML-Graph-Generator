testArray = [1, 2, 3, 4, 5, 6]
print("Before removal: ", testArray)
testArray.remove(4)
print("After removal: ", testArray)
number = 2
print("Does it contain", number, "? -> ", testArray.__contains__(number))

word = "why hello there"
letter = 'wh'
print("Does 'word' contain", letter, "? ->", word.__contains__(letter))

word2 = "hello"
if (word2 == "hello"):
    print("This code works")

# how would you remove the 'h' from hello? -> go from immutable to mutable by casting string into a list

# what element will the following command remove from the arrayvv
testArray2 = [1, 2, 3, 4, 5, 1, 2, 1, 1]
print("testArray2 ->", testArray2)

testArray2.remove(1)
print("testArray2 after removal ->", testArray2)

# testing join function - calling multiple non-consecutive elements from a list and then putting them together using join
testArray3 = ['oh', 'ok', 'um', 'well']
testStringParanthesized = testArray3[3], testArray3[2]
# testString = ''.join(testArray3[0], testArray3[3]) <- join function only takes one parameter
testStringList = list(testStringParanthesized)
testString = ''.join(testStringList)
print("testString: ", testString)

anotherString = 'entertain '
print("length of anotherString: ", len(anotherString)) # length of a string = number of characters in the string, including spaces\

mockValues = "[4, 8, 1, 7, 3, 6, 5, 2] k = -1000]"
print("\n\nThis is mockValues: ", mockValues)
mockValuesSplit = mockValues.split("=")
print("After splitting mockValues by '=': ", mockValuesSplit)

'''
# is it possible to import a function from another file in a function?
# note: i moved this file into the User Interface so that it could access the file that the other function is in
def testing():
    from SEMLvalueSorting import VEarrayGen
    arrayOfGraphValues = [6, 9, 11, 3, 10, 5, 12, 7, 1, 2, 4, 8] # would have to be in a proper format already
    vertices, edges = VEarrayGen(arrayOfGraphValues)
    print("It works! Vertices -> ", vertices, "Edges -> ", edges)

testing()

'''

# do loops defaulty start at 0? yes
for i in range(10):
  print(i)
