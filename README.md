# Generic End-to-End Data Pipeline (ETL) Project

## Project Overview
This project demonstrates the design and implementation of a **generic, end-to-end data pipeline** that processes **any CSV dataset** using a complete **ETL (Extract, Transform, Load)** workflow. The pipeline ingests raw data, applies automated transformations, stores the processed data in a cloud-hosted open-source data warehouse, and enables interactive data visualization through a dashboard.

The project is designed to be **dataset-agnostic**, **scalable**, and **industry-aligned**, focusing entirely on **open-source tools** commonly used in real-world data engineering workflows.

---

## Objectives
- Build a reusable data pipeline that accepts **any CSV dataset**
- Implement a structured **Data Lake** with raw and processed layers
- Apply **generic ETL transformations** without hardcoding schema
- Load transformed data into an **open-source data warehouse**
- Enable **interactive data analysis and visualization**
- Follow modular and cost-efficient data engineering practices

---

## System Architecture
CSV Dataset
↓
Data Lake (Raw Layer)
↓
ETL Transformation (Python)
↓
Data Lake (Processed Layer)
↓
PostgreSQL Data Warehouse
↓
Streamlit Dashboard


---

## ETL Pipeline Description

### Extract
- Any CSV dataset can be ingested into the pipeline
- Raw data is stored **unchanged** in the Data Lake (raw layer)
- Dataset metadata such as row count, column names, data types, and missing values is captured

### Transform
- Column names are standardized automatically
- Duplicate records are removed
- Missing values are handled using generic rules
- Numeric, categorical, and date columns are detected dynamically
- Transformed data is saved to the Data Lake (processed layer)

### Load
- Processed data is loaded into a **PostgreSQL data warehouse**
- Tables are created automatically based on dataset structure
- Data loading is verified using SQL queries

### Visualize
- A Streamlit dashboard connects directly to the PostgreSQL database
- Tables and columns are discovered dynamically
- Users can explore data interactively using summaries and visualizations

---

## Tools and Technologies Used

- **Programming Language:** Python  
- **Data Processing:** Pandas, NumPy  
- **Data Lake:** File-based storage (Raw and Processed layers)  
- **Data Warehouse:** PostgreSQL  
- **Visualization:** Streamlit  
- **Version Control:** Git and GitHub  
- **Deployment:** Local execution / Open-source cloud database  

---

## Key Features
- Works with **any CSV dataset**
- No hardcoded schema or column names
- Fully automated ETL pipeline
- Open-source data warehouse integration
- Interactive analytics dashboard
- Resume-ready, industry-aligned project





