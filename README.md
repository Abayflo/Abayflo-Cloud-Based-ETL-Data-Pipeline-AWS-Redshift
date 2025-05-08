# Cloud-Based ETL Pipeline with AWS

This project demonstrates an end-to-end ETL pipeline that extracts raw data, transforms it using Python, and loads it into an Amazon Redshift data warehouse.

## 🔧 Tech Stack
- AWS S3
- AWS Glue
- Amazon Redshift
- Python (ETL scripts)
- SQL
- Terraform (optional IAC)
- Pandas, boto3

## 🛠 Workflow
1. Extract sample data (e.g., from a public API or local CSV)
2. Store raw data in S3
3. Clean/transform using Python
4. Load into Redshift staging tables
5. Apply transformations using SQL

## 📊 Use Case
Simulates a basic sales dataset pipeline for a retail company — preparing the data for BI and reporting use.

## 📁 Directory Structure
- `etl/`: Python scripts for ETL logic
- `sql/`: Table schema and SQL transformations
- `terraform/`: Optional IAC for Redshift + S3 setup
- `data/`: Sample source data

## 🚀 How to Run
Instructions for setting up AWS credentials, running the ETL scripts, and checking the data in Redshift.
