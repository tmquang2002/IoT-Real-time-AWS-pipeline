import requests
import json
import time
import random
from datetime import datetime

# URL của API Gateway – sẽ cập nhật sau khi tạo ở Bước 2
API_URL = "https://paukonv4vk.execute-api.ap-southeast-2.amazonaws.com/prod/ingest"

# Danh sách các thiết bị (50 thiết bị)
DEVICE_IDS = [f"sensor_{i:03d}" for i in range(1, 6)]

def generate_sensor_data(device_id):
    return {
        "device_id": device_id,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "temperature": round(random.uniform(60, 85), 2),
        "humidity": round(random.uniform(50, 95), 2),
        "vibration": round(random.uniform(0.01, 0.06), 3)
    }

def send_data():
    for device_id in DEVICE_IDS:
        payload = generate_sensor_data(device_id)
        try:
            response = requests.post(API_URL, json=payload)
            print(f"{device_id}: {response.status_code} - {payload}")
        except Exception as e:
            print(f"Error sending data for {device_id}: {e}")

# Gửi dữ liệu mỗi 10 giây
while True:
    send_data()
    time.sleep(2)
