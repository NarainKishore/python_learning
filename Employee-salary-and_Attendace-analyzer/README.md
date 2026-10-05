# Employee Salary & Attendance Analyzer

## 1. Project Overview

The **Employee Salary & Attendance Analyzer** is a Python console-based project that analyzes employee salary and monthly attendance information.

The program processes employee records and generates:

* Individual employee analysis
* Salary classifications
* Attendance classifications
* Total and average salary
* Highest and lowest salary
* Highest-paid and lowest-paid employees
* Salary category counts
* Total and average attendance
* Highest and lowest attendance

This project was developed as a **For Loop Master Project** to practice Python fundamentals learned so far.

---

## 2. Project Objective

The main objective of this project is to apply Python `for` loops to a practical real-world problem.

The project focuses on using:

* `for` loops
* `range()`
* List indexing
* Conditional statements
* Accumulators
* Counters
* Largest-value logic
* Smallest-value logic
* Average calculations
* Formatted output

The project intentionally does not use advanced Python concepts such as functions, dictionaries, tuples, sets, nested lists, or `while` loops.

---

## 3. Input Data

The program uses three related lists:

* Employee names
* Employee salaries
* Employee attendance

The same index represents the same employee across all three lists.

Example:

```text
Employee    Salary    Attendance

Arun        ₹25000    24 days
Priya       ₹32000    26 days
Karthik     ₹45000    22 days
Divya       ₹28000    27 days
Rahul       ₹50000    25 days
```

---

## 4. Salary Classification Rules

Employees are classified according to their salary:

| Salary Range     | Category      |
| ---------------- | ------------- |
| ₹40,000 or above | High Salary   |
| ₹30,000–₹39,999  | Medium Salary |
| Below ₹30,000    | Low Salary    |

---

## 5. Attendance Classification Rules

Employees are classified according to their monthly attendance:

| Attendance       | Category             |
| ---------------- | -------------------- |
| 25 days or above | Excellent Attendance |
| 23–24 days       | Good Attendance      |
| Below 23 days    | Poor Attendance      |

---

## 6. Individual Employee Analysis

For every employee, the program displays:

* Employee name
* Salary
* Attendance
* Salary category
* Attendance category

The program processes each employee using a `for` loop and list indexing.

---

## 7. Salary Analysis

The program calculates:

* Total salary
* Number of employees
* Average salary
* Highest salary
* Highest-paid employee
* Lowest salary
* Lowest-paid employee
* Number of high-salary employees
* Number of medium-salary employees
* Number of low-salary employees

The calculations are performed using loops instead of built-in functions.

---

## 8. Attendance Analysis

The program calculates:

* Total attendance days
* Average attendance
* Highest attendance
* Lowest attendance

The program uses accumulator and largest/smallest-value logic to perform these calculations.

---

## 9. Python Concepts Practiced

This project demonstrates the following concepts:

### Basic Concepts

* Variables
* Lists
* List indexing
* Arithmetic operators
* Comparison operators
* f-strings

### Control Flow

* `for` loops
* `range()`
* `if`
* `elif`
* `else`

### Problem-Solving Patterns

* Accumulator pattern
* Counter pattern
* Largest-value pattern
* Smallest-value pattern
* Average calculation
* Tracking related information

---

## 10. Restrictions

The project was intentionally developed using only previously learned concepts.

The following built-in functions were not used for calculations:

```text
sum()
max()
min()
len()
```

The project also does not use:

* Nested lists
* `while` loops
* Functions
* Dictionaries
* Tuples
* Sets
* External libraries

The calculations are implemented manually using loops and variables.

---

## 11. Sample Results

The program produces results similar to:

```text
Total Salary: ₹180000
Number of Employees: 5
Average Salary: ₹36000.0

Highest Salary: ₹50000
Highest Paid Employee: Rahul

Lowest Salary: ₹25000
Lowest Paid Employee: Arun

High Salary Employees: 2
Medium Salary Employees: 1
Low Salary Employees: 2

Total Attendance: 124
Average Attendance: 24.8
Highest Attendance: 27
Lowest Attendance: 22
```

---

## 12. How to Run

Make sure Python is installed on your system.

Navigate to the project directory:

```bash
cd student-performance-management-system
```

Run the Python program:

```bash
python3 employee_salary_attendance.py
```

The program will display the employee analysis and summary reports in the terminal.

---

## 13. Project Structure

```text
employee-salary-attendance-analyzer/
│
├── employee_salary_attendance.py
├── README.md
└── sample_output.txt
```

---

## 14. Learning Outcome

By completing this project, the following `for` loop skills were practiced:

1. Iterating through lists
2. Using `range()` with indexes
3. Connecting related data using indexes
4. Processing multiple records
5. Building accumulators
6. Building counters
7. Finding largest and smallest values
8. Tracking the item associated with a value
9. Calculating averages
10. Combining loops with conditional statements

This project completes the practical `for` loop stage of the Python learning roadmap before moving to the `while` loop.
