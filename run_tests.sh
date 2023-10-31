#!/bin/bash
set -e
OAREPO_VERSION=${OAREPO_VERSION:-11}
OAREPO_VERSION_MAX=$((OAREPO_VERSION+1))

MODEL="thesis"
VENV=".model_venv"

if test -d ./build-tests/$MODEL; then
	rm -rf ./build-tests/$MODEL
fi

oarepo-compile-model ./build-tests/$MODEL.yaml --output-directory ./build-tests/$MODEL -vvv
python3 -m venv $VENV
. $VENV/bin/activate
pip install -U setuptools pip wheel
#pip install invenio-app
#pip install pytest-invenio
pip install "oarepo>=$OAREPO_VERSION,<$OAREPO_VERSION_MAX"
pip install "./build-tests/$MODEL[tests]"
pytest build-tests/$MODEL/tests

