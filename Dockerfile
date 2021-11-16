FROM debian:bullseye-slim

RUN apt-get update && \
    apt-get install -y cron

# install script
COPY ./src/mod-dati.sh /mod-dati/

# input and output folders
RUN mkdir /mod-dati/input
ENV INPUT=/mod-dati/input/

RUN mkdir /mod-dati/output
ENV OUTPUT=/mod-dati/output/

# install the cron job
COPY cron-job /etc/cron.d/cron-job
RUN chmod 0644 /etc/cron.d/cron-job
RUN crontab /etc/cron.d/cron-job

CMD bash /mod-dati/mod-dati.sh && \
    service cron start
