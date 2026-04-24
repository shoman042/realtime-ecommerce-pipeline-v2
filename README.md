# 🚀 Real-Time E-Commerce Data Pipeline (V2)

### **End-to-End Data Engineering Project | Olist Dataset**

---

## 🏗️ Project Overview

This project implements a scalable **Real-Time ETL Pipeline** using the Medallion Architecture. It processes live e-commerce transactions, handles data transformations on the fly, and ensures data integrity through professional orchestration and containerization.

---

## 🛠️ Tech Stack (Detailed Explanation)

### 1. **Apache Kafka (Message Broker)**

* **Function:** Handles real-time data streaming and acts as a distributed message queue.
* **When to use:** For high-throughput, real-time streaming data systems.
* **Why used:** Acts as a buffer between producers and Spark to ensure no data loss.
* **Implementation:** Created `orders_topic` to stream JSON transaction data.

---

### 2. **Apache Spark (PySpark) – Processing Engine**

* **Function:** Processes and transforms big data efficiently using in-memory computation.
* **When to use:** For large-scale data transformation and real-time analytics.
* **Why used:** Used Spark Structured Streaming to clean and transform incoming Kafka data.
* **Implementation:** Converts raw data into structured, clean datasets (Silver Layer).

---

### 3. **Apache Airflow (Orchestrator)**

* **Function:** Manages and schedules workflows programmatically.
* **When to use:** When handling dependent tasks in automated pipelines.
* **Why used:** Automates pipeline execution and handles retries on failure.
* **Implementation:** DAGs created to control workflow execution.

---

### 4. **Docker & Docker Compose (Infrastructure)**

* **Function:** Containerization for consistent environments.
* **When to use:** To avoid environment conflicts and simplify deployment.
* **Why used:** Runs Kafka, Spark, MySQL, and Airflow in isolated containers.
* **Implementation:** `docker-compose.yml` defines all services and networking.

---

### 5. **MySQL (Data Warehouse - Serving Layer)**

* **Function:** Stores structured, processed data for analysis.
* **When to use:** As a reliable storage layer for analytics and reporting.
* **Why used:** Serves as final destination for cleaned data.
* **Implementation:** Spark connects via JDBC to load processed data.

---

## 📁 Repository Structure

* `/scripts` → Python Producers & PySpark Streaming jobs
* `/dags` → Airflow DAGs
* `/docker` → Docker configuration files
* `.gitignore` → Excludes datasets and unnecessary files

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/shoman042/realtime-ecommerce-pipeline-v2.git
```

### 2. Start Infrastructure

```bash
cd docker
docker-compose up -d
```

### 3. Run Data Ingestion

Execute Python scripts inside `/scripts` to start streaming data into Kafka.

### 4. Monitor Pipeline

Open Airflow UI:

```
http://localhost:8080
```

---

## 👨‍💻 Author

**Yusuf Shoman**
Computer Engineering Student @ Tanta University

🔗 GitHub: https://github.com/shoman042
