import networkx as nx
import matplotlib.pyplot as mp

#creating the digraph object
SEML = nx.DiGraph()
color = 'blue'
#adding nodes
SEML.add_node(7,pos=(1,3),node_color= color)
SEML.add_node(1,pos=(3,1),node_color=color)
SEML.add_node(8,pos=(5,3),node_color=color)
SEML.add_node(4,pos=(3,5),node_color=color)

SEML.add_node(2,pos=(1.5,4.5),node_color=color)
SEML.add_node(5,pos=(1.5,1.5),node_color=color)
SEML.add_node(6,pos=(4.5,1.5),node_color=color)
SEML.add_node(3,pos=(4.5,4.5),node_color=color)

#edges
SEML.add_edges_from([(7, 1), (8, 1), (8, 4), (7, 4)])

position = nx.get_node_attributes(SEML, 'pos')
node_color = nx.get_node_attributes(SEML, 'node_color')

mp.title("Testing 4 vertices")
nx.draw(SEML, position, node_color = 'gray', with_labels = True)
mp.savefig("testSave" + ".jpg")

#next two functions are executed to clear the recently created graphs (to prepare to create new graphs)
mp.clf()
SEML.clear()

print("ok!")