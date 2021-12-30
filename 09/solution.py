import json
import re
import sys

import networkx as nx


INPUTMATCH = r'(?P<c1>\w+) to (?P<c2>\w+) = (?P<d>\d+)'

cities = connections = nx.Graph()
for line in sys.stdin.readlines():
    m = re.match(INPUTMATCH,line).groupdict()
    cities.add_edge(m['c1'], m['c2'], weight=int(m['d']))

for n in list(cities.nodes()):
    cities.add_edge(n,'s',weight=0)
    cities.add_edge(n,'t',weight=0)

#list(map(print,cities.edges(data=True)))

minweight = float('inf')
maxweight = 0
for path in nx.all_simple_paths(cities, source='s', target='t'):
    if len(path) < len(cities):
        continue
    weight = nx.path_weight(cities, path, weight='weight')
    #print(path, weight)
    minweight = min(weight,minweight)
    maxweight = max(weight,maxweight)
print(f'*1: {minweight}')
print(f'*2: {maxweight}')

import matplotlib.pyplot as plt
import graphviz as gv
from networkx.drawing.nx_agraph import graphviz_layout



graphpos = graphviz_layout(cities)
nx.draw(cities,graphpos,node_size=400,node_color='#AADDDD')
nx.draw_networkx_labels(cities,graphpos,{n:f"{n}" for n in cities.nodes()},font_size=10)
nx.draw_networkx_edge_labels(cities,graphpos,{(u,v):d['weight'] for (u,v,d) in cities.edges(data=True)})
nx.drawing.nx_pydot.write_dot(cities,"debug.dot")
plt.show()
