import time
import requests
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# -------- Arduino --------
ARDUINO_IP = "192.168.43.26"
URL = f"http://{ARDUINO_IP}/data"

# -------- InfluxDB --------
INFLUX_URL = "http://influxdb:8086"
TOKEN = "super-secret-fire-token"
ORG = "fire-org"
BUCKET = "fire-data"

client = InfluxDBClient(
    url=INFLUX_URL,
    token=TOKEN,
    org=ORG
)

write_api = client.write_api(write_options=SYNCHRONOUS)

print("🔥 Ingestion service started")

while True:
    try:
        r = requests.get(URL, timeout=3)
        data = r.json()

        point = (
            Point("fire_metrics")
            .field("temperature", data["temp"])
            .field("humidity", data["hum"])
            .field("smoke", data["smoke"])
            .field("alarm", int(data["alarm"]))
        )

        write_api.write(bucket=BUCKET, record=point)
        print("✅ Data written:", data)

    except Exception as e:
        print("❌ Error:", e)

    time.sleep(2)