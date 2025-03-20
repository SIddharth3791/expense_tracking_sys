from .db_config import db_connection_cursor

def fetch_all_expenses():
    with db_connection_cursor() as cursor:
        cursor.execute("select * from expenses")
        expense_data = cursor.fetchall()
        return expense_data

def fetch_expenses_by_date(exp_date):
    with db_connection_cursor() as cursor:
        cursor.execute("select * from expenses where expense_date = %s",(exp_date,))
        expense_data = cursor.fetchall()
        return expense_data

def insert_expense(exp_date, amount, category, note):
    with db_connection_cursor(True) as cursor:
        cursor.execute("Insert INTO expenses(expense_date, amount, category, notes) Values (%s, %s, %s, %s)",
                       (exp_date, amount, category, note))

def delete_expense(exp_date):
    with db_connection_cursor(True) as cursor:
        cursor.execute("Delete FROM expenses WHERE expense_date = %s",(exp_date,))

def fetch_expense_summary(start_exp_date, end_exp_date):
    with db_connection_cursor() as cursor:
        cursor.execute("Select category, sum(amount) as total" +
                                        " From expense_manager.expenses" +
                                        " Where expense_date"+
                                        " Between %s and %s" +
                                        " Group by category", (start_exp_date, end_exp_date))

        summary_data = cursor.fetchall()
        return summary_data

if __name__ == "__main__":
    for data in fetch_expense_summary("2024-08-01","2024-08-30"):
        print(data)