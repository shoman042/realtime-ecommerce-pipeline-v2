import pandas as pd
from kafka import KafkaProducer
import json, time, os

producer = KafkaProducer(
    bootstrap_servers=['localhost:9094'],
    api_version=(0, 10, 2),
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

file_path = os.path.join('raw_data', 'olist_orders_dataset.csv')
df = pd.read_csv(file_path)

print("🚀 Streaming Started...")
for index, row in df.head(1000).iterrows():
    data = {"order_id": str(row['order_id']), "customer_id": str(row['customer_id']), 
            "price": 100.0, "order_status": str(row['order_status'])}
    producer.send('olist_orders', value=data)
    print(f"Sent: {data['order_id']}")
    time.sleep(0.1)