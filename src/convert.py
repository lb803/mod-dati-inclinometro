#!/usr/bin/env python3
from datetime import datetime
import sys
from os import path
import csv
import re

in_file = path.abspath(sys.argv[1])
out_file = path.abspath(sys.argv[2])

def fix_date(date):
    date_obj = datetime.strptime(date, '%d-%m-%Y %H:%M:%S')

    return date_obj.strftime('%Y-%m-%d %H:%M:%S')

def main():
    with open(in_file, 'r') as csv_r_file:
        reader = csv.reader(csv_r_file, delimiter=';')

        for row in reader:
            # skip empty lines
            if len(row) == 0:
                continue

            # if first column matches input date pattern
            if re.match(r'\d+-\d+-\d+ \d+:\d+:\d+', row[0]):
                row[0] = fix_date(row[0])

            print(row)


if __name__ == "__main__":
    main()
