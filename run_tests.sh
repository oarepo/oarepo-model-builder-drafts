#!/bin/bash
set -e

MODEL="thesis"
VENV=".model_venv"
export OPENSEARCH_PORT=9400
#cd $(dirname $0)/..
if test -d ./build-tests/$MODEL; then
	rm -rf ./build-tests/$MODEL
fi
oarepo-compile-model ./build-tests/$MODEL.yaml --output-directory ./build-tests/$MODEL --profile model,drafts -vvv
python3 -m venv $VENV
. $VENV/bin/activate
pip install -U setuptools pip wheel
pip install "./build-tests/$MODEL[tests]"
pytest build-tests/$MODEL/tests