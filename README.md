# EasyGraph Testing codes

This repository contains testing codes for [EasyGraph](https://github.com/easy-graph/Easy-Graph).

This is a work in progress, and we work closely with the EasyGraph developers to solve the problems we encounter.

- [EasyGraph Testing codes](#easygraph-testing-codes)
  - [Methodology](#methodology)
    - [Overview](#overview)
    - [Technical details](#technical-details)
  - [Setup](#setup)
  - [Run tests](#run-tests)
  - [Issues with the C bindings as per easygraph v0.2a38](#issues-with-the-c-bindings-as-per-easygraph-v02a38)

## Methodology

### Overview
- The result from [NetworkX](https://networkx.org) is used as the source of truth, if they both provide an API to do the same thing. E.g., `nx.constraint(nx.Graph)` and `eg.constraint(eg.Graph)`.
- If NetworkX doesn't have a functionality we want to test, the testing code for that functionality will be placed right inside of the [EasyGraph repository](https://github.com/easy-graph/Easy-Graph). 

- EasyGraph and NetworkX have many overlapping functionalities, while the former provide low-level C++ bindings for compute-intensive work, and have both the pure Python API and the encapsulated C++ API for some of its functionalities, and we will also compare the result from both interfaces for them.

### Technical details
- Testing framework: pytest
- `float` result are compared with `pytest.approx()`
- Testing dataset: see [datasets](./datasets/).
  - The project is focusing on testing the C bindings at the moment, and the `eg.GraphC` class has limited methods for loading data, so
  - The only dataset in used currently is the [`Karate Club undirected graph`](http://vlado.fmf.uni-lj.si/pub/networks/data/Ucinet/UciData.htm) dataset, and I've convert the data to edgelist [here](./karateclub.edgelist).

## Setup

```bash
git clone https://github.com/tddschn/easygraph-test.git
cd easygraph-test

# install pinned dependencies
# CPython >=3.9,<3.10 is required
poetry install # install poetry first: https://python-poetry.org/
# activate venv
poetry shell
```

## Run tests

```bash
poetry run pytest
```

## Issues with the C bindings as per easygraph v0.2a38

- Only the undirected graph class `eg.GraphC` is implemented, 
  - Tt lacks many attributes (e.g. `._adj`, `__dict__`), methods (especially the dunder ones like `__iter__`) and functionalities compared the its pure Python counterpart `eg.Graph`.
  - Hangs or throws seg faults when you run the [example codes](https://easy-graph.github.io/tutorial.html) on the class.
  - It uses different data structures for storing, and it could bite you if you expect them to behave like `eg.Graph`.