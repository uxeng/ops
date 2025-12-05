#!/usr/bin/env bash
source ./apps/uxeng/conda_environment_uxeng.sh 
conda activate uxeng
cd dev
python -m nox -s tests-3.12
python -m pylint ./src/ ./tests/
