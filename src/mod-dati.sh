#!/bin/bash

set -eu

in_folder=''
out_file=''

print_usage() {
    echo "usage: mod-dati.sh [-i in_folder] [-o out_file]"
    echo "  -i in_folder   specify input folder infolder"
    echo "  -o out_file    specify output file outfile"
    exit 1
}

while getopts 'i:o:' flag; do
    case "${flag}" in
      i) in_folder="${OPTARG}" ;;
      o) out_file="${OPTARG}" ;;
      *) print_usage
	 exit 1 ;;
    esac
done

find $in_folder -maxdepth 1 -type f -name "*.csv" -mmin -120 \
     -exec python3 "$(dirname $0)/convert.py" {} $out_file \;
