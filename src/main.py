#!/usr/bin/env python3
from datetime import datetime
import sys
from os import path

file_path = path.abspath(sys.argv[1])

def ordina_data(data):
    data_obj = datetime.strptime(data, '%d-%m-%Y %H:%M:%S')

    return data_obj.strftime('%d/%m/%Y %H:%M:%S')

def main():
    print(file_path)


if __name__ == "__main__":
    main()
