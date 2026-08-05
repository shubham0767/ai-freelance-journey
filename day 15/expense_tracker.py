expenses = {}

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        name = input("Expense Name: ")
        amount = float(input("Amount: "))
        expenses[name] = amount

    elif choice == "2":
        if len(expenses) == 0:
            print("No Expenses.")
        else:
            for name, amount in expenses.items():
                print(name, ":", amount)

    elif choice == "3":
        print("Total Expenses =", sum(expenses.values()))

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")
        