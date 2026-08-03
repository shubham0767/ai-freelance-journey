print("=" * 40)
print("ATM System")
print("=" * 40)

balance=10000
while True:
    print("\n1. Check Balance")
    print("\n2. Deposit")
    print("\n3. Withdraw")
    print("\n4. Exit")

    try:
        choice=int(input("enter your choice:"))

        if choice==1:
            print("current balance :",balance)

        elif choice ==2:
            amount=float(input("Enter Deposit Amount:"))
            balance+=amount
            print("deposit Successful.")
            print("Updated Balance:",balance)

        elif choice == 3:
            amount = float(input("Enter Withdraw Amount: "))

            if amount <= balance:
                balance -= amount
                print("Withdrawal Successful.")
                print("Updated Balance:", balance)
            else:
                print("Insufficient Balance.")

        elif choice == 4:
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid Choice.")

    except ValueError:
        print("Please enter valid numbers.") 