# List from previous tasks
employee_salaries = [60100, 90000, 44500, 71000, 14950, 10000, 83920, 57000, 18900, 120500]
updated_salaries = []

# Use for loop to iterate over list
for selari in employee_salaries:
    updated_salaries.append(selari * 1.1)

# Testing
print("Updated employee salaries:", updated_salaries)
print("Old sum of expenses:", sum(employee_salaries))
print("New sum of expenses:", sum(updated_salaries))