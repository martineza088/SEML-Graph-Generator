import networkx as nx
import matplotlib.pyplot as mp

#creating the digraph object
SEML = nx.DiGraph()
#adding nodes
SEML.add_node(7, pos = (1, 3), node_color = 'gray')

position = nx.get_node_attributes(SEML, 'pos')
node_color = nx.get_node_attributes(SEML, 'node_color')

mp.title("TESTINGGGG")
nx.draw(SEML, position, node_color = 'gray', with_labels = True)
mp.savefig("testSave" + ".jpg")

#next two functions are executed to clear the recently created graphs (to prepare to create new graphs)
mp.clf()
SEML.clear()

print("ok!")