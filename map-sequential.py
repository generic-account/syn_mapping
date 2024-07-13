from nltk.corpus import wordnet as wn
import networkx as nx

def get_syns(word):
    synnets = wn.synonyms(word)
    final = []
    for i in synnets:
        for j in i:
            final.append(j)
    return final

def gen_adj_dict(words):
    d = {}
    for word in words:
        d[word] = tuple(get_syns(word))
    return d

with open("400k_words_alpha.txt", "r") as f:
    words = [line.strip() for line in f.readlines()]
print("file read")

adj_dict = gen_adj_dict(words)
print("adj dict done")

G = nx.Graph(adj_dict)
print("graph generated")

nx.write_gml(G, "top_400k.gml")
print("graph saved")