import streamlit as st
from datetime import datetime
import requests

from add_expense_tab import add_update_exp
from analytic_tab import get_summary

API_URL="http://localhost:8000/api"
st.title("Expense Management System")
tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
    add_update_exp()
with tab2:
    get_summary()