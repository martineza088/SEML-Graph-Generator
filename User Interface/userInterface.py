from graphGenerator import *

# this python script will serve to provide user's ability to generate graphs using only input
filePath1 = r"C:\Users\alyan\Downloads\Research\SEML Research (Summer '24 & '25)\SEML-Graph-Generator\User Interface\testUserInput.txt"

def userInterface(filePath):
    print("\n\nInitializing graph generator...\n\n")
    SEML_graphValues, SEML_kValues = readFile(filePath)
    print("\n\nChecking validity of each graph...\n")
    checkingGraphValidity(SEML_graphValues, SEML_kValues)

    print("Generating graphs.... (Note: This may take longer for a txt file containing more than 10 graphs)")
    graphGen(filePath, SEML_graphValues, SEML_kValues)

userInterface(filePath1)