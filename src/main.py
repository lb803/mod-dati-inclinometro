#!/usr/bin/env python3
from datetime import datetime
import sys
from os import path
import csv
import re

file_path = path.abspath(sys.argv[1])
file_name = path.basename(file_path)

def ordina_data(data):
    data_obj = datetime.strptime(data, '%d-%m-%Y %H:%M:%S')

    return data_obj.strftime('%d/%m/%Y %H:%M:%S')

def main():
    with open(file_name, 'w+') as csv_w_file:
        writer = csv.writer(csv_w_file, delimiter=';')
        
        with open(file_path, 'r') as csv_r_file:
            reader = csv.reader(csv_r_file, delimiter=';')

            for row in reader:
                # if not empty and first column matches input date pattern
                if len(row) and \
                   re.match(r'\d+-\d+-\d+ \d+:\d+:\d+', row[0]):
                    row[0] = ordina_data(row[0])

                # write entire row to output file
                writer.writerow(row)




if __name__ == "__main__":
    main()
