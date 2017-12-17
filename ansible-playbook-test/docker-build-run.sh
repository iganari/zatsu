#!/bin/bash

set -xeu

_I_TAG='zatsu-ansible'

set +eu
docker rmi ${_I_TAG}

set -eu
# docker build --no-cache . -t ${_I_TAG}
docker build . -t ${_I_TAG}

sh ./docker-run.sh ${_I_TAG}
