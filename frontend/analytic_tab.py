import streamlit as st
from datetime import datetime
import pandas as pd
import requests

API_URL="http://localhost:8000/api"
categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

def get_summary():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 10))

    if st.button("Get Analytic"):
        summary_response = requests.get(url=f"{API_URL}/summary/{start_date}/{end_date}")

        if summary_response.status_code == 200:
            summary_data = summary_response.json()
            summary_df = pd.DataFrame(summary_data)

            summary_df_sorted = summary_df.sort_values(by="percentage", ascending=True).round(2)

            st.title("Expense Break Down By Category")
            st.bar_chart(data=summary_df_sorted.set_index("category")['percentage'])

            st.table(summary_df_sorted)