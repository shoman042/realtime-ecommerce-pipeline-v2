import pandas as pd
import os

# المسار اللي فيه الملفات بعد ما فكيت الضغط
path = 'D:raw_data/'

# أهم 3 جداول هنبدأ بيهم
files = [
    'olist_customers_dataset.csv',
    'olist_orders_dataset.csv',
    'olist_order_items_dataset.csv'
]

for file in files:
    full_path = os.path.join(path, file)
    df = pd.read_csv(full_path)
    
    print(f"--- Exploring: {file} ---")
    print(f"Shape: {df.shape}") # بيعرفك عدد الصفوف والأعمدة
    print(f"Columns: {list(df.columns)}")
    print(f"Missing Values: \n{df.isnull().sum()}") # بيعرفك لو في داتا ناقصة
    print("\n")