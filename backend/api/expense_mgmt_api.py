from fastapi import APIRouter
from datetime import date
from typing import  List
from backend.model.expense import Expense
from backend.service import expense_service

router = APIRouter()

@router.get("/expense/all")
def fetch_all():
    return expense_service.fetch_all_expenses()

@router.get("/expense/{expense_date}", response_model=List[Expense])
def fetch_expense_date(expense_date:date):
    return expense_service.fetch_expenses_by_date(expense_date)

@router.post("/expense/{expense_date}")
def add_or_update_expense_data(expense_date: date , expenses:List[Expense] ):
    return expense_service.add_or_update_expense_data(expense_date, expenses)

