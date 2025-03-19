# from fastapi import FastAPI
# from datetime import date
#
# from repositories import expenses_repository
#
# app = FastAPI()
#
# @app.get("/expense/{expense_date}")
# def fetch_expense_date(expense_date:date):
#     return expenses_repository.fetch_expenses_by_date(expense_date)