class Expense:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date

class Budget:
    def __init__(self, category, limit):
        self.category = category
        self.limit = limit
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def calculate_remaining(self):
        total_expenses = sum(expense.amount for expense in self.expenses)
        remaining = self.limit - total_expenses
        return remaining

budget = Budget("1", 500)

expense1 = Expense("1", 50, "2024-05-12")
expense2 = Expense("2", 100, "2024-05-10")

budget.add_expense(expense1)
budget.add_expense(expense2)

remaining = budget.calculate_remaining()

print(f"Оставшийся лимит для категории '{budget.category}': {remaining}")
