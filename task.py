
budget = float(input())
n = int(input())

expenses = {}

for i in range(n):
    category = input()
    amount = float(input())
    rate = float(input())
    fee_percent = float(input())

    converted = amount * rate
    fee = converted * fee_percent / 100
    total = converted + fee

    expenses[category] = expenses.get(category, 0) + total

total_spending = sum(expenses.values())

print(f"Total Spending: {total_spending:.2f}")

if total_spending <= budget:
    print(f"Remaining Budget: {budget - total_spending:.2f}")
else:
    print(f"Budget Exceeded: {total_spending - budget:.2f}")

if expenses:
    largest = max(expenses, key=expenses.get)
    print(f"Largest Expense: {largest}")
