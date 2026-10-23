
# Campus Registration Identifier Analyzer

branch_names = {
    "CS": "Computer Science",
    "EC": "Electronics",
    "ME": "Mechanical",
    "EE": "Electrical"
}

registrations = []

n = int(input("Enter number of student IDs: "))

for i in range(n):
    reg_id = input("Enter registration ID: ").strip().upper()
    registrations.append(reg_id)

print("\n===== REGISTRATION ANALYSIS =====")

for reg_id in registrations:
    print("\nRegistration ID:", reg_id)

    # Validate length
    if len(reg_id) != 8:
        print("Status: Invalid length")
        continue

    year = reg_id[0:2]
    branch = reg_id[2:4]
    number = reg_id[4:8]

    # Validate year
    if not year.isdigit():
        print("Status: Invalid admission year")
        continue

    # Validate branch
    if branch not in branch_names:
        print("Status: Invalid branch code")
        continue

    # Validate student number
    if not number.isdigit() or number == "0000":
        print("Status: Invalid student number")
        continue

    print("Status: Valid Registration ID")
    print("Admission Year: 20" + year)
    print("Branch Code:", branch)
    print("Branch Name:", branch_names[branch])
    print("Student Number:", number)

print("\n===== BRANCH-WISE CLASSIFICATION =====")

for code, name in branch_names.items():
    students = [
        reg_id for reg_id in registrations
        if len(reg_id) == 8
        and reg_id[:2].isdigit()
        and reg_id[2:4] == code
        and reg_id[4:].isdigit()
        and reg_id[4:] != "0000"
    ]

    print(name, ":", len(students), "records")

print("\n===== YEAR-WISE CLASSIFICATION =====")

years = {}

for reg_id in registrations:
    if (len(reg_id) == 8
        and reg_id[:2].isdigit()
        and reg_id[2:4] in branch_names
        and reg_id[4:].isdigit()
        and reg_id[4:] != "0000"):

        year = "20" + reg_id[:2]
        years[year] = years.get(year, 0) + 1

for year, count in sorted(years.items()):
    print(year, ":", count, "students")
