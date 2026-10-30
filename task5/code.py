
from datetime import datetime
from math import ceil

# Input vehicle details
vehicle = input("Enter Vehicle Number: ")
print("1. Two-Wheeler")
print("2. Car")
print("3. Bus")

choice = int(input("Select Vehicle Category: "))

# Vehicle rates and daily limits
if choice == 1:
    category = "Two-Wheeler"
    rate = 10
    daily_limit = 100
elif choice == 2:
    category = "Car"
    rate = 20
    daily_limit = 200
elif choice == 3:
    category = "Bus"
    rate = 40
    daily_limit = 400
else:
    print("Invalid Vehicle Category!")
    exit()

# Input entry and exit times
entry = input("Enter Entry Time (HH:MM): ")
exit_time = input("Enter Exit Time (HH:MM): ")

try:
    t1 = datetime.strptime(entry, "%H:%M")
    t2 = datetime.strptime(exit_time, "%H:%M")

    start = t1.hour * 60 + t1.minute
    end = t2.hour * 60 + t2.minute

    # Calculate overnight duration
    duration = end - start
    if duration <= 0:
        duration += 1440

    hours = ceil(duration / 60)

    # Calculate parking charges
    days = duration // 1440
    remaining_hours = ceil((duration % 1440) / 60)

    charge = days * daily_limit
    charge += min(remaining_hours * rate, daily_limit)

    # Calculate penalty
    penalty = 0
    if duration > 720:
        penalty = 50

    total = charge + penalty

    # Display parking receipt
    print("\n===== PARKING RECEIPT =====")
    print("Vehicle Number:", vehicle)
    print("Vehicle Category:", category)
    print("Entry Time:", entry)
    print("Exit Time:", exit_time)
    print("Parking Duration:", hours, "hours")
    print("Parking Charge: Rs.", charge)
    print("Penalty: Rs.", penalty)
    print("Total Fee: Rs.", total)
    print("===========================")

except ValueError:
    print("Invalid Time Format! Enter time in HH:MM format.")

