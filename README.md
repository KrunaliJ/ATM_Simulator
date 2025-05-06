# ATM_Simulator using python if ststement ,elif ,else, short if,short if..else,and ,or ,not,nested if pass

Lines 1–2
# Initial balance
balance = 1000
A variable balance is initialized with ₹1000. This simulates the user's bank balance.

Lines 4–7
print("Welcome to Python Bank ATM!")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")
These lines print a menu for the user to choose what they want to do in the ATM simulator.

Line 9
choice = int(input("Enter your choice (1-4): "))
Takes the user's input (1 to 4) and stores it as an integer in choice.

Lines 11–29: if, elif, else
if choice == 1:
    print(f"Your current balance is ₹{balance}")
If the user enters 1, we show their current balance using an if statement.

elif choice == 2:
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{balance}")
    else:
        print("Invalid deposit amount.")
If the user selects 2, they are asked to enter a deposit amount.
We use a nested if to ensure the amount is positive.
If valid, it’s added to the balance; otherwise, an error is shown.

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
If the user chooses to withdraw (option 3), they enter an amount.
We use nested if again to check two things:
Amount must be positive.
Amount must not exceed balance.
If both are valid, withdraw the money; otherwise, show an error.

elif choice == 4:
    print("Thank you for using the ATM.")
If the user enters 4, we exit the system politely.

else:
    print("Invalid choice.")
If the input doesn't match 1–4, we show an error. This is the else part.

Line 31: Shorthand if...else
min_balance = 100
print("Maintain minimum balance!" if balance < min_balance else "Balance is sufficient.")
This is a shorthand if...else expression.
If balance is below ₹100, it prints a warning; otherwise, it says your balance is fine.

Lines 34–38: and, or, not
atm_card = True
pin_entered = True

if atm_card and pin_entered:
    print("Access granted!")
else:
    print("Access denied!")
Here we use logical and to simulate ATM access:
Both card and PIN must be present.
If either is missing, access is denied using else.

Line 41: not operator
if not atm_card:
    print("Please insert your ATM card.")
Demonstrates the not operator.
if atm_card is False, this reminds the user to insert the card.

Line 44–46: pass statement
if balance > 5000:
    # This is a placeholder for future tax deduction logic
    pass
This if block uses the pass statement.
pass means "do nothing (for now)". It's often used when the logic will be added later.


