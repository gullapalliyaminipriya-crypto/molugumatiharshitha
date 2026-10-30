
# Library Borrowing and Fine Reconciliation

# Tuple format:
# (Book ID, Borrowing Days, Return Status)

books = [
    ("B101", 18, True),
    ("B102", 10, True),
    ("B103", 20, False),
    ("B104", 14, True),
    ("B105", 17, True)
]

BORROWING_LIMIT = 14
FINE_PER_DAY = 5

total_fine = 0
overdue_count = 0
available_count = 0
unavailable_count = 0

print("========== LIBRARY REPORT ==========")
print("Book ID  Days  Overdue  Fine  Status")
print("------------------------------------")

for book in books:

    book_id, days, returned = book

    if returned:
        overdue_days = max(0, days - BORROWING_LIMIT)
        fine = overdue_days * FINE_PER_DAY
        status = "Available"
        available_count += 1

        if overdue_days > 0:
            overdue_count += 1
    else:
        overdue_days = max(0, days - BORROWING_LIMIT)
        fine = 0
        status = "Unavailable"
        unavailable_count += 1

    total_fine += fine

    print(book_id, days, overdue_days,
          fine, status)

print("------------------------------------")
print("Total Overdue Books:", overdue_count)
print("Available Books:", available_count)
print("Unavailable Books:", unavailable_count)
print("Total Fine: Rs.", total_fine)

print("====================================")

