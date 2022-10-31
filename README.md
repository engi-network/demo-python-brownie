# demo-python-brownie

Project demonstrating Solidity and Python [Brownie](https://eth-brownie.readthedocs.io/) on the Engi network.

## Install

`pipenv install`

### Generate requirements

`pipenv requirements --dev > requirements.txt`

## Run

`pipenv run pytest --report-log pytest.json`

### Docker

`docker compose up --exit-code-from tests`

Engi-compatible test runner output is in `pytest.json`