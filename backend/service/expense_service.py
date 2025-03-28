from  datetime import  date
from typing import  List
from backend.model.expense import Expense
from backend.model.expense_summary import ExpenseSummary
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

def fetch_expense_summary(start_exp_date: date, end_exp_date: date):
    db_data_summary = expense_repository.fetch_expense_summary(start_exp_date,end_exp_date)
    exp_summary = ExpenseSummary(summary=db_data_summary)
    # Count Total Expense
    total_exp = sum(exp['total'] for exp in exp_summary.summary)

    summary_breakdown={
        "category" : [],
        "total" : [],
        "percentage" : []
    }
    # Update Each Category With Percentage
    for exp in exp_summary.summary:
        summary_breakdown['category'].append(exp['category'])
        summary_breakdown['total'].append(exp['total'])
        summary_breakdown['percentage'].append(round((exp['total'] * 100) / total_exp, 2))
    return summary_breakdown

def fetch_summary_by_months():
    return expense_repository.fetch_expense_summary_by_month()