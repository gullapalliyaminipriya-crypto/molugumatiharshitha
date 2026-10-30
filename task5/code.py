
# Student Group Formation with Score Balancing

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))
    students.append((name, score))

group_size = int(input("Enter group size: "))

if group_size <= 0 or group_size > n:
    print("Invalid group size!")

else:
    # Sort students by descending scores
    students.sort(key=lambda x: x[1], reverse=True)

    # Calculate number of groups
    groups = [[] for _ in range((n + group_size - 1) // group_size)]
    totals = [0] * len(groups)

    # Allocate students to the group
    # having the lowest total score
    for student in students:
        min_group = totals.index(min(totals))

        groups[min_group].append(student)
        totals[min_group] += student[1]

    # Display results
    print("\n--- STUDENT GROUP DETAILS ---")

    for i in range(len(groups)):
        print("\nGroup", i + 1)

        for name, score in groups[i]:
            print(name, "-", score)

        print("Total Score:", totals[i])

    # Calculate score difference
    difference = max(totals) - min(totals)

    print("\nHighest Group Total:", max(totals))
    print("Lowest Group Total:", min(totals))
    print("Score Difference:", difference)

