import random

# ATM Simulator Program

# Initial balance
balance = 10000
pin = ""

# Function to display balance
def display_balance():
    print(f"Your balance is: ₱{balance}")

# Function to withdraw money
def withdraw():
    global balance, transaction_history
    amount = float(input("Enter the amount to withdraw: ₱"))
    if amount > balance:
        print("Insufficient funds. Withdrawal failed.")
    else:
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: ₱{balance}")
        transaction_history.append(f"Withdrew ₱{amount}")

# Function to transfer money
def transfer():
    global balance, transaction_history
    amount = float(input("Enter the amount to transfer: ₱"))
    if amount > balance:
        print("Insufficient funds. Transfer failed.")
    else:
        recipient = input("Enter the recipient's account number: ")
        print(f"₱{amount} transferred to {recipient}.")
        balance -= amount
        print(f"Remaining balance: ₱{balance}")
        transaction_history.append(f"Transferred ₱{amount} to {recipient}")

# Function to deposit money
def deposit():
    global balance, transaction_history
    amount = float(input("Enter the amount to deposit: ₱"))
    balance += amount
    print(f"Deposit successful. Updated balance: ₱{balance}")
    transaction_history.append(f"Deposited ₱{amount}")

# Function to change PIN
def change_pin():
    global pin
    new_pin = input("Enter your new 4-digit PIN: ")
    if len(new_pin) == 4 and new_pin.isdigit():
        pin = new_pin
        print("PIN successfully changed.")
    else:
        print("Invalid PIN. Please enter a 4-digit number.")

# Main program
while True:
    user_input = input("Enter your PIN: ")
    pin = str(random.randint(1000, 9999))  # Generate a random 4-digit PIN

    print("\n===== ATM Simulator =====")
    print("1. Display Balance")
    print("2. Withdraw Money")
    print("3. Transfer Money")
    print("4. Deposit Money")
    print("5. Change PIN")
    print("6. View Transaction History")
    print("7. Quit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        display_balance()
    elif choice == '2':
        withdraw()
    elif choice == '3':
        transfer()
    elif choice == '4':
        deposit()
    elif choice == '5':
        change_pin()
    elif choice == '6':
        print("\n===== Transaction History =====")
        for transaction in transaction_history:
            print(transaction)
    elif choice == '7':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
