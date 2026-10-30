
# Campus Transport Allocation

routes = int(input("Enter number of routes: "))

total_required = 0
total_allocated = 0
total_unserved = 0

demands = []
capacities = []

for i in range(routes):
    print("\nRoute", i + 1)

    passengers = int(input("Enter passenger demand: "))
    capacity = int(input("Enter bus capacity: "))

    if passengers < 0 or capacity <= 0:
        print("Invalid input")
        exit()

    demands.append(passengers)
    capacities.append(capacity)

available_buses = int(input("\nEnter total available buses: "))

if available_buses < 0:
    print("Invalid number of buses")
    exit()

print("\n----- TRANSPORT ALLOCATION -----")

remaining_buses = available_buses

for i in range(routes):

    passengers = demands[i]
    capacity = capacities[i]

    required = (passengers + capacity - 1) // capacity

    allocated = min(required, remaining_buses)

    served = min(passengers, allocated * capacity)

    unserved = passengers - served

    remaining_buses -= allocated

    total_required += required
    total_allocated += allocated
    total_unserved += unserved

    print("\nRoute:", i + 1)
    print("Passenger Demand:", passengers)
    print("Bus Capacity:", capacity)
    print("Buses Required:", required)
    print("Buses Allocated:", allocated)
    print("Passengers Served:", served)
    print("Unserved Passengers:", unserved)

print("\n----- FINAL SUMMARY -----")
print("Total Buses Required:", total_required)
print("Total Buses Allocated:", total_allocated)
print("Remaining Buses:", remaining_buses)
print("Total Unserved Passengers:", total_unserved)

