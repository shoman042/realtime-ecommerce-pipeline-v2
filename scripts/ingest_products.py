import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:root_password@localhost:3306/olist_db')

def ingest_products():
    file_path = 'raw_data/olist_products_dataset.csv'
    
    print(f"⏳ Reading {file_path}...")
    df = pd.read_csv(file_path)
    
    print(f"🚀 Uploading {len(df)} products to MySQL...")
    df.to_sql('products', con=engine, if_exists='append', index=False)
    print("✅ Products table is ready!")

if __name__ == "__main__":
    ingest_products()