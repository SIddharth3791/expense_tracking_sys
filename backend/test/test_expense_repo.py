from backend.repositories import expenses_repository


def test_fetch_expenses_by_date():
    expense = expenses_repository.fetch_expenses_by_date("2024-08-15")
    assert len(expense) == 1
    assert expense[0]["amount"] == 10
    assert  expense[0]["category"] == "Shopping"

def test_invalid_fetch_expenses_by_date():
    expense = expenses_repository.fetch_expenses_by_date("2099-01-01")
    assert len(expense) == 0

def test_fetch_all_expenses():
    exenses_data = expenses_repository.fetch_all_expenses()
    assert len(exenses_data) > 10

def test_fetch_expense_summary():
    exp_summary = expenses_repository.fetch_expense_summary("2024-08-01", "2024-08-30")
    assert len(exp_summary) == 5
    assert exp_summary[0]["category"] == "Entertainment"
    assert exp_summary[0]["total"] == 305.0

def test_fetch_expense_summary_invalid_date():
    exp_summary = expenses_repository.fetch_expense_summary("2099-08-01", "2099-08-30")
    assert len(exp_summary) == 0