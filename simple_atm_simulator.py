def check_balance(balance):
    print("Your balance is: ₹", balance)


def deposit(balance):
    amount = float(input("Enter deposit amount: ₹"))

    if amount > 0:
        balance = balance + amount
        print("Amount deposited successfully.")
    else:
        print("Invalid amount.")

    return balance


def withdraw(balance):
    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Invalid amount.")

    elif amount > balance:
        print("Insufficient balance.")

    else:
        balance = balance - amount
        print("Please collect your cash.")

    return balance


# Login
correct_pin = "1234"
pin = input("Enter your PIN: ")

if pin == correct_pin:

    print("\nLogin successful!")

    balance = 5000

    while True:

        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance(balance)

        elif choice == 2:
            balance = deposit(balance)

        elif choice == 3:
            balance = withdraw(balance)

        elif choice == 4:
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice!")

else:
    print("Incorrect PIN!")
