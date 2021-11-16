# mod-dati-inclinometro

`mod-dati-inclinometro` e’ un layer di compatibilita’ tra due strumenti, in cui l’output del primo deve essere modificato per diventare un input valido per il secondo.

## Descrizione
I file di input sono documenti *.csv contenenti un elenco di misurazioni. Ogni misurazione e’ prefissata da un campo data in formato `gg-mm-aaaa [...]`.  `mod-dati-inclinometro` modifica il formato a `gg/mm/aaaa [...]` e riporta il risultato in output. I nomi dei file rimangono invariati.

## Specifiche Tecniche
I file di input vengono campionati a intervalli regolari (pooling) e `mod-dati-inclinometro` esegue la conversione. Il criterio di selezione e’ la data di scrittura: i file devono essere stati scritti almeno 5 minuti prima (per limitare problemi di sincronia (i/o) del primo strumento). 

Il processo viene fatto partire con cron.

`mod-dati-inclinometro` e’ uno script bash. Questo seleziona i file nella cartella di input (specificata come variabile di ambiente `$INPUT`), esegue la conversione e riporta i risultati nella cartella di output (`$OUTPUT`).

## Installazione
### crontab
Il modo piu’ semplice e’ quello di definire un job in crontab, ad esempio:

```
* 7-19 * * 1-5 bash /mod-dati/mod-dati.sh
```
### docker
Alternativa e’ usare un container docker con un comando come questo:
```
docker run -dit --entrypoint /bin/sh \
           -v cartella-di-input/:/mod-dati/input/ \
           -v cartella-di-output/:/mod-dati/output/ \
           lb803/mod-dati-inclinometro
```