n = int(input())
transactions = []

for i in range(n):
    transaction_id = input().strip()
    amount = float(input())
    transactions.append((transaction_id, amount))

threshold = float(input())

seen = set()
duplicates = set()
suspicious = []

for transaction_id, amount in transactions:
    reasons = []

    if transaction_id in seen:
        duplicates.add(transaction_id)
        reasons.append("Duplicate transaction")
    else:
        seen.add(transaction_id)

    if amount > threshold:
        reasons.append("Threshold exceeded")

    if reasons:
        suspicious.append((transaction_id, amount, reasons))

print("Duplicate Transactions:")
for transaction_id in sorted(duplicates):
    print(transaction_id)

print("Suspicious Entries:")
for transaction_id, amount, reasons in suspicious:
    print(f"{transaction_id} {amount:.2f}: {', '.join(reasons)}")