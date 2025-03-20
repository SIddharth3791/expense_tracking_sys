from fastapi import FastAPI
from backend.api import expense_mgmt_api, expense_analytic_api


app = FastAPI()

#Routes
app.include_router(expense_mgmt_api.router, prefix="/api", tags=["Expense_mgmt"])
app.include_router(expense_analytic_api.router, prefix="/api", tags=["Expense_analytic"])

@app.get("/")
def root():
    return {"Message": "Welcome to Expense Tracking Application"}