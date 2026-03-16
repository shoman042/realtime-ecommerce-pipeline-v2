🚀 Real-Time E-Commerce Data Pipeline (V2)
End-to-End Data Engineering Project | Olist Dataset
📌 Project Overview
This project implements a scalable Real-Time ETL Pipeline using the Medallion Architecture. It processes live e-commerce transactions, handles data transformations on the fly, and ensures data integrity through professional orchestration and containerization.

🛠️ Tech Stack: Why, When, and How?
1. Apache Kafka (The Message Broker)
Function: High-throughput, distributed messaging system.

When to use: When dealing with high-velocity data (streaming) where data loss is not an option.

Why in this project? It acts as a buffer between the data producer and the processing engine. It ensures that even if Spark faces a delay, the order data is safely stored in Topics.

Implementation: Used a dedicated orders_topic where Python producers stream JSON-formatted transaction data.

2. Apache Spark - PySpark (The Processing Brain)
Function: Unified analytics engine for large-scale data processing.

When to use: When you need to perform complex transformations (Cleaning, Aggregations) on massive datasets in real-time.

Why in this project? Used Spark Structured Streaming to consume Kafka messages instantly, enforce data schemas, and clean the data before it reaches the database.

Implementation: Developed a transformation logic to convert data types, filter null values, and join streams.

3. Apache Airflow (The Orchestrator)
Function: Platform to programmatically author, schedule, and monitor workflows.

When to use: When you have a multi-step pipeline and need to manage dependencies, retries, and scheduling.

Why in this project? To automate the entire flow. Instead of manual execution, Airflow DAGs manage the timing and order of data ingestion tasks.

Implementation: Created DAGs to trigger ingestion scripts and monitor the health of the pipeline.

4. Docker & Docker Compose (Infrastructure)
Function: OS-level virtualization to deliver software in packages called containers.

When to use: When you want a consistent environment across different machines (Development vs. Production).

Why in this project? To avoid "dependency hell." It allows Kafka, Spark, and MySQL to run in isolated environments with a single command.

Implementation: Defined a multi-container architecture in docker-compose.yml managing networking and port mapping.

5. MySQL (The Serving Layer)
Function: Reliable Relational Database Management System (RDBMS).

When to use: When you need a structured "Source of Truth" for cleaned data that BI tools (like Power BI) can easily query.

Why in this project? It serves as the Gold/Silver Layer where processed data is stored, making it ready for downstream analytical queries.

Implementation: Connected Spark to MySQL using JDBC Connectors for real-time data sinking.

📁 Repository Structure
/scripts: Python Producers and PySpark Streaming jobs.

/dags: Airflow DAG definitions for workflow automation.

/docker: Infrastructure as Code (Docker-Compose files).

.gitignore: Optimized to exclude heavy datasets (.csv) and local caches.

🚀 Getting Started
Clone the Repo: git clone https://github.com/shoman042/realtime-ecommerce-pipeline-v2.git

Spin up Infra: docker-compose up -d

Run Ingestion: Execute the Python scripts in /scripts to begin streaming.

Monitor: Access Airflow UI at localhost:8080 to track the pipeline.

Developed by: Yusuf Shoman
Computer Engineering Student @ Tanta University
