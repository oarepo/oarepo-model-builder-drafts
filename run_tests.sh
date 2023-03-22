#!/bin/bash
set -e

MODEL="thesis"
VENV=".model_venv"
if test -d ./tests/$MODEL; then
	rm -rf ./tests/$MODEL
fi
oarepo-compile-model ./tests/$MODEL.yaml --output-directory ./tests/$MODEL --profile model,drafts -vvv
python3 -m venv $VENV
. $VENV/bin/activate
pip install -U setuptools pip wheel
pip install "./tests/$MODEL[tests]"
pytest tests/$MODEL/tests
