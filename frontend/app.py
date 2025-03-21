import streamlit as st
from datetime import datetime
import requests

from add_expense_tab import add_update_exp
from analytic_tab import get_summary_category
from analytics_by_month import get_summary_month

API_URL="http://localhost:8000/api"
st.title("Expense Management System")
tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics By Category", "Analytics By Month"])

with tab1:
    add_update_exp()
with tab2:
    get_summary_category()
with tab3:
    get_summary_month()