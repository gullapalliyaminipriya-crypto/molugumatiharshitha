
# Campus Event Seating and Entry Validation

registrations = []
entry_records = []
seating = []

rows = int(input("Enter number of seating rows: "))
seats_per_row = int(input("Enter seats per row: "))

# Generate seating using a nested list
for r in range(rows):
    row = []
    for s in range(seats_per_row):
        row.append("")
    seating.append(row)

capacity = rows * seats_per_row

while True:
    print("\n===== CAMPUS EVENT SYSTEM =====")
    print("1. Register Participant")
    print("2. Assign Seat")
    print("3. Validate Ticket Entry")
    print("4. View Seating")
    print("5. View Summary Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        reg_id = input("Enter registration ID: ")
        name = input("Enter participant name: ")

        if any(reg[0] == reg_id for reg in registrations):
            print("Registration ID already exists.")
        else:
            registrations.append((reg_id, name))
            print("Participant registered successfully.")

    elif choice == "2":
        reg_id = input("Enter registration ID: ")

        if not any(reg[0] == reg_id for reg in registrations):
            print("Invalid registration ID.")
            continue

        if any(reg[0] == reg_id for reg in
               [(sid, seat) for row in seating
                for seat in row for sid in [seat]]):
            pass

        assigned = False

        for r in range(rows):
            for s in range(seats_per_row):
                if seating[r][s] == reg_id:
                    print("Seat already assigned.")
                    assigned = True
                    break
            if assigned:
                break

        if not assigned:
            for r in range(rows):
                for s in range(seats_per_row):
                    if seating[r][s] == "":
                        seating[r][s] = reg_id
                        print("Seat assigned: Row", r + 1,
                              "Seat", s + 1)
                        assigned = True
                        break
                if assigned:
                    break

        if not assigned:
            print("No seats available.")

    elif choice == "3":
        reg_id = input("Enter ticket registration ID: ")

        if not any(reg[0] == reg_id for reg in registrations):
            print("Entry rejected: Invalid ticket.")
        elif reg_id in entry_records:
            print("Entry rejected: Duplicate entry detected.")
        else:
            entry_records.append(reg_id)
            print("Ticket valid. Entry permitted.")

    elif choice == "4":
        print("\n===== SEATING ARRANGEMENT =====")

        for r, row in enumerate(seating):
            print("Row", r + 1, ":", end=" ")
            for s, reg_id in enumerate(row):
                if reg_id == "":
                    print("[Available]", end=" ")
                else:
                    print("[" + reg_id + "]", end=" ")
            print()

    elif choice == "5":
        occupied = sum(
            1 for row in seating for seat in row if seat != ""
        )
        available = capacity - occupied

        print("\n===== EVENT SUMMARY =====")
        print("Total Registrations:", len(registrations))
        print("Total Seating Capacity:", capacity)
        print("Occupied Seats:", occupied)
        print("Available Seats:", available)
        print("Successful Entries:", len(entry_records))

        print("\nRegistered Participants:")
        for reg_id, name in registrations:
            print(reg_id, "-", name)

    elif choice == "6":
        print("Exiting Campus Event System.")
        break

    else:
        print("Invalid choice. Try again.")
