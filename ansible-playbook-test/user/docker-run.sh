#!/bin/bash

set -x

BASEPATH=$(cd `dirname $0`; pwd)
docker run --rm -it -v ${BASEPATH}:/usr/local/iganari -w /usr/local/iganari --name ${1} ${1} /bin/bash
