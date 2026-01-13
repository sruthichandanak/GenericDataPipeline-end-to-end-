Generic End-to-End Data Pipeline (ETL) Project

Project Overview
This project demonstrates the design and implementation of a generic, end-to-end data pipeline that processes any CSV dataset through a complete ETL (Extract, Transform, Load) workflow. The pipeline ingests raw data, applies automated transformations, stores the processed data in a cloud data warehouse, and enables interactive data visualization through a dashboard.
The project is dataset-agnostic, scalable, and industry-aligned, showcasing real-world data engineering practices using open-source tools and cloud services.

Objectives
• Build a reusable data pipeline that accepts any CSV dataset
• Implement a structured Data Lake with raw and processed layers
• Apply generic ETL transformations without hardcoding schema
• Load cleaned data into a cloud-hosted data warehouse
• Enable interactive data analysis and visualization
• Design a cloud-agnostic and cost-efficient architecture

System Architecture
CSV Dataset
↓
Data Lake (Raw Layer)
↓
ETL Transformation (Python)
↓
Data Lake (Processed Layer)
↓
Cloud Data Warehouse (PostgreSQL)
↓
Visualization Dashboard (Streamlit)

ETL Pipeline Description

Extract
• Any CSV file is ingested into the pipeline
• Raw data is stored unchanged in the Data Lake (raw layer)
• Dataset metadata such as row count, column names, data types, and missing values is captured

Transform
• Column names are standardized automatically
• Duplicate records are removed
• Missing values are handled using generic rules
• Numeric, categorical, and date columns are detected dynamically
• Transformed data is saved to the Data Lake (processed layer)

Load
• Processed data is loaded into a cloud-hosted PostgreSQL data warehouse
• Database tables are created automatically
• Data load is verified using SQL queries

Visualize
• A Streamlit dashboard connects directly to the data warehouse
• Available tables and columns are discovered dynamically
• Users can explore data interactively through summaries and visualizations

Tools and Technologies Used
Programming Language: Python
Data Processing: Pandas, NumPy
Data Lake: File-based (Raw and Processed layers)
Data Warehouse: PostgreSQL (cloud-hosted)
Visualization: Streamlit
Version Control: Git and GitHub
Cloud Platforms: Render PostgreSQL, Azure (planned extension)

Key Features
• Works with any CSV dataset
• No hardcoded schema or column names
• Automated ETL workflow
• Cloud-based data warehouse
• Interactive analytics dashboard
• Resume-ready, industry-aligned project
