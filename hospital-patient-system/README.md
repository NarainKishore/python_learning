# Hospital Patient Registration & Billing System

A beginner-level Python console application that simulates a simple hospital patient registration and billing system.

## Project Description

This project collects basic patient information and uses conditional statements to determine the patient's category, consultation type, insurance discount, emergency charges, and final bill.

The project was created as a practical project for learning and strengthening Python conditional statements.

## Features

* Collects patient information
* Categorizes patients based on age
* Handles emergency and regular consultations
* Applies health insurance discounts
* Adds emergency charges when applicable
* Calculates the final consultation bill
* Generates a formatted patient report

## Python Concepts Used

* Variables
* Data types
* `input()`
* Type conversion using `int()` and `float()`
* Arithmetic operators
* Comparison operators
* `if`
* `elif`
* `else`
* Nested `if`
* Ternary operator
* f-strings
* Basic output formatting

## How to Run

Make sure Python is installed on your system.

Open the terminal inside the project directory and run:

```bash
python hospital_patient_system.py
```

The program will ask for:

```text
Enter patient name:
Enter patient age:
Enter consultation fee:
Do you have health insurance? (yes/no):
Is this an emergency? (yes/no):
```

After entering the information, the program generates a hospital patient report.

## Billing Rules

### Patient Category

| Age          | Category      |
| ------------ | ------------- |
| Below 5      | Child under 5 |
| 5–17         | Child/Teen    |
| 18–59        | Adult         |
| 60 and above | Senior        |

### Insurance

Patients with health insurance receive a **20% discount** on the consultation fee.

### Emergency

Emergency cases receive an additional **₹500 emergency charge**.

### Children Under 5

Patients below 5 years receive a **free consultation**.

## Example

```text
=============================================
          HOSPITAL PATIENT REPORT
=============================================

Patient Information
---------------------------------------------
Patient Name : Arun
Age          : 65
Category     : Senior

Visit Information
---------------------------------------------
Case         : Emergency

Billing Information
---------------------------------------------
Original Fee       : ₹1000.00
Insurance Discount : ₹200.00
Emergency Charge   : ₹500.00
Final Bill         : ₹1300.00
=============================================
```

## Project Structure

```text
hospital-patient-system/

├── hospital_patient_system.py
├── README.md
└── sample_output.txt
```

### Files

* `hospital_patient_system.py` — Main Python program
* `README.md` — Project documentation
* `sample_output.txt` — Sample outputs from different test cases

## Learning Purpose

This project is part of my practical Python learning journey.

The main goal of this project is to strengthen my understanding of conditional statements, nested decision-making, comparison operators, arithmetic operations, and formatted output before moving on to loops.
