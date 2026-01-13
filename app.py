# STEP 4: Generic Streamlit Dashboard for Any Dataset

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# -------------------------------
# PostgreSQL connection details
# -------------------------------
DATABASE_URL = "postgresql://etl_warehouse_user:lmHfpsZBHL7zkCXMnzH8fpw1BcPQAVVl@dpg-d5drekqli9vc73do4fa0-a.oregon-postgres.render.com/etl_warehouse"

engine = create_engine(DATABASE_URL)

st.set_page_config(page_title="Generic ETL Dashboard", layout="wide")
st.title("📊 Generic Data Pipeline Dashboard")

# -------------------------------
# Fetch available tables
# -------------------------------
query_tables = """
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
"""

tables = pd.read_sql(query_tables, engine)['table_name'].tolist()

if not tables:
    st.warning("No tables found in the database.")
    st.stop()

table_name = st.selectbox("Select a table", tables)

# -------------------------------
# Load selected table
# -------------------------------
df = pd.read_sql(f"SELECT * FROM {table_name}", engine)

st.subheader("Dataset Preview")
st.dataframe(df.head())

# -------------------------------
# Dataset Summary
# -------------------------------
st.subheader("Dataset Summary")
st.write(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
st.write("Column Names:", list(df.columns))

# -------------------------------
# Numeric Column Analysis
# -------------------------------
numeric_cols = df.select_dtypes(include='number').columns.tolist()

if numeric_cols:
    st.subheader("Numeric Analysis")

    col = st.selectbox("Select numeric column", numeric_cols)

    chart_type = st.radio(
        "Select visualization type",
        ["Histogram", "Line Chart", "Bar Chart"]
    )

    if chart_type == "Histogram":
        st.bar_chart(df[col].value_counts().sort_index())

    elif chart_type == "Line Chart":
        st.line_chart(df[col])

    elif chart_type == "Bar Chart":
        st.bar_chart(df[col])

    st.subheader("Summary Statistics")
    st.write(df[col].describe())

else:
    st.info("No numeric columns available for analysis.")

# -------------------------------
# Categorical Column Analysis
# -------------------------------
categorical_cols = df.select_dtypes(include='object').columns.tolist()

if categorical_cols:
    st.subheader("Categorical Analysis")

    cat_col = st.selectbox("Select categorical column", categorical_cols)

    st.bar_chart(df[cat_col].value_counts())

# -------------------------------
# Correlation Analysis
# -------------------------------
if len(numeric_cols) > 1:
    st.subheader("Correlation Matrix")
    corr = df[numeric_cols].corr()
    st.dataframe(corr)
