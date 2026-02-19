# AIM: Write a Python program to calculate the gross salary of an employee.
# Coder:
# Date:
bs = float(input("Enter Basic Salary: "))
da = 0.70 * bs
ta = 0.30 * bs
hra = 0.10 * bs
gross_salary = bs + da + ta + hra
print("\nSalary Details:")
print("Basic Salary:\t", bs)
print("DA (70%):\t", da)
print("TA (30%):\t", ta)
print("HRA (10%):\t", hra)
print("Gross Salary:\t", gross_salary)


# Write your code here
