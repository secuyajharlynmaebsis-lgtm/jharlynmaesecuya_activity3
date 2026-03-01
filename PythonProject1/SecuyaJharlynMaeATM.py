secuya_balance = 500.00 # starting balance

while True:
    print()
    print("============================================")
    print("||     Welcome to a Simple ATM System!    ||")
    print("============================================\n")
    print("1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    try:
        print(" ")
        secuya_options = int(input("Choose an option (1-4): "))

        # Balance Inquiry
        if secuya_options == 1:
            print(" ")
            print(f"Your current balance is Php{secuya_balance:.2f} \n")

        # Deposit Money
        elif secuya_options == 2:
            print(" ")
            secuya_amount = float(input("Enter amount to deposit: "))
            if secuya_amount <= 0:
                print("Your deposit amount must be greater than 0. \n")
                continue
            secuya_balance += secuya_amount
            print (" ")
            print(f"Deposit successful. Your new balance is Php{secuya_balance:.2f} \n")

        # Withdraw Money
        elif secuya_options ==3:
            print(" ")
            print(f"Your current balance is Php{secuya_balance:.2f}")
            print(" ")
            secuya_amount = float(input("Enter amount to withdraw: "))
            # Check non-negative values
            if secuya_amount <= 0:
                print(" ")
                print("Your withdrawal amount must be greater than 0. \n")
                continue
            # Check if withdrawal amount is not greater than balance
            elif secuya_amount > secuya_balance:
                print(" ")
                print("Your withdrawal amount cannot be greater than your balance. \n")
                continue
            # Computation
            else:
                secuya_balance -= secuya_amount
                print(" ")
                print(f"Remaining balance is: Php{secuya_balance:.2f} \n ")

        # Terminate program
        elif secuya_options == 4:
            print(" ")
            print("Thank you for using the program. Goodbye!")
            break

        # Verify options
        else:
            print(" ")
            print("Invalid option. Please choose 1 to 4. \n")
            continue

    # Validate inputs for error handling
    except ValueError:
        print(" ")
        print("Invalid input. Please enter a number. \n")
