from graphGenerator import *

# this python script will serve to provide user's ability to generate graphs using only input
filePath1 = r"C:\Users\alyan\Downloads\Research\SEML Research (Summer '24 & '25)\SEML-Graph-Generator\Graph Generation\testUserInput.txt" # must be changed if filepath for the txt file containing SEML graph values is different

def consoleOutput(filePath):
    print("\n\nInitializing graph generator...\n\n")
    SEML_graphValues, SEML_kValues = readFile(filePath)
    print("\n\nChecking validity of each graph...\n")
    checkingGraphValidity(SEML_graphValues, SEML_kValues)

    print("\n\n\nGenerating graphs.... (Note: This may take longer for a txt file containing many graphs)")
    graphGen(filePath, SEML_graphValues, SEML_kValues)

consoleOutput(filePath1)