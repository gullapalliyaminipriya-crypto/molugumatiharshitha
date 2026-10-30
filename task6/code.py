
# Tuple-Based Course Registration Validation

registrations = []

n = int(input("Enter number of students: "))

# Read student registrations
for i in range(n):
    print("\nStudent", i + 1)

    student_id = input("Enter Student ID: ")
    courses = tuple(input("Enter courses separated by spaces: ").upper().split())

    registrations.append((student_id, courses))

# Predefined invalid course combinations
invalid_combinations = [
    ("PYTHON", "JAVA"),
    ("AI", "ML")
]

print("\n----- REGISTRATION VALIDATION -----")

for student_id, courses in registrations:

    errors = []

    # Check duplicate courses
    if len(courses) != len(set(courses)):
        errors.append("Duplicate course registration")

    # Check invalid course combinations
    selected = set(courses)

    for pair in invalid_combinations:
        if pair[0] in selected and pair[1] in selected:
            errors.append(
                pair[0] + " and " + pair[1] +
                " cannot be selected together"
            )

    # Display result
    print("\nStudent ID:", student_id)
    print("Courses:", courses)

    if errors:
        print("Status: INVALID")
        for error in errors:
            print("Reason:", error)
    else:
        print("Status: VALID")

print("\nValidation Completed.")

