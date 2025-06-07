# creating a file for automatic coordinate assignment (rather than hard-coding)
import networkx as nx
import matplotlib.pyplot as mp

#checking if node values can be negative, and if the graph image will accomodate

#creating the digraph object
negativeSEML = nx.DiGraph()
#adding nodes, coordinate transformations: x - minus 5, y - minus 5
negativeSEML.add_node(7,pos=(-4,-2),node_color='gray')
negativeSEML.add_node(1,pos=(-2,-4),node_color='gray')
negativeSEML.add_node(8,pos=(0,-2),node_color='gray')
negativeSEML.add_node(4,pos=(-2,0),node_color='gray')

negativeSEML.add_node(2,pos=(-3.5, -.5),node_color='blue')
negativeSEML.add_node(5,pos=(-3.5, -3.5),node_color='white')
negativeSEML.add_node(6,pos=(-.5, -3.5),node_color='white')
negativeSEML.add_node(3,pos=(-.5, -.5),node_color='white')

#edges
negativeSEML.add_edges_from([(7, 1), (8, 1), (8, 4), (7, 4)])

position = nx.get_node_attributes(negativeSEML, 'pos')
node_color = nx.get_node_attributes(negativeSEML, 'node_color')

mp.title("Testing negative 4 vertices")
nx.draw(negativeSEML, position, node_color = 'gray', with_labels = True)
mp.savefig("Negative SEML Coordinates" + ".jpg")

#next two functions are executed to clear the recently created graphs (to prepare to create new graphs)
mp.clf()
negativeSEML.clear()

print("done!")