def atm_withdrawal():
    balance = 1000  # Initial balance

    print("Welcome to the ATM!")
    print(f"Your current balance is: ${balance}")

    # Ask the user to enter the withdrawal amount
    withdrawal_amount = float(input("Enter the amount you want to withdraw: "))

    # Check if the withdrawal amount is less than or equal to the current balance
    if withdrawal_amount <= balance:
        balance -= withdrawal_amount
        print(f"Transaction successful! You have withdrawn ${withdrawal_amount}.")
        print(f"Your new balance is: ${balance}")
    else:
        print("Insufficient funds! The withdrawal amount exceeds your current balance.")

# Run the ATM simulation
atm_withdrawal()
