import streamlit as st
import pandas as pd
import sqlite3
import os

st.set_page_config(page_title="DataFrame Viewer", layout="wide")
st.title("DataFrame Viewer")

# Input for database file path
db_path = st.text_input("Enter SQLite Database File Path", value="example.db")

# Input for SQL query
sql_query = st.text_area("Enter SQL Query", height=200, value="SELECT * FROM your_table")

if st.button("Execute Query"):
    if not os.path.exists(db_path):
        st.error(f"Database file '{db_path}' not found.")
    else:
        try:
            # Connect to the SQLite database
            conn = sqlite3.connect(db_path)
            # Execute the query and fetch the result into a DataFrame
            df = pd.read_sql_query(sql_query, conn)
            conn.close()

            # Display the DataFrame in Streamlit
            st.write("Query Result:")
            st.dataframe(df)  # Use st.dataframe for better display options
            st.write("Number of Rows:", df.shape[0])
            st.write("Number of Columns:", df.shape[1])
            st.write("Column Names:", df.columns.tolist())
            st.write("Data Types:")
            st.write(df.dtypes.to_dict())
        except Exception as e:
            st.error(f"An error occurred: {e}")