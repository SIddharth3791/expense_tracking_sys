from .db_config import db_connection_cursor
from ..logging_utils import setup_logger

logger = setup_logger("Expense_Repository")

def fetch_all_expenses():
    logger.info("FETCHING ALL EXPENSES")
    with db_connection_cursor() as cursor:
        cursor.execute("select * from expenses")
        expense_data = cursor.fetchall()
        return expense_data

def fetch_expenses_by_date(exp_date):
    logger.info(f"FETCHING EXPENSES FOR THE DATE: {exp_date}")
    with db_connection_cursor() as cursor:
        cursor.execute("select * from expenses where expense_date = %s",(exp_date,))
        expense_data = cursor.fetchall()
        return expense_data

def insert_expense(exp_date, amount, category, note):
    logger.info(f"INSERT NEW EXPENSE :: Date - {exp_date}, amount - {amount}, category - {category}, note - {note} ")
    with db_connection_cursor(True) as cursor:
        cursor.execute("Insert INTO expenses(expense_date, amount, category, notes) Values (%s, %s, %s, %s)",
                       (exp_date, amount, category, note))

def delete_expense(exp_date):
    logger.info(f"DELETE ALL EXPENSE FOR DATE: {exp_date}")
    with db_connection_cursor(True) as cursor:
        cursor.execute("Delete FROM expenses WHERE expense_date = %s",(exp_date,))

def fetch_expense_summary(start_exp_date, end_exp_date):
    logger.info(f"FETCH ALL EXPENSE SUMMARY FOR START DATE: {start_exp_date} - END DATE: {end_exp_date}")
    with db_connection_cursor() as cursor:
        cursor.execute("Select category, sum(amount) as total" +
                                        " From expense_manager.expenses" +
                                        " Where expense_date"+
                                        " Between %s and %s" +
                                        " Group by category", (start_exp_date, end_exp_date))

        summary_data = cursor.fetchall()
        return summary_data