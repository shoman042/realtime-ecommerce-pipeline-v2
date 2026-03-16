import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root_password@localhost:3306/olist_db')

def ingest_orders():
    print("⏳ Reading Orders CSV...")
    df = pd.read_csv('raw_data/olist_orders_dataset.csv')
    
    # تحويل الأعمدة من Text لـ DateTime عشان SQL يفهمها
    date_columns = [
        'order_purchase_timestamp', 'order_approved_at', 
        'order_delivered_carrier_date', 'order_delivered_customer_date', 
        'order_estimated_delivery_date'
    ]
    
    for col in date_columns:
        df[col] = pd.to_datetime(df[col])
    
    print(f"🚀 Uploading {len(df)} orders to MySQL...")
    df.to_sql('orders', con=engine, if_exists='append', index=False)
    print("✅ Orders table is ready!")

if __name__ == "__main__":
    ingest_orders()