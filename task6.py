
students = []
attendance = []
marks = []
events = []
resources = []

while True:
    print("\n===== SMART CAMPUS MANAGEMENT =====")
    print("1. Add Student Record")
    print("2. Record Attendance")
    print("3. Enter Student Marks")
    print("4. Event Registration")
    print("5. Resource Allocation")
    print("6. Summary Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        branch = input("Enter Branch: ")

        students.append((sid, name, branch))
        print("Student record added successfully.")

    elif choice == "2":
        sid = input("Enter Student ID: ")

        if any(s[0] == sid for s in students):
            status = input("Enter attendance (Present/Absent): ")
            attendance.append((sid, status))
            print("Attendance recorded.")
        else:
            print("Student not found.")

    elif choice == "3":
        sid = input("Enter Student ID: ")

        if any(s[0] == sid for s in students):
            subject = input("Enter Subject: ")
            score = float(input("Enter Marks (0-100): "))

            if 0 <= score <= 100:
                marks.append((sid, subject, score))
                print("Marks recorded successfully.")
            else:
                print("Invalid marks.")
        else:
            print("Student not found.")

    elif choice == "4":
        sid = input("Enter Student ID: ")

        if any(s[0] == sid for s in students):
            event = input("Enter Event Name: ")
            events.append((sid, event))
            print("Event registration successful.")
        else:
            print("Student not found.")

    elif choice == "5":
        resource = input("Enter Resource Name: ")
        sid = input("Enter Student ID: ")

        if any(s[0] == sid for s in students):
            resources.append((resource, sid))
            print("Resource allocated successfully.")
        else:
            print("Student not found.")

    elif choice == "6":
        print("\n===== CAMPUS SUMMARY REPORT =====")

        print("\nStudent Records:")
        for sid, name, branch in students:
            print("ID:", sid, "| Name:", name,
                  "| Branch:", branch)

        print("\nAttendance Records:")
        for sid, status in attendance:
            print("ID:", sid, "| Status:", status)

        print("\nMarks Records:")
        for sid, subject, score in marks:
            print("ID:", sid, "| Subject:", subject,
                  "| Marks:", score)

        print("\nEvent Registrations:")
        for sid, event in events:
            print("ID:", sid, "| Event:", event)

        print("\nResource Allocations:")
        for resource, sid in resources:
            print("Resource:", resource, "| Student ID:", sid)

        print("\nTotal Students:", len(students))
        print("Total Attendance Entries:", len(attendance))
        print("Total Marks Entries:", len(marks))
        print("Total Event Registrations:", len(events))
        print("Total Resource Allocations:", len(resources))

        if marks:
            average = sum(m[2] for m in marks) / len(marks)
            print("Overall Average Marks:", round(average, 2))

    elif choice == "7":
        print("Exiting Smart Campus Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
