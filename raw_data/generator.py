import pandas as pd
from faker import Faker
import random
import time
import os

fake = Faker()

def generate_order():
    return {
        "order_id": fake.uuid4(),
        "customer_name": fake.name(),
        "product_name": random.choice(["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]),
        "price": round(random.uniform(10.0, 1000.0), 2),
        "order_date": pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
    }

# عمل فولدر للبيانات الخام (Bronze Layer)
if not os.path.exists('data/bronze'):
    os.makedirs('data/bronze')

print("بدء توليد البيانات... اضغط Ctrl+C للإيقاف")
while True:
    data = [generate_order() for _ in range(5)] # بنعمل 5 طلبات كل مرة
    df = pd.DataFrame(data)
    
    # حفظ الملف بصيغة CSV في طبقة الـ Bronze
    file_name = f"data/bronze/orders_{int(time.time())}.csv"
    df.to_csv(file_name, index=False)
    
    print(f"تم إنشاء ملف جديد: {file_name}")
    time.sleep(10) # انتظر 10 ثواني قبل تكرار العملية