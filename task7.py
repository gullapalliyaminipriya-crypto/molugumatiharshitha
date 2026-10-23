
# Smart Public Transport Fare Reconciliation

routes = []
total_expected = 0
total_collected = 0

while True:
    print("\n===== TRANSPORT FARE SYSTEM =====")
    print("1. Add Route Transaction")
    print("2. View Route Details")
    print("3. Revenue Reconciliation Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        route = input("Enter route name: ")
        category = input("Passenger category (Adult/Child/Senior): ").lower()
        passengers = int(input("Enter number of passengers: "))
        collected = float(input("Enter collected revenue: "))

        if category == "adult":
            fare = 50
        elif category == "child":
            fare = 25
        elif category == "senior":
            fare = 30
        else:
            print("Invalid passenger category.")
            continue

        if passengers <= 0 or collected < 0:
            print("Invalid passenger count or revenue.")
            continue

        expected = passengers * fare
        difference = collected - expected

        routes.append(
            (route, category, passengers, expected,
             collected, difference)
        )

        total_expected += expected
        total_collected += collected

        print("Expected Revenue: ₹", expected)
        print("Collected Revenue: ₹", collected)

        if difference == 0:
            print("Status: Reconciled")
        elif difference < 0:
            print("Status: Revenue Shortage")
        else:
            print("Status: Excess Collection")

    elif choice == "2":
        print("\n===== ROUTE DETAILS =====")

        if not routes:
            print("No transactions available.")
        else:
            for route, category, count, expected, collected, diff in routes:
                print("\nRoute:", route)
                print("Category:", category.title())
                print("Passengers:", count)
                print("Expected Revenue: ₹", expected)
                print("Collected Revenue: ₹", collected)
                print("Difference: ₹", diff)

    elif choice == "3":
        print("\n===== RECONCILIATION REPORT =====")
        print("Total Expected Revenue: ₹", total_expected)
        print("Total Collected Revenue: ₹", total_collected)

        difference = total_collected - total_expected
        print("Overall Difference: ₹", difference)

        if difference == 0:
            print("Status: Revenue fully reconciled.")
        elif difference < 0:
            print("Status: Overall revenue shortage.")
        else:
            print("Status: Overall excess collection.")

        print("\nDiscrepancy Transactions:")
        found = False

        for route, category, count, expected, collected, diff in routes:
            if diff != 0:
                print(route, "-", category.title(),
                      "- Difference: ₹", diff)
                found = True

        if not found:
            print("No discrepancies found.")

    elif choice == "4":
        print("Exiting Fare Reconciliation System.")
        break

    else:
        print("Invalid choice. Try again.")
