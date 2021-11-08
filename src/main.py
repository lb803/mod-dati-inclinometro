#!/usr/bin/env python3
from datetime import datetime
import sys
from os import path
import csv
import re

file_path = path.abspath(sys.argv[1])

def ordina_data(data):
    data_obj = datetime.strptime(data, '%d-%m-%Y %H:%M:%S')

    return data_obj.strftime('%d/%m/%Y %H:%M:%S')

def main():
    with open(file_path) as csv_r_file:
        data = csv.reader(csv_r_file, delimiter=';')

        for row in data:
            # if not empty and first column matches input date pattern
            if len(row) and \
               re.match(r'\d+-\d+-\d+ \d+:\d+:\d+', row[0]):
                row[0] = ordina_data(row[0])
                print(row[0])




if __name__ == "__main__":
    main()
