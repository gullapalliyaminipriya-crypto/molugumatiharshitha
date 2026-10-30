
# Tuple-Based Course Registration Validation

registrations = []

# Available courses
available_courses = (
    "Python", "Java", "C", "DBMS",
    "AI", "Web"
)

# Invalid course combinations
invalid_combinations = [
    ("Python", "Java"),
    ("C", "Java")
]

n = int(input("Enter number of students: "))

# Collect student registrations
for i in range(n):
    print("\nStudent", i + 1)

    student_id = input("Enter student ID: ")

    courses = input(
        "Enter courses separated by spaces: "
    ).split()

    # Store registration as tuple
    registration = (student_id, tuple(courses))

    registrations.append(registration)

# Validation process
violated_students = []

print("\n===== COURSE REGISTRATION REPORT =====")

for student_id, courses in registrations:

    duplicate_courses = []
    invalid_courses = []
    invalid_pairs = []

    # Find duplicate courses
    for course in courses:
        if courses.count(course) > 1:
            if course not in duplicate_courses:
                duplicate_courses.append(course)

    # Find unavailable courses
    for course in courses:
        if course not in available_courses:
            if course not in invalid_courses:
                invalid_courses.append(course)

    # Check invalid combinations
    for pair in invalid_combinations:
        if pair[0] in courses and pair[1] in courses:
            invalid_pairs.append(pair)

    # Display student details
    print("\nStudent ID:", student_id)
    print("Registered Courses:", courses)

    violation = False

    if duplicate_courses:
        print("Duplicate Courses:", duplicate_courses)
        violation = True

    if invalid_courses:
        print("Invalid Courses:", invalid_courses)
        violation = True

    if invalid_pairs:
        print("Invalid Combinations:", invalid_pairs)
        violation = True

    if violation:
        print("Status: Registration Invalid")
        violated_students.append(student_id)
    else:
        print("Status: Registration Valid")

# Final report
print("\n===== FINAL SUMMARY =====")

print("Total Students:", len(registrations))
print("Students with Violations:", len(violated_students))

if violated_students:
    print("Violation Student IDs:", violated_students)
else:
    print("No Registration Violations Found")

print("\n===== VALIDATION COMPLETED =====")

