FROM python:3.10-slim

WORKDIR /app

COPY ingest.py .

RUN pip install requests influxdb-client

CMD ["python", "ingest.py"]