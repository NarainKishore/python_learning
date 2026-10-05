employees = ["Arun", "Priya", "Karthik", "Divya", "Rahul"]

salaries = [25000, 32000, 45000, 28000, 50000]

attendance = [24, 26, 22, 27, 25]

total_salary = 0
total_employees = 0

highest_salary = salaries[0]
highest_paid_employee = employees[0]

lowest_salary = salaries[0]
lowest_paid_employee = employees[0]


highest_salary_count = 0
medium_salary_count = 0
low_salary_count = 0


total_attendance_days = 0
highest_attendance = attendance[0]
lowest_attendance = attendance[0]


num_records = 0
for emp in employees:
    num_records += 1

print("=============================================")
print("       EMPLOYEE ANALYSIS REPORT")
print("=============================================")

for i in range(num_records):
    current_emp = employees[i]
    current_sal = salaries[i]
    current_att = attendance[i]


    total_salary += current_sal
    total_employees += 1

    if current_sal >= 40000:
        sal_category = "High Salary"
        highest_salary_count += 1
    elif 30000 <= current_sal <= 39999:
        sal_category = "Meduim Salary"
        medium_salary_count += 1
    else:
        sal_category = "Low Salary"
        low_salary_count += 1


    if current_att >= 25:
        att_category = "Excellent Attendance"
    elif 23 <= current_att <= 24:
        att_category = "Good Attendance"
    else:
        att_category = "Poor Attendance"


    if current_sal > highest_salary:
        highest_salary = current_sal
        highest_paid_employee = current_emp

    if current_sal < lowest_salary:
        lowest_salary = current_sal
        lowest_paid_employee = current_emp


    total_attendance_days += current_att


    if current_att > highest_attendance:
        highest_attendance = current_att

    if current_att < lowest_attendance:
        lowest_attendance = current_att


    print(f"Employee:            {current_emp}")
    print(f"Salary:             ₹{current_sal}")
    print(f"Attendance:          {current_att} days")
    print(f"Salary Category:     {sal_category}")
    print(f"Attendance Category: {att_category}")
    print("----------------------------------------")


avg_salary = total_salary / total_employees
avg_attendance = total_attendance_days / total_employees

print("\n==============================================")
print("               SALARY SUMMARY")
print("================================================")
print(f"Total Salary:           ₹{total_salary}")
print(f"Number of Employees:     {total_employees}")
print(f"Average Salary:         ₹{avg_salary}")
print()

print(f"Highest Salary:         ₹{highest_salary}")
print(f"Highest Paid Employee:   {highest_paid_employee}")
print()

print(f"Lowest Salary:          ₹{lowest_salary}")
print(f"Lowest Paid Employee:    {lowest_paid_employee}")
print()

print(f"High Salary Employees:   {highest_salary_count}")
print(f"Medium Salary Employees: {medium_salary_count}")
print(f"Low Salary Employees:    {low_salary_count}")

print("\n==============================================")
print("            ATTENDANCE SUMMARY")
print("================================================")
print(f"Total Attendance :    {total_attendance_days}")
print(f"Average Attendance:   {avg_attendance}")
print(f"Highest Attendance:   {highest_attendance}")
print(f"Lowest Attendance:    {lowest_attendance}")