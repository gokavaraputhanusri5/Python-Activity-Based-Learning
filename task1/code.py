
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")

basic = float(input("Enter Basic Salary: "))
allowances = float(input("Enter Allowances: "))
hours = float(input("Enter Overtime Hours: "))
rate = float(input("Enter Overtime Rate per Hour: "))
incentives = float(input("Enter Incentives: "))

# Calculate overtime pay
overtime = hours * rate

# Calculate gross salary
gross = basic + allowances + overtime + incentives

# Calculate progressive deductions
if gross <= 20000:
    deduction = gross * 0.05

elif gross <= 40000:
    deduction = (20000 * 0.05) + ((gross - 20000) * 0.10)

else:
    deduction = (20000 * 0.05) + (20000 * 0.10) + ((gross - 40000) * 0.15)

# Calculate net salary
net = gross - deduction

# Display salary statement
print("\n========== SALARY STATEMENT ==========")
print("Employee Name :", name)
print("Employee ID   :", emp_id)
print("--------------------------------------")
print("Basic Salary  : Rs.", basic)
print("Allowances    : Rs.", allowances)
print("Overtime Pay  : Rs.", overtime)
print("Incentives    : Rs.", incentives)
print("--------------------------------------")
print("Gross Salary  : Rs.", gross)
print("Deductions    : Rs.", deduction)
print("--------------------------------------")
print("Net Salary    : Rs.", net)
print("======================================")

