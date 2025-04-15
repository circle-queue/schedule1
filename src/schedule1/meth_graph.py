import json
import networkx as nx
from importlib.resources import files

import pandas as pd
from schedule1 import data
DATA = files(data)

df = pd.read_csv(DATA / 'meth_graph.csv', header=None).set_axis(['in_1', 'in_2', 'name', 'value'], axis=1)

G = nx.Graph()
for row in df.itertuples():
    G.add_edge(row.in_1, row.name, attr=row.in_2)

nx.set_edge_attributes(G, df.set_index(['in_1', 'name']).in_2.to_dict(), 'label')
edge_labels = {(1, 2): 'Edge 1-2', (1, 3): 'Edge 1-3', (2, 3): 'Edge 2-3', (3, 4): 'Edge 3-4', (4, 5): 'Edge 4-5'}
nx.set_edge_attributes(G, edge_labels, 'label')

pos = nx.spring_layout(G, seed=42)  # Layout for better visualization
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'label'), font_size=8)