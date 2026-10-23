capacity = int(input())
stops = int(input())

passengers = 0

for i in range(1, stops + 1):
    boarding = int(input())
    alighting = int(input())

    if boarding < 0 or alighting < 0:
        print("Invalid passenger count")
        continue

    if alighting > passengers:
        print("Invalid alighting count")
        continue

    passengers = passengers - alighting + boarding

    print(f"Stop {i}: {passengers} passengers")

    if passengers > capacity:
        print("Capacity Violation")
    else:
        print("Within Capacity")

print(f"Final Passenger Count: {passengers}")