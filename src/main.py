#!/usr/bin/env python3
from datetime import datetime

CAMPIONI = ['26-10-2021 02:00:00', '26-10-2021 05:00:00', '26-10-2021 08:00:00', '26-10-2021 11:00:00', '26-10-2021 14:00:00', '26-10-2021 17:00:00', '26-10-2021 20:00:00']

def ordina_data(data):
    data_obj = datetime.strptime(data, '%d-%m-%Y %H:%M:%S')

    return data_obj.strftime('%d/%m/%Y %H:%M:%S')

def main():
    for data in CAMPIONI:
        print(ordina_data(data))


if __name__ == "__main__":
    main()
