# 🏦 Modern Bank Reviews Data Warehouse

An end-to-end ELT pipeline for collecting, processing, transforming, and visualizing bank customer reviews using modern Data Engineering tools.

## 📌 Project Overview

This project automates the complete data pipeline for customer reviews of Moroccan banks.

The pipeline performs:

- Web scraping of Google Maps reviews using Playwright
- Natural Language Processing (language detection, sentiment analysis, keyword extraction, topic modeling)
- Loading raw data into PostgreSQL
- Data transformation with dbt
- Workflow orchestration with Apache Airflow
- Business Intelligence dashboard with Power BI

---

## 🏗️ Architecture

```text
                   Airflow
                      │
                      ▼
        Playwright Scraper (Docker)
                      │
                      ▼
              PostgreSQL (Raw Data)
                      │
                      ▼
               NLP Processing
                      │
                      ▼
             dbt Transformations
                      │
                      ▼
               Data Warehouse
                      │
                      ▼
                 Power BI Dashboard
```

---

# 🛠️ Tech Stack

- Python
- Playwright
- PostgreSQL
- Apache Airflow
- dbt
- Docker & Docker Compose
- Power BI
- Pandas
- Transformers
- KeyBERT
- Sentence Transformers
- LangDetect

---

# 📂 Project Structure

```text
.
├── bank_reviews_dbt/
├── dags/
├── src/
│   ├── scraping/
│   ├── nlp/
│   └── database/
├── dashboard/
├── config/
├── plugins/
├── logs/
├── Dockerfile
├── docker-compose.yaml
├── requirements-airflow.txt
├── requirements.txt
└── README.md
```

---

# 🚀 Features

- Automated Google Maps review scraping
- Language detection
- Sentiment Analysis
- Keyword Extraction
- Topic Modeling
- PostgreSQL data storage
- dbt data transformations
- Automated Airflow orchestration
- Interactive Power BI dashboard

---

# ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
cd modern-bank-reviews-data-warehouse
```

Build Docker images

```bash
docker compose build
```

Start services

```bash
docker compose up -d
```

Open Airflow

```
http://localhost:8080
```

Default credentials

```
Username: airflow
Password: airflow
```

---

# ▶️ Pipeline

The Airflow DAG executes the following tasks:

1. Scraping
2. NLP Processing
3. dbt Run
4. dbt Tests

---

# 📊 Dashboard

The Power BI dashboard provides:

- Sentiment distribution
- Reviews over time
- Bank comparison
- Rating analysis
- Language distribution
- Keyword analysis
- Topic analysis

---

# 📷 Screenshots

You can add screenshots here.

Example:

```
dashboard/screenshots/dashboard.png
```

---

# 👩‍💻 Author

**Soumia**

Data & Software Engineering Student

