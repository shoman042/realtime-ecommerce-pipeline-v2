# 🚀 Real-Time E-Commerce Data Pipeline (V2)
### **End-to-End Data Engineering Project | Olist Dataset**

---

## 🏗️ Project Overview
This project implements a scalable **Real-Time ETL Pipeline** using the Medallion Architecture. It processes live e-commerce transactions, handles data transformations on the fly, and ensures data integrity through professional orchestration and containerization.

---

## 🛠️ الأدوات المستخدمة: الشرح التفصيلي (Tech Stack)

### 1. **Apache Kafka (وسيط الرسائل - Message Broker)**
* **الوظيفة (Function):** يعمل كمنصة لنقل البيانات الضخمة والرسائل اللحظية بسرعة عالية وتخزينها بشكل مؤقت.
* **متى نستخدمها (When to use):** نستخدمها عندما نتعامل مع "بيانات متدفقة" (Streaming Data) بسرعة كبيرة، ونحتاج لضمان عدم ضياع أي بيان في حالة توقف أو بطء النظام المعالج.
* **لماذا استخدمتها هنا؟ (Why here):** لتعمل كـ **Buffer** (مخزن مؤقت) بين سكريبتات إنتاج البيانات (Producers) ومحرك المعالجة (Spark). هذا يضمن استمرارية تدفق بيانات الطلبات (Orders) حتى لو كان هناك ضغط عالي على المعالجة.
* **التنفيذ (How):** قمت بإنشاء `orders_topic` لاستقبال بيانات المعاملات بصيغة JSON وتوزيعها على المشتركين.

### 2. **Apache Spark - PySpark (محرك المعالجة - Processing Brain)**
* **الوظيفة (Function):** محرك موحد لتحليل ومعالجة البيانات الضخمة (Big Data) بسرعة فائقة في الذاكرة (In-Memory).
* **متى نستخدمها (When to use):** عندما نحتاج لإجراء عمليات تحويل وتنظيف معقدة (Transformations) على كميات هائلة من البيانات في وقت قياسي أو لحظي.
* **لماذا استخدمتها هنا؟ (Why here):** استخدمت تقنية **Spark Structured Streaming** لقراءة البيانات فور وصولها لكافكا، والقيام بتنظيفها (Cleaning)، وتصحيح أنواع البيانات، وفلترة القيم الناقصة قبل تخزينها.
* **التنفيذ (How):** تطوير منطق برمجى بلغة Python لتحويل البيانات الخام إلى بيانات مهيأة للتحليل (Silver Layer).

### 3. **Apache Airflow (المنظم - The Orchestrator)**
* **الوظيفة (Function):** منصة لإدارة وجدولة ومراقبة مسارات العمل (Workflows) برمجياً.
* **متى نستخدمها (When to use):** عندما يكون لدينا سلسلة من المهام المعتمدة على بعضها البعض (Dependencies) ونريد أتمتة تشغيلها ومراقبة فشلها أو نجاحها.
* **لماذا استخدمتها هنا؟ (Why here):** لتحويل المشروع من مجرد أكواد يدوية إلى **Pipeline** احترافي يعمل تلقائياً. الأيرفلو يضمن تشغيل سكريبتات سحب البيانات في مواعيد محددة وإعادة المحاولة (Retry) في حالة الفشل.
* **التنفيذ (How):** إنشاء **DAGs** تنظم ترتيب تشغيل المهام وتراقب حالة النظام.

### 4. **Docker & Docker Compose (البنية التحتية - Infrastructure)**
* **الوظيفة (Function):** تقنية الحاويات التي تتيح تشغيل البرامج في بيئات معزولة تماماً تضمن عمل الكود على أي جهاز.
* **متى نستخدمها (When to use):** عندما نريد تجنب مشاكل "اختلاف الإعدادات بين الأجهزة" (It works on my machine) ولتسهيل تنصيب الأدوات المعقدة.
* **لماذا استخدمتها هنا؟ (Why here):** لتشغيل منظومة كاملة (Kafka, Spark, MySQL, Airflow) بضغطة زر واحدة، مما يضمن أن المشروع سيعمل بنفس الكفاءة عند أي مهندس آخر.
* **التنفيذ (How):** صياغة ملف `docker-compose.yml` يحدد الشبكات، الأحجام (Volumes)، والمنافذ (Ports) لكل أداة.

### 5. **MySQL (مستودع البيانات - The Serving Layer)**
* **الوظيفة (Function):** قاعدة بيانات علائقية موثوقة لتخزين البيانات المنظمة.
* **متى نستخدمها (When to use):** عندما نحتاج لمصدر نهائي للمعلومات (Source of Truth) يكون جاهزاً للربط مع أدوات تحليل البيانات مثل Power BI أو Tableau.
* **لماذا استخدمتها هنا؟ (Why here):** لتعمل كمستقر نهائي للبيانات "النظيفة" بعد معالجتها، مما يسمح للمحللين بكتابة استعلامات SQL واستخراج تقارير الأعمال بسهولة.
* **التنفيذ (How):** ربط Spark بقاعدة البيانات باستخدام **JDBC Connectors** لنقل البيانات المعالجة لحظياً.

---

## 📁 Repository Structure
* **`/scripts`**: Python Producers and PySpark Streaming jobs.
* **`/dags`**: Airflow DAG definitions for workflow automation.
* **`/docker`**: Infrastructure as Code (Docker-Compose files).
* **`.gitignore`**: Optimized to exclude heavy datasets (`.csv`) and local caches.

---

## 🚀 Getting Started
1.  **Clone the Repo:** ```bash
    git clone [https://github.com/shoman042/realtime-ecommerce-pipeline-v2.git](https://github.com/shoman042/realtime-ecommerce-pipeline-v2.git)
    ```
2.  **Spin up Infra:** ```bash
    cd docker && docker-compose up -d
    ```
3.  **Run Ingestion:** Execute the Python scripts in `/scripts` to begin streaming data to Kafka.
4.  **Monitor:** Access Airflow UI at `localhost:8080` to track the pipeline tasks.

---
**Developed by:** [Yusuf Shoman](https://github.com/shoman042)  
*Computer Engineering Student @ Tanta University*
