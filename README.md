# 🚀 Real-Time E-Commerce Data Pipeline (V2)
**End-to-End Data Engineering Project | Olist Dataset**

## 📌 Overview
This project demonstrates a robust real-time ETL pipeline. It ingests e-commerce data, processes it on the fly, and stores it in a structured format for analysis, all managed within a containerized environment.

## 🏗️ Architecture & Tools
🛠️ Tech Stack & Tool Justification
1. Apache Kafka (The Backbone)
Role: Distributed Message Broker / Data Ingestion.

Why I used it? In real-world e-commerce, thousands of orders happen every second. Kafka acts as a buffer. Even if our processing engine (Spark) slows down, Kafka stores the messages safely, ensuring Zero Data Loss. It decouples the data source (Producer) from the processing layer.

2. Apache Spark - PySpark (The Brain)
Role: Real-time Stream Processing.

Why I used it? I used Spark Structured Streaming because of its high throughput and low latency. Unlike traditional batch processing, Spark processes each order the moment it arrives in Kafka, performing real-time cleaning and schema enforcement.

3. Apache Airflow (The Conductor)
Role: Workflow Orchestration.

Why I used it? Managing multiple Python scripts manually is inefficient. I used Airflow to automate the ingestion tasks and monitor the pipeline. If a task fails, Airflow handles the retries and alerts me, making the pipeline "production-ready."

4. Docker & Docker Compose (The Infrastructure)
Role: Containerization & Orchestration.

Why I used it? Setting up Spark, Kafka, and MySQL locally is a configuration nightmare. Docker ensures that this entire pipeline can run on any machine (Windows, Linux, Mac) with a single command: docker-compose up. It provides perfect isolation between tools.

5. MySQL (The Storage Layer)
Role: Relational Database (Data Sink).

Why I used it? Once the data is cleaned by Spark, it needs to be stored in a structured format. MySQL is perfect for this "Silver/Gold" layer, allowing Data Analysts to write SQL queries or connect BI tools like Power BI to visualize the results.

## 📁 Project Structure
- `scripts/`: Python scripts for data production and Spark processing.
- `dags/`: Airflow directed acyclic graphs for automation.
- `docker/`: Infrastructure configuration files.
- `raw_data/`: (Ignored via .gitignore) Dataset source.

## ⚙️ How to Run
1. Clone the repo.
2. Navigate to `docker/` and run `docker-compose up -d`.
3. Start the Python producer in `scripts/`.
4. Submit the Spark job via Docker exec.
