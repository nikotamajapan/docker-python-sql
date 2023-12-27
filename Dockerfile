FROM python:3.9.10

RUN apt-get update && \
    apt-get -y install gcc libmariadb-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install mysqlclient

COPY ./table_get.py /app/table_get.py

WORKDIR /app

CMD python ./table_get.py