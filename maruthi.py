print("===== EMPLOYEE TESTING PROJECT =====")

name = input("Enter your name: ")
employee_id = input("Enter employee ID: ")
salary = int(input("Enter salary: "))

print("\n===== TEST RESULTS =====")

if name == "":
    print("Invalid employee name")
else:
    print("Employee name is valid")

if employee_id == "":
    print("Invalid employee ID")
else:
    print("Employee ID is valid")

if salary <= 0:
    print("Invalid salary")
else:
    print("Salary is valid")
