#!/usr/bin/env python3
from datetime import datetime

CAMPIONI = ['26-10-2021 02:00:00', '26-10-2021 05:00:00', '26-10-2021 08:00:00', '26-10-2021 11:00:00', '26-10-2021 14:00:00', '26-10-2021 17:00:00', '26-10-2021 20:00:00']

# questa funzione accetta una 'data' in ingresso e
# restituisce un equivalente con i campi ordinati come lo vogliamo noi.
def ordina_data(data):
    # crea una istanza di datatime con i valori di 'data'
    # sapedo che il formato di ingresso e' dd-mm-yy hh:mm:ss
    data_obj = datetime.strptime(data, '%d-%m-%Y %H:%M:%S')

    # restituisci la data riordinata come dd/mm/yy hh:mm:ss
    return data_obj.strftime('%d/%m/%Y %H:%M:%S')

def main():
    # considera i valori di 'CAMPIONI' uno alla volta e
    # riponili a turno in 'data'
    for data in CAMPIONI:
        # mostra a schermo il risultatto della funzione ordina_data()
        # avente argomento 'data'
        print(ordina_data(data))


if __name__ == "__main__":
    main()
