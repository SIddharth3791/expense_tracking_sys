from  datetime import  date
from typing import  List
from backend.model.expense import Expense
from backend.repositories import expense_repository


def fetch_all_expenses():
    return expense_repository.fetch_all_expenses()

def fetch_expenses_by_date(expense_date: date):
    return expense_repository.fetch_expenses_by_date(expense_date)

def add_or_update_expense_data(expense_date: date , expenses:List[Expense] ):
    try:
        # Delete Before Saving
        expense_repository.delete_expense(expense_date)
        # Save All New Expenses
        for exp in expenses:
            expense_repository.insert_expense(expense_date, exp.amount,exp.category, exp.notes)
        return "Expenses Saved Successfully"
    except Exception as err:
        return f"Error While Saving Expenses {err}"
