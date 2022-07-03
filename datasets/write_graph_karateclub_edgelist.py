#!/usr/bin/env python3

import networkx as nx
from get_sample_graph import get_graph_karateclub
from pathlib import Path

dataset_path = Path(__file__).parent.parent / 'data' / 'karateclub.edgelist'

g = get_graph_karateclub()
nx.write_edgelist(g, str(dataset_path.resolve()), data=False)
