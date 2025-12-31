expensesList = []   # list of expenses in form of dictionary

print("========== Welcome to Expense Tracker ==========")

while True:
    print("\n==== MENU ====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Kharcha")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice: "))

    # 1. ADD EXPENSE
    if choice == 1:
        date = input("Enter the date of expense: ")
        category = input("Enter the product category: ")
        description = input("Write detail of product: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("Your expense is added successfully.")

    # 2. VIEW ALL EXPENSES
    elif choice == 2:
        if len(expensesList) == 0:
            print("No expenses added yet.")
        else:
            print("\n====== Your Expenses ======")
            count = 1
            for eachKharcha in expensesList:
                print(
                    f"Kharcha Number {count} -> "
                    f"{eachKharcha['date']}, "
                    f"{eachKharcha['category']}, "
                    f"{eachKharcha['description']}, "
                    f"{eachKharcha['amount']}"
                )
                count += 1

    # 3. VIEW TOTAL KHARCHA
    elif choice == 3:
        total = 0
        for eachKharcha in expensesList:
            total += eachKharcha["amount"]

        print("Total Kharcha:", total)

    # 4. EXIT
    elif choice == 4:
        print("Thanks for using our application.")
        break

    # INVALID OPTION
    else:
        print("Invalid choice. Please try again.")
