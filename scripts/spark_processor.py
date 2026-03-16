from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

spark = SparkSession.builder.appName("Olist_Streaming").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("order_id", StringType(), True),
    StructField("customer_id", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("order_status", StringType(), True)
])

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka_yusuf:9092") \
    .option("subscribe", "olist_orders") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING) as json_payload") \
    .select(from_json(col("json_payload"), schema).alias("data")) \
    .select("data.*")

def write_to_mysql(batch_df, batch_id):
    if batch_df.count() > 0:
        batch_df.write \
            .format("jdbc") \
            .option("url", "jdbc:mysql://mysql_yusuf:3306/olist_db") \
            .option("driver", "com.mysql.cj.jdbc.Driver") \
            .option("dbtable", "silver_orders") \
            .option("user", "root") \
            .option("password", "root") \
            .mode("append").save()
        print(f"✅ Batch {batch_id} - {batch_df.count()} records saved!")

query = json_df.writeStream.foreachBatch(write_to_mysql).start()
query.awaitTermination()