patient_name = input("Enter patient name: ")
patient_age = int(input("Enter patient age: "))
fee = float(input("Enter consultation fee: "))
insurance = input("Do you have health insurance? (yes/no): ")
emergency = input("Is this an emergency? (yes/no): ")


# Determine case type and emergency charge

if emergency == "yes":
    case_type = "Emergency"
    emergency_charge = 500.00
else:
    case_type = "Regular Consultation"
    emergency_charge = 0.00


# Determine patient category

if patient_age < 5:
    category = "Child under 5"
elif patient_age < 18:
    category = "Child/Teen"
elif patient_age < 60:
    category = "Adult"
else:
    category = "Senior"


# Determine consultation fee and insurance discount

if patient_age < 5:
    original_fee = 0.00
    insurance_discount = 0.00

else:
    original_fee = fee

    if insurance == "yes":
        insurance_discount = original_fee * 0.20
    else:
        insurance_discount = 0.00


# Calculate final bill

final_bill = (
    original_fee
    - insurance_discount
    + emergency_charge
)


# Generate patient report

print("\n" + "=" * 45)
print("          HOSPITAL PATIENT REPORT")
print("=" * 45)

print("\nPatient Information")
print("-" * 45)
print(f"Patient Name : {patient_name}")
print(f"Age          : {patient_age}")
print(f"Category     : {category}")

print("\nVisit Information")
print("-" * 45)
print(f"Case         : {case_type}")

print("\nBilling Information")
print("-" * 45)
print(f"Original Fee       : ₹{original_fee:.2f}")
print(f"Insurance Discount : ₹{insurance_discount:.2f}")
print(f"Emergency Charge   : ₹{emergency_charge:.2f}")
print(f"Final Bill         : ₹{final_bill:.2f}")

print("=" * 45)