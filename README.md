# 🚀 Real-Time E-Commerce Data Pipeline (V2)
**End-to-End Data Engineering Project | Olist Dataset**

## 📌 Overview
This project demonstrates a robust real-time ETL pipeline. It ingests e-commerce data, processes it on the fly, and stores it in a structured format for analysis, all managed within a containerized environment.

## 🏗️ Architecture & Tools
- **Apache Kafka:** Real-time message streaming.
- **Apache Spark (PySpark):** Stream processing and data transformation.
- **Apache Airflow:** Workflow orchestration and scheduling.
- **MySQL:** Persistent storage for processed data.
- **Docker & Docker Compose:** Infrastructure management.

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
