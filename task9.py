
# Nested List Examination Seating Validation

rows = int(input("Enter number of rows: "))
cols = int(input("Enter seats per row: "))

seating = []

print("Enter roll numbers for each seat.")
print("Use 0 for an empty seat and -1 for a reserved seat.")

for i in range(rows):
    row = []
    for j in range(cols):
        roll = int(input(f"Row {i+1}, Seat {j+1}: "))
        row.append(roll)
    seating.append(row)

n = int(input("Enter number of registered students: "))
registered = []

for i in range(n):
    roll = int(input("Enter registered roll number: "))
    registered.append(roll)

reserved = []
r = int(input("Enter number of reserved positions: "))

for i in range(r):
    row = int(input("Reserved row number: "))
    col = int(input("Reserved seat number: "))
    reserved.append((row - 1, col - 1))

seen = []
duplicates = []
empty = []
invalid = []
wrong_reserved = []

for i in range(rows):
    for j in range(cols):
        roll = seating[i][j]

        if (i, j) in reserved:
            if roll != -1:
                wrong_reserved.append((i + 1, j + 1))
            continue

        if roll == -1:
            wrong_reserved.append((i + 1, j + 1))

        elif roll == 0:
            empty.append((i + 1, j + 1))

        else:
            if roll in seen:
                duplicates.append(roll)
            else:
                seen.append(roll)

            if roll not in registered:
                invalid.append(roll)

print("\n===== EXAM SEATING VALIDATION REPORT =====")
print("\nSeating Matrix:")

for row in seating:
    print(row)

print("\nDuplicate Roll Numbers:", sorted(set(duplicates)))
print("Empty Seats:", empty)
print("Invalid Student Allocations:", sorted(set(invalid)))
print("Reserved Seat Errors:", wrong_reserved)

if not duplicates and not invalid and not wrong_reserved:
    print("\nSeating validation completed successfully.")
else:
    print("\nSeating validation found errors.")

print("Total Seating Capacity:", rows * cols)
print("Total Empty Seats:", len(empty))
print("Total Reserved Positions:", len(reserved))
