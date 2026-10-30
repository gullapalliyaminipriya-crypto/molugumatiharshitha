
# Multi-Criteria Library Resource Distribution

book_name = input("Enter book name: ")
total_copies = int(input("Enter total available copies: "))

n = int(input("Enter number of library branches: "))

branches = []

for i in range(n):
    print("\nEnter details for Branch", i + 1)

    name = input("Enter branch name: ")
    demand = int(input("Enter book demand: "))
    priority = int(input("Enter priority (1-3): "))

    branches.append((name, demand, priority))

# Sort branches by priority
# Priority 1 is highest priority
branches.sort(key=lambda x: x[2])

available = total_copies
total_allocated = 0
total_unmet = 0

print("\n========== LIBRARY DISTRIBUTION REPORT ==========")
print("Book Name:", book_name)
print("Total Available Copies:", total_copies)

print("\nBranch\t\tDemand\tPriority\tAllocated\tUnmet")

for name, demand, priority in branches:

    allocated = min(demand, available)
    unmet = demand - allocated

    available -= allocated
    total_allocated += allocated
    total_unmet += unmet

    print(name, "\t", demand, "\t", priority,
          "\t\t", allocated, "\t\t", unmet)

print("\nTotal Allocated Copies:", total_allocated)
print("Total Unmet Demand:", total_unmet)
print("Remaining Copies:", available)

print("\nDistribution Completed.")

