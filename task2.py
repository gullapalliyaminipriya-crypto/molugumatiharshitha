
n = int(input())
fixed_fee = float(input())
limit = float(input())
penalty_rate = float(input())

households = []

for i in range(n):
    name = input()
    consumption = float(input())

    # Progressive consumption charges
    if consumption <= 10:
        charge = consumption * 5
    elif consumption <= 20:
        charge = 10 * 5 + (consumption - 10) * 8
    elif consumption <= 30:
        charge = 10 * 5 + 10 * 8 + (consumption - 20) * 12
    else:
        charge = 10 * 5 + 10 * 8 + 10 * 12
        charge += (consumption - 30) * 15

    # Excess usage penalty
    penalty = 0
    if consumption > limit:
        penalty = (consumption - limit) * penalty_rate

    bill = charge + fixed_fee + penalty

    households.append((name, consumption, bill))

# Display household bills
for name, consumption, bill in households:
    print(f"{name}: Consumption={consumption:.2f}, Bill={bill:.2f}")

# Identify highest consumption
if households:
    highest = max(households, key=lambda x: x[1])
    print(f"Highest Consumption: {highest[0]}")

    # Average consumption
    average = sum(h[1] for h in households) / len(households)
    print(f"Average Consumption: {average:.2f}")

    # Identify excessive usage
    print("Excessive Usage Households:")
    found = False

    for name, consumption, bill in households:
        if consumption > limit:
            print(name)
            found = True

    if not found:
        print("None")
