
energy_rate = 8       # Cost per electricity unit
water_rate = 2        # Cost per water unit

energy_limit = 100    # Maximum average daily energy usage
water_limit = 500     # Maximum average daily water usage

buildings = []

n = int(input("Enter number of buildings: "))
days = int(input("Enter number of days: "))

for i in range(n):
    name = input("\nEnter building name: ")
    energy = []
    water = []

    for j in range(days):
        print("Day", j + 1)
        e = float(input("Enter electricity consumption (kWh): "))
        w = float(input("Enter water consumption (litres): "))
        energy.append(e)
        water.append(w)

    total_e = sum(energy)
    total_w = sum(water)

    avg_e = total_e / days
    avg_w = total_w / days

    energy_cost = total_e * energy_rate
    water_cost = total_w * water_rate
    total_cost = energy_cost + water_cost

    if energy[0] != 0:
        e_change = ((energy[-1] - energy[0]) /
                    energy[0]) * 100
    else:
        e_change = 0

    if water[0] != 0:
        w_change = ((water[-1] - water[0]) /
                    water[0]) * 100
    else:
        w_change = 0

    score = total_e * 0.6 + total_w * 0.4

    buildings.append({
        "name": name,
        "total_e": total_e,
        "total_w": total_w,
        "avg_e": avg_e,
        "avg_w": avg_w,
        "energy_cost": energy_cost,
        "water_cost": water_cost,
        "total_cost": total_cost,
        "e_change": e_change,
        "w_change": w_change,
        "score": score
    })

# Display audit report
print("\n========== CAMPUS AUDIT REPORT ==========")

for b in buildings:
    print("\nBuilding:", b["name"])
    print("Total Electricity:", b["total_e"], "kWh")
    print("Total Water:", b["total_w"], "litres")
    print("Average Electricity:", round(b["avg_e"], 2))
    print("Average Water:", round(b["avg_w"], 2))
    print("Electricity Cost: Rs.", b["energy_cost"])
    print("Water Cost: Rs.", b["water_cost"])
    print("Total Cost: Rs.", b["total_cost"])
    print("Electricity Change:", round(b["e_change"], 2), "%")
    print("Water Change:", round(b["w_change"], 2), "%")

    if b["avg_e"] > energy_limit:
        print("Excessive Electricity Consumption")
    if b["avg_w"] > water_limit:
        print("Excessive Water Consumption")
    if b["avg_e"] <= energy_limit and b["avg_w"] <= water_limit:
        print("Consumption is within limits")

# Rank buildings by score
buildings.sort(key=lambda x: x["score"], reverse=True)

print("\n========== BUILDING RANKING ==========")
for rank, b in enumerate(buildings, start=1):
    print(rank, b["name"], "- Score:", round(b["score"], 2))

print("\nAudit Completed Successfully!")

