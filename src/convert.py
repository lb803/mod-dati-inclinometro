#!/usr/bin/env python3
from datetime import datetime, timedelta
import sys
from os import path, walk, stat
import csv
import re

in_folder = path.abspath(sys.argv[1])
out_file = path.abspath(sys.argv[2])

TIME_FRAME=60
HEADER_LENGHT=3


class Source:
    def __init__(self, in_folder):
        self.in_folder = in_folder
        self.now = datetime.now()
        self.time_ago = self.now - timedelta(minutes=TIME_FRAME)

    def get_list(self):
        file_list = []

        for root, dirs, files in walk(self.in_folder):
            for file_name in files:
                file_path = path.join(root, file_name)
                file_metadata = stat(file_path)
                file_mtime = datetime.fromtimestamp(file_metadata.st_mtime)

                if file_mtime > self.time_ago:
                    file_list.append(file_path)

        return file_list


def fix_date(date):
    date_obj = datetime.strptime(date, '%d-%m-%Y %H:%M:%S')

    return date_obj.strftime('%Y-%m-%d %H:%M:%S')

def main():
    source = Source(in_folder)
    file_list = source.get_list()
    print(file_list)

#    with open(in_file, 'r') as csv_r_file, \
#         open(out_file, 'a+') as cvs_w_file:
#        reader = csv.reader(csv_r_file, delimiter=';')
#        writer = csv.writer(cvs_w_file)

        # skip header rows if out_file exists
#        if path.exists(out_file):
#            for header_row in range(HEADER_LENGHT):
#                next(reader)

#        for row in reader:
            # skip empty lines
#            if len(row) == 0:
#                continue

            # if first column matches input date pattern
#            if re.match(r'\d+-\d+-\d+ \d+:\d+:\d+', row[0]):
#                row[0] = fix_date(row[0])

#            writer.writerow(row)


if __name__ == "__main__":
    main()
