import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine('mysql+pymysql://root:root_password@localhost:3306/olist_db')

def ingest_translation():
    # بنجبره يدور في الفولدر اللي إنت فيه دلوقتي
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'raw_data', 'product_category_name_translation.csv')
    
    print(f"🔍 Checking path: {file_path}")
    
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print(f"📊 Found {len(df)} rows. Starting upload...")
        # if_exists='replace' هيمسح القديم (لو موجود) ويحط الجديد عشان نتأكد
        df.to_sql('category_translation', con=engine, if_exists='replace', index=False)
        print("✅ Success! Check phpMyAdmin now.")
    else:
        print("❌ File NOT found! Check if 'raw_data' folder has the file.")

if __name__ == "__main__":
    ingest_translation()python ingest_translation.py