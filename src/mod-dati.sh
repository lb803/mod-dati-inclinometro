#!/bin/bash

set -eu

find $INPUT -maxdepth 1 -type f -name "*.csv" -mmin +5 -exec \
     sh -c 'sed "s,\([0-9]\{2\}\)-\([0-9]\{2\}\)-\([0-9]\{4\}\),\1/\2/\3," "$1" > $OUTPUT/$(basename "$1") && rm "$1"' sh {} \;