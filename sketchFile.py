testArray = [1, 2, 3, 4, 5, 6]
print("Before removal: ", testArray)
testArray.remove(4)
print("After removal: ", testArray)
number = 2
print("Does it contain", number, "? -> ", testArray.__contains__(number))

word = "why hello there"
letter = 'wh'
print("Does /'word'/ contain", letter, "? ->", word.__contains__(letter))