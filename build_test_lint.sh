#!/usr/bin/env bash
source ../apps/uxeng/conda_environment_uxeng.sh 
conda activate uxeng
export PYTHONPATH=/home/uxeng/dev/src
python -m nox -s tests-3.12
python -m pylint ./src/ ./tests/
python -m pip install dist/*.whl
pytest --cov ./src/ --cov-report term-missing -n 2 --durations=20
