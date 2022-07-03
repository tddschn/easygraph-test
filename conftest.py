#!/usr/bin/env python3

import easygraph as eg
import networkx as nx
from easygraph import Graph, GraphC
import pytest
from pathlib import Path


@pytest.fixture
def karateclub_edgelist_abspath() -> str:
    return str((Path(__file__).parent / 'karateclub.edgelist').resolve())


@pytest.fixture
def karateclub_graph(karateclub_edgelist_abspath) -> Graph:
    g = Graph()
    g.add_edges_from_file(karateclub_edgelist_abspath)
    return g


@pytest.fixture
def karateclub_graphc(karateclub_edgelist_abspath) -> GraphC:
    gc = GraphC()
    gc.add_edges_from_file(karateclub_edgelist_abspath)
    return gc


@pytest.fixture
def karateclub_graph_nx() -> nx.Graph:
    import networkx as nx
    from datasets.get_sample_graph import get_graph_karateclub

    g = get_graph_karateclub()
    return g
