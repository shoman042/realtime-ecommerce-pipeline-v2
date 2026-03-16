import pandas as pd
from sqlalchemy import create_engine

# الاتصال بقاعدة البيانات
engine = create_engine('mysql+pymysql://root:root_password@localhost:3306/olist_db')

def ingest_order_items():
    print("⏳ Reading Order Items CSV...")
    # تأكد من مسار الملف
    df = pd.read_csv('raw_data/olist_order_items_dataset.csv')
    
    # تحويل التاريخ لـ DateTime
    df['shipping_limit_date'] = pd.to_datetime(df['shipping_limit_date'])
    
    print(f"🚀 Uploading {len(df)} items to MySQL...")
    # الرفع لجدول order_items
    df.to_sql('order_items', con=engine, if_exists='append', index=False)
    print("✅ Order Items table is ready!")

if __name__ == "__main__":
    ingest_order_items()