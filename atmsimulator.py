
# Initial balance
balance = 1000

print("Welcome to Python Bank ATM!")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

# Get user's choice
choice = int(input("Enter your choice (1-4): "))

# Using if, elif, else
if choice == 1:
    print(f"Your current balance is ₹{balance}")

elif choice == 2:
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{balance}")
    else:
        print("Invalid deposit amount.")

elif choice == 3:
    amount = float(input("Enter amount to withdraw: "))
    
    # nested if and logical operators
    if amount > 0:
        if amount <= balance:
            balance -= amount
            print(f"Withdrawn ₹{amount}. New balance: ₹{balance}")
        else:
            print("Insufficient balance.")
    else:
        print("Invalid withdrawal amount.")

elif choice == 4:
    print("Thank you for using the ATM.")

else:
    print("Invalid choice.")

# Shorthand if
min_balance = 100
print("Maintain minimum balance!" if balance < min_balance else "Balance is sufficient.")

# Shorthand if...else example with OR, AND, NOT
atm_card = True
pin_entered = True

# compound condition using and, or, not
if atm_card and pin_entered:
    print("Access granted!")
else:
    print("Access denied!")

# Using 'not'
if not atm_card:
    print("Please insert your ATM card.")

# Example use of 'pass' (can be in future logic)
if balance > 5000:
    # This is a placeholder for future tax deduction logic
    pass
