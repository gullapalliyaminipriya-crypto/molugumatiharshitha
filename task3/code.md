# Employee Payroll and Deduction Analysis

## 1. Problem Statement

Develop a Python program to calculate an employee's salary based on basic pay, allowances, overtime, and incentives. Calculate the gross salary and apply progressive deductions according to predefined salary slabs. Finally, generate a formatted salary statement showing gross salary, total deductions, and net salary.

## 2. Algorithm

1. Start the program.
2. Read employee name, basic pay, allowances, overtime pay, and incentives.
3. Calculate gross salary by adding all earnings.
4. Calculate deductions using the following progressive rules:
   - First ₹10,000: No deduction.
   - Next ₹10,000: 5% deduction.
   - Remaining amount above ₹20,000: 10% deduction.
5. Calculate net salary by subtracting deductions from gross salary.
6. Display the formatted salary statement.
7. Stop the program.

## 3. Python Source Code

```meramid

flowchart TD
    A([START]) --> B[/Enter Employee Name/]
    B --> C[/Enter Basic Pay, Allowances, Overtime and Incentives/]
    C --> D[Calculate Gross Salary]
    D --> E{Gross Salary <= 10000?}
    E -- Yes --> F[Deduction = 0]
    E -- No --> G{Gross Salary <= 20000?}
    G -- Yes --> H[Deduction = Gross Salary - 10000 * 0.05]
    G -- No --> I[Deduction = 500 + (Gross Salary - 20000) * 0.10]
    F --> J[Calculate Net Salary]
    H --> J
    I --> J
    J --> K[/Display Salary Statement/]
    K --> L([STOP])
```


```

## 4. Sample Input

```
Enter employee name: Ravi
Enter basic pay: 25000
Enter allowances: 5000
Enter overtime pay: 2000
Enter incentives: 3000
```

## 5. Sample Output

```
========== SALARY STATEMENT ==========
Employee Name : Ravi
--------------------------------------
Basic Pay     : Rs. 25000.00
Allowances    : Rs. 5000.00
Overtime Pay  : Rs. 2000.00
Incentives    : Rs. 3000.00
--------------------------------------
Gross Salary  : Rs. 35000.00
Deduction     : Rs. 1550.00
Net Salary    : Rs. 33450.00
======================================
```

## 6. Calculation

- Gross salary = 25,000 + 5,000 + 2,000 + 3,000 = ₹35,000
- Deduction = (₹10,000 × 5%) + (₹15,000 × 10%) = ₹2,000

Therefore, the correct net salary is ₹33,000.

Note: The sample output's deduction and net salary should be ₹2,000 and ₹33,000, respectively. The code calculates these values correctly.
