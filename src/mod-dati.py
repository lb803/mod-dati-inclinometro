#!/usr/bin/env python3
from datetime import datetime, timedelta
import sys
from os import path, walk, stat
import csv
import re

in_folder = path.abspath(sys.argv[1])
out_file = path.abspath(sys.argv[2])

TIME_FRAME = 60
HEADER_LENGHT = 3


class Source:
    """
    Class to discover and produce a list of files to be processed.

    Given an input folder `in_folder`, the class checks which files have
    been modified in the last `TIME_FRAME` minutes and returns a list with
    the get_list() method.
    """
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


class Writer:
    """
    Writer class.

    Csv rows returned by a Reader object are written to a new csv file.
    """
    def __init__(self, out_file):
        self.cvs_w_file = open(out_file, 'a+', newline='')
        self.writer = csv.writer(self.cvs_w_file)

    def write_row(self, row):
        self.writer.writerow(row)

    def __exit__(self):
        self.csv_w_file.close()


class Reader:
    """
    Reader class

    Given an input file `in_file`, the class allows to iter through the rows
    of interest to the software (see magic method __iter__() for details)
    which can be safely written with a Writer object.

    Supplementary methods are:
     - fix_date() which fixes the date format of the input `row`;
     - skip_header_rows() as we don't want to repeat the header when appending
    entries from multiple files (or if `out_file` exists for whatever reason).
    """
    def __init__(self, in_file):
        self.csv_r_file = open(in_file, 'r')
        self.reader = csv.reader(self.csv_r_file, delimiter=';')

    def __iter__(self):
        for row in self.reader:
            # skip empty lines
            if len(row) == 0:
                continue

            # if first column matches input date pattern
            if re.match(r'\d+-\d+-\d+ \d+:\d+:\d+', row[0]):
                row[0] = self.fix_date(row[0])

            yield row

    def fix_date(self, date):
        date_obj = datetime.strptime(date, '%d-%m-%Y %H:%M:%S')

        return date_obj.strftime('%Y-%m-%d %H:%M:%S')

    def skip_header_rows(self):
        for header_row in range(HEADER_LENGHT):
            next(self.reader)

    def __exit__(self):
        self.csv_r_file.close()


def main():
    source = Source(in_folder)
    file_list = source.get_list()

    # quit if no input file(s) to process
    if not file_list:
        sys.exit()

    out_file_exists = path.exists(out_file)

    writer = Writer(out_file)

    for index, in_file in enumerate(file_list):
        reader = Reader(in_file)

        if index or out_file_exists:
            reader.skip_header_rows()

        for row in reader:
            writer.write_row(row)


if __name__ == "__main__":
    main()
