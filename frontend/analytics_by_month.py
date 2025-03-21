import streamlit as st
import pandas as pd
import requests

API_URL = "http://localhost:8000/api/summary/month"

def get_summary_month():

    st.title("Expense Breakdown By Month")

    summary_response = requests.get(url=API_URL)

    if summary_response.status_code == 200:

        expense_summary_data = summary_response.json()

        df_month = pd.DataFrame(expense_summary_data)

        df_month = df_month.rename(columns={'month_name': 'Months'})
        df_month = df_month.rename(columns={'year_number': 'Year'})
        # df_month_sorted = df_month.sort_values(by=['Months','Year'])
        st.bar_chart(df_month.set_index("Months")['total'])

        st.table(df_month)

