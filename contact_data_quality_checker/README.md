# Contact Data Quality Checker

## Project Overview

The **Contact Data Quality Checker** is a Python command-line application that validates basic contact information before it is stored in a spreadsheet, database, or customer management system.

The program accepts a contact name, email address, and phone number. It cleans selected fields, checks their basic validity, and displays a validation report.

## Features

- Removes leading and trailing whitespace from names.
- Converts email addresses to lowercase.
- Checks whether the name is empty.
- Performs basic email-format validation.
- Checks whether the email contains exactly one `@` symbol.
- Checks that the email contains a period after the `@` symbol.
- Rejects email addresses containing spaces.
- Verifies that the phone number contains exactly 10 digits.
- Displays individual validation results.
- Displays an overall status: `ACCEPTED` or `NEEDS REVIEW`.

## Python Concepts Used

This project applies the following Python concepts:

- Variables and data types
- User input using `input()`
- Strings and f-strings
- String methods: `strip()`, `lower()`, `count()`, and `find()`
- String checks: `isdigit()` and `len()`
- Membership operators: `in` and `not in`
- Conditional statements: `if` and `else`
- Logical operators: `and`
- Boolean variables and validation logic

## Project Structure

```text
contact_data_quality_checker/
├── contact_data_quality_checker.py
├── README.md
└── sample_output.txt
```

## How to Run the Project

### Prerequisites

- Python 3 installed on your system
- A terminal or command-line interface

### Execution Steps

1. Open Terminal.
2. Navigate to the project directory:

   ```bash
   cd ~/python_learning/contact_data_quality_checker
   ```

3. Run the Python program:

   ```bash
   python3 contact_data_quality_checker.py
   ```

4. Enter the requested name, email address, and phone number.

5. Review the validation results displayed in the terminal.

## Example

### Input

```text
Name: Aravind M
Email: aravind@example.com
Phone: 8923843458
```

### Output

```text
Email after cleanup: aravind@example.com
Name valid: True
Email valid: True
Phone valid: True
ACCEPTED
```

## Validation Rules

| Field | Validation rule |
|---|---|
| Name | Must not be empty after removing leading and trailing spaces |
| Email | Must contain exactly one `@`, a period after `@`, and no spaces |
| Phone | Must contain exactly 10 numeric digits |
| Final status | `ACCEPTED` when all three fields pass; otherwise `NEEDS REVIEW` |

## Limitations

- Email validation is basic and does not guarantee that an email address exists or satisfies every email-address standard.
- Phone validation assumes a 10-digit number and does not support country codes, spaces, hyphens, or extensions.
- The program validates data locally and does not store contact information in a database.
- The program does not verify whether a phone number is active or belongs to the person entering it.

## Learning Outcome

This project demonstrates how Python strings, built-in string methods, conditions, and logical operators can be combined to build a practical data-validation tool.

It also introduces a basic data-quality workflow that can be extended for spreadsheets, database entry forms, and customer management applications.

## Future Improvements

- Add more robust email-format validation.
- Support phone numbers with country codes.
- Allow repeated entries without restarting the program.
- Save validated contacts to a CSV file.
- Add automated tests for valid and invalid inputs.