from nltk.corpus import wordnet as wn
import networkx as nx
import matplotlib.pyplot as plt

def get_syns(word):
    synnets = wn.synonyms(word)
    final = []
    for i in synnets:
        for j in i:
            final.append(j)
    return final

class Graph: 
    def __init__(self): 
        self.lst = [] 
    def addEdge(self, a, b): 
        self.lst.append([a,b]) 
    def visualize(self): 
        G = nx.Graph() 
        G.add_edges_from(self.lst) 
        nx.draw_networkx(G,font_size=5,node_size=1) 
        plt.show() 
  
# Driver code 
G = Graph() 
def add_syns(word,depth):
    if depth == 0:
        return 0
    syns = get_syns(word)
    for syn in syns:
        G.addEdge(word,syn)
        add_syns(syn,depth-1)


add_syns("dog",5)
G.visualize()
print(len(get_syns("book")))