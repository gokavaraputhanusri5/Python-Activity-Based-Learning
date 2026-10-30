

## 1. Problem Statement

Develop a Python program to calculate an employee's gross salary based on basic pay, allowances, overtime pay, and incentives. Apply progressive deductions based on the gross salary and calculate the net salary. Finally, generate a properly formatted salary statement displaying the employee details, salary components, total gross salary, deductions, and net salary.

## 2. Algorithm

1. Start the program.
2. Read employee name and employee ID.
3. Input basic salary.
4. Input allowances, overtime hours, overtime rate, and incentives.
5. Calculate overtime pay.

&#x20;  Overtime Pay = Overtime Hours × Overtime Rate

6\. Calculate gross salary.

&#x20;  Gross Salary = Basic Salary + Allowances + Overtime Pay + Incentives

7. Calculate progressive deductions:
   - 5% deduction on the first ₹20,000.
   - 10% deduction on the next ₹20,000.
   - 15% deduction on the remaining amount above ₹40,000.
8. Calculate net salary.

&#x20;  Net Salary = Gross Salary − Total Deductions

9. Display the formatted salary statement.
10. Stop the program.



``` 4. Flowchart (Mermaid Code)

flowchart TD
    A([Start]) --> B[/Input Employee Details/]
    B --> C[/Input Basic Salary, Allowances/]
    C --> D[/Input Overtime Hours, Rate and Incentives/]
    D --> E[Calculate Overtime Pay]
    E --> F[Calculate Gross Salary]
    F --> G{Gross Salary <= 20000?}
    G -- Yes --> H[Deduction = Gross x 5%]
    G -- No --> I{Gross Salary <= 40000?}
    I -- Yes --> J[Deduction = 5% of 20000 + 10% of Remaining]
    I -- No --> K[Deduction = 5% of 20000 + 10% of 20000 + 15% of Remaining]
    H --> L[Calculate Net Salary]
    J --> L
    K --> L
    L --> M[/Display Salary Statement/]
    M --> N([Stop])
```


## 5. Sample Input

```
Enter Employee Name: Ravi
Enter Employee ID: 101
Enter Basic Salary: 30000
Enter Allowances: 5000
Enter Overtime Hours: 10
Enter Overtime Rate per Hour: 200
Enter Incentives: 3000
```

## 6. Sample Output

```
========== SALARY STATEMENT ==========
Employee Name : Ravi
Employee ID   : 101
--------------------------------------
Basic Salary  : Rs. 30000.0
Allowances    : Rs. 5000.0
Overtime Pay  : Rs. 2000.0
Incentives    : Rs. 3000.0
--------------------------------------
Gross Salary  : Rs. 40000.0
Deductions    : Rs. 3000.0
--------------------------------------
Net Salary    : Rs. 37000.0
======================================
```

## 7. Result

Thus, the Python program successfully calculates the employee's gross salary, applies progressive deductions, and generates a formatted salary statement displaying the total earnings, deductions, and final net salary.
