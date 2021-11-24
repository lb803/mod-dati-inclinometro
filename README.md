# mod-dati-inclinometro

`mod-dati-inclinometro` e’ un layer di compatibilita’ tra due strumenti, in cui l’output del primo deve essere modificato per diventare un input valido per il secondo.

## Descrizione
I file di input sono documenti *.csv contenenti un elenco di misurazioni. Ogni misurazione e’ prefissata da un campo data in formato `gg-mm-aaaa [...]`.  `mod-dati-inclinometro` modifica il formato a `aaaa-mm-gg [...]` e riporta il risultato in output. L'output viene rediretto ad un file prestabilito.

## Specifiche Tecniche
I file di input vengono campionati a intervalli regolari (pooling) e `mod-dati-inclinometro` esegue la conversione. Il criterio di selezione e’ la data di scrittura: i file devono essere stati modificati/scritti nel'ora precedente.

`mod-dati-inclinometro` e’ un programma python. Questo seleziona i file nella cartella di input, esegue la conversione e riporta i risultati (append) nel file di output.

```
python3 mod-dati.py ./cartella/di/input/ ./file/di/output.csv
```

Il processo viene fatto partire con Windows Scheduler via bat file. Il file bat puo' essere scritto come (un esemptio e' riportato nel repository):

```
@echo off
"C:\percorso\fino\a\python.exe" C:\percorso\fino\a\mod-dati.py C:\percorso\fino\alla\cartella\input\ C:\percorso\fino\a\file\di\output.csv
exit
```


## Installazione

1. Installare python sul computer windows di destinazione: https://www.python.org/downloads/ .
2. Copire il repository `mod-dati-inclinometro`.
3. Personalizzare il file bat di esempio con cartelle e file desiderati.
4. Creare un "Basic Task" nel Windows Scheduler di windows.
