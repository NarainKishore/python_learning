name = input("Name: ")
email = input("Email: ")
phone = input("Phone: ")

name = name.strip()
name_valid = len(name) > 0

email = email.lower()

email_valid = (
    email.count("@") == 1 
    and "." in email and 
    " " not in email
    and email.find(".") > email.find("@")
)

phone_valid  = phone.isdigit() and len(phone) == 10
print(f"\nEmail after cleanup: {email}")
print(f"Name valid: {name_valid}")
print(f"Email valid: {email_valid}")
print(f"Phone valid: {phone_valid}")


if name_valid and email_valid and phone_valid:
    print("ACCEPTED")
else:
    print("NEEDS REVIEW")
