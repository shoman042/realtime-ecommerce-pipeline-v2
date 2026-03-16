import pandas as pd
from sqlalchemy import create_engine

# الاتصال بالـ MySQL اللي جوه دوكر
# التركيبة: mysql+pymysql://user:password@localhost:port/dbname
engine = create_engine('mysql+pymysql://root:root_password@localhost:3306/olist_db')

def upload_data():
    print("⏳ Reading CSV file...")
    # تأكد إن مسار الملف صح بالنسبة لمكان السكربت
    df = pd.read_csv('raw_data/olist_customers_dataset.csv')
    
    print(f"🚀 Uploading {len(df)} rows to MySQL...")
    # الرفع للجدول اللي كريتناه
    df.to_sql('customers', con=engine, if_exists='append', index=False)
    
    print("✅ Done! Data is now in the database.")

if __name__ == "__main__":
    upload_data()