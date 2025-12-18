## SEML-Graphs-Generator

The code in this repository is meant to automate the process of drawing subtractive-edge magic labeling (SEML) source/sink graphs. 
This project is meant to be a continuation of a Mathematics capstone project done by Alley Koenig, who created code that generates vertex and edge values of valid SEML graphs. The code in this repository is capable of taking the output from that code and use it to automatically draw these SEML graphs. Since the output from the code in the capstone project provided over a thousand different valid graph values, the main goal of this project was to make the process of drawing these graphs more efficient so that it would be easier to potentially discover new theorems for SEML graphs.   under the source/sink cycle categories. 

(Summer 2025 Project)

## Key Files
- graphGenerator.py: File that draws the SEML graphs using the txt file provided by the user. 
- consoleOutput.py: File that is responsible for initiating the graph generation process. This is where the file location for the txt containing SEML graph values must be entered.
- SEMLvalueSorting.py: A file containing functions that extract the edge values and vertex values from user input. They also double check the validity of the user input. Functions in this file are used in the graphGenerator.py file.
- testUserInput.txt: This file contains the SEML graph values in a format that the code is able to read. These values are converted into PNGs containing these values in a drawn out SEML graph. 

## Author

**Alyanna Martinez**