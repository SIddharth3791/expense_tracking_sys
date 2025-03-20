import streamlit as st
from datetime import datetime
import requests

API_URL="http://localhost:8000"
categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]
st.title("Expense Management System")
tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

expenses = []
with tab1:
    selected_date = st.date_input("Select Date",datetime(2024,8,1))
    response = requests.get(url=f"{API_URL}/expense/{selected_date}")
    if response.status_code == 200:
        expense_data = response.json()
    else:
        st.error("FAILED TO RETRIEVE DATA")
        expense_data = []

    with st.form(key="expense_form"):

        col1, col2, col3 = st.columns(3)

        with col1:
            col1.subheader("Anount")
        with col2:
            col2.subheader("Category")
        with col3:
            col3.subheader("Notes")

        for i in range(5):
            if i < len(expense_data):
                amount = expense_data[i]['amount']
                category = expense_data[i]['category']
                notes = expense_data[i]['notes']
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            with col1:
                amount_input = st.number_input(label="Anount", min_value=0.0, step=1.0, value=amount, key=f"amount_{i}", label_visibility="collapsed")
            with col2:
                category_input = st.selectbox(label="Category", options=categories, index=categories.index(category),  key=f"category_{i}", label_visibility="collapsed")
            with col3:
                notes_input = st.text_input(label="Notes", value=notes, key=f"notes_{i}", label_visibility="collapsed")

            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })

        submit_button = st.form_submit_button()
        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense['amount']>0]
            submit_response = requests.post(url=f"{API_URL}/expense/{selected_date}", json=filtered_expenses)

            if submit_response.status_code == 200:
                st.success("Expenses Updated Successfully!!!!!")
            else:
                st.error("Failed to Update Expenses")
