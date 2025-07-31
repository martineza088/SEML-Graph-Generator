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