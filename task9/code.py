
branches = int(input("Enter number of branches: "))
months = int(input("Enter number of months: "))

categories = ["Rent", "Salary", "Electricity"]
expenses = []

for i in range(branches):
    print("\nBranch", i + 1)
    name = input("Enter branch name: ")
    branch_data = []

    for j in range(months):
        month_data = []
        print("Month", j + 1)

        for category in categories:
            amount = float(input(category + " expense: "))
            month_data.append(amount)

        branch_data.append(month_data)

    expenses.append([name, branch_data])

# Calculate branch and category totals
category_totals = [0, 0, 0]
branch_totals = []

for name, data in expenses:
    total = 0

    for month in data:
        total += sum(month)

        for j in range(3):
            category_totals[j] += month[j]

    branch_totals.append(total)
    print("\n", name, "Total:", total)
    print("Average:", total / months)

print("\nCategory-wise Expenses:")
for i in range(3):
    print(categories[i], ":", category_totals[i])

print("\nHighest Expense Branch:",
      expenses[branch_totals.index(max(branch_totals))][0])

print("Highest Expense Category:",
      categories[category_totals.index(max(category_totals))])

print("Overall Expense:", sum(branch_totals))

