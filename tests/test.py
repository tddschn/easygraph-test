#!/usr/bin/env python3

import easygraph as eg
import networkx as nx
from easygraph import Graph, GraphC
import pytest
from pytest import approx
from pathlib import Path


def test_constraint(
    karateclub_graph: Graph, karateclub_graphc: GraphC, karateclub_graph_nx: nx.Graph
):
    constraint_nx = nx.constraint(karateclub_graph_nx)
    constraint_eg = eg.constraint(karateclub_graph)
    constraint_egc = eg.constraint(karateclub_graphc)
    assert constraint_nx == approx(constraint_eg)
    assert constraint_nx == approx(constraint_egc)


def test_hierarchy(
    karateclub_graph: Graph, karateclub_graphc: GraphC, karateclub_graph_nx: nx.Graph
):
    # hierarchy_nx = nx.hierarchy(karateclub_graph_nx)
    hierarchy_eg = eg.hierarchy(karateclub_graph)
    hierarchy_egc = eg.hierarchy(karateclub_graphc)
    assert hierarchy_eg == approx(hierarchy_egc)
    # assert hierarchy_nx == approx(hierarchy_eg)
    # assert hierarchy_nx == approx(hierarchy_egc)
