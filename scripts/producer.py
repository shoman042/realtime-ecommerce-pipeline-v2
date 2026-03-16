import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("🚀 Starting Olist Real-time Producer...")

while True:
    data = {
        "order_id": f"order_{random.randint(1000, 9999)}",
        "customer_id": f"user_{random.randint(1, 500)}",
        "price": round(random.uniform(10.5, 500.0), 2),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    
    producer.send('olist_orders', value=data)
    
    print(f"📦 Sent: {data}")
    time.sleep(2) # يبعت طلب كل ثانيتين