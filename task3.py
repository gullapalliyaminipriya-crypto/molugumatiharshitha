weight = float(input())
length = float(input())
width = float(input())
height = float(input())
zone = int(input())
urgency = input().strip().lower()
restriction = input().strip().lower()

volume = length * width * height
chargeable_weight = max(weight, volume / 5000)

zone_rates = {1: 20, 2: 40, 3: 60, 4: 80}
eligible = []

if zone not in zone_rates or min(weight, length, width, height) <= 0:
    print("Invalid parcel details")
else:
    base = chargeable_weight * 10 + zone_rates[zone]

    services = {
        "standard": (1.0, 5, 30),
        "express": (1.5, 10, 20),
        "premium": (2.0, 20, 15)
    }

    for service, (multiplier, extra, max_days) in services.items():
        if restriction == "restricted" and service != "premium":
            continue

        if chargeable_weight > 30:
            continue

        if urgency == "urgent" and service == "standard":
            continue

        if urgency not in ("normal", "urgent"):
            continue

        cost = base * multiplier + extra
        eligible.append((cost, service, max_days))

    if eligible:
        eligible.sort()
        for cost, service, days in eligible:
            print(f"{service.title()}: Rs. {cost:.2f}, {days} days")

        print(f"Best option: {eligible[0][1].title()}")
        print(f"Minimum charge: Rs. {eligible[0][0]:.2f}")
    else:
        print("No eligible courier service")