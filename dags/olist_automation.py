from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, text

default_args = {'owner': 'yusuf_shoman', 'start_date': datetime(2026, 3, 15)}
dag = DAG('olist_final_master_v12', default_args=default_args, schedule_interval=None)

def master_ingestion():
    # الاتصال مع التأكد من الـ charset
    engine = create_engine('mysql+pymysql://root:root_password@db:3306/olist_db?charset=utf8mb4')
    raw_data_path = '/usr/local/airflow/raw_data/'
    
    with engine.connect() as conn:
        # 1. تحضير جدول Sellers يدوياً
        conn.execute(text("DROP TABLE IF EXISTS sellers;"))
        conn.execute(text("""
            CREATE TABLE sellers (
                seller_id VARCHAR(100) PRIMARY KEY,
                seller_zip_code_prefix INT,
                seller_city VARCHAR(255),
                seller_state VARCHAR(10)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
        """))
        
        # 2. تحضير جدول Order Reviews يدوياً (عشان الإيموجي)
        conn.execute(text("DROP TABLE IF EXISTS order_reviews;"))
        conn.execute(text("""
            CREATE TABLE order_reviews (
                review_id VARCHAR(100),
                order_id VARCHAR(100),
                review_score INT,
                review_comment_title TEXT,
                review_comment_message TEXT,
                review_creation_date DATETIME,
                review_answer_timestamp DATETIME
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
        """))

        # قائمة الملفات والأسماء
        targets = {
            'olist_sellers_dataset.csv': 'sellers',
            'olist_order_reviews_dataset.csv': 'order_reviews'
        }

        for file_name, table_name in targets.items():
            try:
                print(f"📖 Reading {file_name}...")
                df = pd.read_csv(raw_data_path + file_name)
                
                # تنظيف الحروف تماماً
                for col in df.select_dtypes(include=['object']):
                    df[col] = df[col].astype(str).apply(lambda x: x.encode('utf-8', 'ignore').decode('utf-8'))
                
                print(f"🚀 Pushing {len(df)} rows to {table_name}...")
                # استخدام append لصب البيانات في الجدول اللي بنيناه
                df.to_sql(table_name, con=engine, if_exists='append', index=False, chunksize=1000)
                print(f"✅ {table_name} is finally populated!")
            except Exception as e:
                print(f"❌ Failed {table_name}: {str(e)}")

task = PythonOperator(task_id='master_task', python_callable=master_ingestion, dag=dag)