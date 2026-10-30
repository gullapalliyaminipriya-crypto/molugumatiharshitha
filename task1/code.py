
# Traffic Violation Penalty Calculator

fine_rules = {
    "over speeding": 1000,
    "no helmet": 500,
    "signal jumping": 1000,
    "no driving licence": 5000,
    "drunk driving": 10000
}

vehicles = ["two-wheeler", "four-wheeler", "heavy vehicle"]

total_fine = 0
violation_count = 0
disqualified = False

n = int(input("Enter number of violations: "))

for i in range(n):
    print("\nViolation", i + 1)

    vehicle = input("Enter vehicle category: ").lower()
    offence = input("Enter offence type: ").lower()
    repeat = input("Is it a repeat offence? (yes/no): ").lower()

    if vehicle not in vehicles:
        print("Invalid vehicle category!")
        continue

    if offence not in fine_rules:
        print("Invalid offence type!")
        continue

    violation_count += 1

    fine = fine_rules[offence]

    if repeat == "yes":
        fine = fine + (fine * 0.50)

    total_fine += fine

    print("Penalty for this violation: Rs.", fine)

    if offence == "drunk driving":
        disqualified = True

# Check final disqualification conditions

if violation_count >= 3:
    disqualified = True

print("\n------ FINAL PENALTY REPORT ------")
print("Total valid violations:", violation_count)
print("Total penalty: Rs.", total_fine)

if disqualified:
    print("Disqualification Status: YES")
    print("Warning: Driver meets disqualification conditions.")
else:
    print("Disqualification Status: NO")
    print("Driver does not meet disqualification conditions.")

