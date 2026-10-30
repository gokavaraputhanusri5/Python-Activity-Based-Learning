

import math

# Input event details
event = input("Enter Event Name: ")

venue = float(input("Enter Venue Cost: "))
equipment = float(input("Enter Equipment Cost: "))
catering = float(input("Enter Catering Cost: "))
transport = float(input("Enter Transport Cost: "))
certificates = float(input("Enter Certificate Cost: "))

participants = int(input("Enter Number of Participants: "))
contribution = float(input("Enter Contribution per Participant: "))
sponsorship = float(input("Enter Sponsorship Amount: "))

# Calculate total expenditure
total_cost = venue + equipment + catering + transport + certificates

# Calculate participant contributions
total_contribution = participants * contribution

# Calculate total available funds
total_funds = total_contribution + sponsorship

# Calculate balance and shortfall
balance = total_funds - total_cost
shortfall = max(0, total_cost - total_funds)

# Calculate minimum registrations
needed = max(0, total_cost - sponsorship)

if contribution > 0:
    minimum = math.ceil(needed / contribution)
else:
    minimum = 0 if needed == 0 else -1

# Display financial report
print("\n===== CAMPUS EVENT FINANCIAL REPORT =====")
print("Event Name:", event)
print("-----------------------------------------")
print("Venue Cost       : Rs.", venue)
print("Equipment Cost   : Rs.", equipment)
print("Catering Cost    : Rs.", catering)
print("Transport Cost   : Rs.", transport)
print("Certificate Cost : Rs.", certificates)
print("-----------------------------------------")
print("Total Cost       : Rs.", total_cost)
print("Participant Fund : Rs.", total_contribution)
print("Sponsorship      : Rs.", sponsorship)
print("Total Funds      : Rs.", total_funds)
print("Financial Balance: Rs.", balance)
print("Sponsorship Shortfall: Rs.", shortfall)

if minimum == -1:
    print("Break-even registrations: Not possible")
else:
    print("Minimum Registrations:", minimum)

if balance >= 0:
    print("Event Status: Budget Covered")
else:
    print("Event Status: Additional Funds Required")

print("=========================================")

