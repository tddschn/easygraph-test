# EasyGraph Testing codes

This repository contains testing codes for [EasyGraph](https://github.com/easy-graph/Easy-Graph).

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