from fastapi import APIRouter
from datetime import date
from backend.service import expense_service

router = APIRouter()

@router.get("/summary/category/{start_exp_date}/{end_exp_date}")
def get_summary(start_exp_date: date, end_exp_date: date):
    return expense_service.fetch_expense_summary(start_exp_date, end_exp_date)

@router.get("/summary/month")
def fetch_summary_by_months():
    return expense_service.fetch_summary_by_months()