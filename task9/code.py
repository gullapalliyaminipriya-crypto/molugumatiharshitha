
# Smart Electricity Billing for Multiple Apartments

n = int(input("Enter number of apartments: "))

apartments = []

for i in range(n):
    print("\nApartment", i + 1)

    apt_no = input("Enter apartment number: ")
    previous = int(input("Enter previous meter reading: "))
    current = int(input("Enter current meter reading: "))
    recorded_bill = float(input("Enter recorded bill amount: "))

    # Validate meter readings
    if current < previous:
        print("Invalid meter readings!")
        continue

    units = current - previous

    # Progressive tariff calculation
    if units <= 100:
        energy_charge = units * 2

    elif units <= 200:
        energy_charge = (100 * 2) + (units - 100) * 3

    else:
        energy_charge = (100 * 2) + (100 * 3) + (units - 200) * 5

    # Fixed charge
    fixed_charge = 50

    subtotal = energy_charge + fixed_charge

    # Rebate calculation
    rebate = 0

    if units < 100:
        rebate = subtotal * 0.10

    final_bill = subtotal - rebate

    # Discrepancy checking
    difference = abs(final_bill - recorded_bill)

    if difference > 0.01:
        status = "Discrepancy Found"
    else:
        status = "Bill Verified"

    apartments.append({
        "number": apt_no,
        "units": units,
        "energy": energy_charge,
        "fixed": fixed_charge,
        "rebate": rebate,
        "bill": final_bill,
        "recorded": recorded_bill,
        "status": status
    })

# Display apartment bills
print("\n------ ELECTRICITY BILL DETAILS ------")

for apt in apartments:
    print("\nApartment:", apt["number"])
    print("Units Consumed:", apt["units"])
    print("Energy Charge: Rs.", round(apt["energy"], 2))
    print("Fixed Charge: Rs.", apt["fixed"])
    print("Rebate: Rs.", round(apt["rebate"], 2))
    print("Final Bill: Rs.", round(apt["bill"], 2))
    print("Recorded Bill: Rs.", round(apt["recorded"], 2))
    print("Status:", apt["status"])

# Rank apartments by consumption
ranked = sorted(
    apartments,
    key=lambda x: x["units"],
    reverse=True
)

print("\n------ CONSUMPTION RANKING ------")

for rank, apt in enumerate(ranked, start=1):
    print(rank, ".", apt["number"],
          "-", apt["units"], "units")

# Display discrepancies
print("\n------ BILLING DISCREPANCIES ------")

found = False

for apt in apartments:
    if apt["status"] == "Discrepancy Found":
        print("Apartment:", apt["number"],
              "| Difference: Rs.",
              round(abs(apt["bill"] - apt["recorded"]), 2))
        found = True

if not found:
    print("No billing discrepancies found.")

print("\nTotal Apartments Processed:", len(apartments))

