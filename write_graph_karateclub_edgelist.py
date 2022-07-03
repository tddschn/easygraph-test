#!/usr/bin/env python3

import networkx as nx
from datasets.get_sample_graph import get_graph_karateclub

g = get_graph_karateclub()
nx.write_edgelist(g, 'karateclub.edgelist', data=False)
