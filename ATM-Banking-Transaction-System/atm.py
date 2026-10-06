account_holder = "Pradeep"
balance = 45000
PIN = 11223344
deposit_count = 0
withdrawal_count = 0
total_deposited = 0
total_withdrawn = 0

attempts = 0

while attempts < 3:

    user_pin = int(input("Enter your PIN: "))

    if PIN == user_pin:
        status = "Login Successful"
        break

    else:
        attempts += 1

        if attempts == 3:
            status = "Account Locked"

print(status)

if status == "Login Successful":

    while True:
        print("======= ATM =======")
        print()

        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History Summary")
        print("5. Exit")
        print()

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(f"Balance : ₹{balance}")

        elif choice == 2:
            amount = int(input("Enter the Deposit amount: ₹"))

            if amount > 0:
                deposit_count += 1
                total_deposited += amount
                balance += amount
            else:
                print(f"Invalid amount: ₹{amount}")

        elif choice == 3:
            amount = int(input("Enter the Withdrawal amount: ₹"))

            if amount <= 0:
                print("Invalid Amount")

            elif amount > balance:
                print("Insufficient Balance")

            else:
                print("Successful withdrawal")

                withdrawal_count += 1
                total_withdrawn += amount
                balance -= amount

        elif choice == 4:
            print("====== TRANSACTION SUMMARY ======")
            print()

            print(f"Total Deposited: ₹{total_deposited}")
            print(f"Deposit Count: {deposit_count}")
            print(f"Total Withdrawn: ₹{total_withdrawn}")
            print(f"Withdrawal Count: {withdrawal_count}")
            print(f"Current Balance: ₹{balance}")

        elif choice == 5:
            print("Thank you for using ABC Bank ATM")
            break

        else:
            print("Invalid Choice")