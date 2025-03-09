import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from auth import check_authentication, get_user_id
from common.db_client import DatabaseClient

# Initialize the database client
db_client = DatabaseClient()

def data_analysis_page():
    """Displays the data analysis page with database integration."""

    if not check_authentication():
        st.warning("Please log in to access this page.")
        return

    st.title("Data Analysis")

    st.markdown("""
    <p>Explore and analyze your data with interactive visualizations.</p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # File Upload
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            st.subheader("Data Preview")
            st.dataframe(df.head())

            st.markdown("---")

            # Basic Statistics
            st.subheader("Basic Statistics")
            st.write(df.describe())

            st.markdown("---")

            # Data Visualization
            st.subheader("Data Visualization")

            # Select columns for visualization
            numeric_columns = df.select_dtypes(include=np.number).columns.tolist()
            if not numeric_columns:
                st.warning("No numeric columns found for visualization.")
                return

            x_axis = st.selectbox("Select X-axis", numeric_columns)
            y_axis = st.selectbox("Select Y-axis", numeric_columns)

            if x_axis and y_axis:
                fig, ax = plt.subplots()
                sns.scatterplot(x=x_axis, y=y_axis, data=df, ax=ax)
                st.pyplot(fig)

                st.markdown("---")

            # Histogram
            st.subheader("Histogram")
            hist_column = st.selectbox("Select column for histogram", numeric_columns)
            if hist_column:
                fig, ax = plt.subplots()
                sns.histplot(df[hist_column], ax=ax)
                st.pyplot(fig)

                st.markdown("---")

            # Correlation Heatmap
            st.subheader("Correlation Heatmap")
            corr = df[numeric_columns].corr()
            fig, ax = plt.subplots()
            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

            # Store analysis metadata in the database
            user_id = get_user_id()
            file_name = uploaded_file.name
            analysis_results = f"Analysis of {file_name} completed." # You can store actual results here.
            query = "INSERT INTO data_analysis (user_id, file_name, analysis_results) VALUES (?, ?, ?)"
            db_client.execute_insert(query, (user_id, file_name, analysis_results))

            st.success("Analysis results saved.")

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    data_analysis_page()