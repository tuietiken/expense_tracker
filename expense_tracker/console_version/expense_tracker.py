from datetime import date, datetime

def add_expense():
    print("\n---Category---")
    print("1. Food")
    print("2. Coffee")
    print("3. Other")
    
    operations = {
        "1": "Food",
        "2": "Coffee",
        "3": "Other"
    }

    while True:  
        choice = input("Choose: ")  
        if choice in operations:
            category = operations[choice]
            break
        else:
            print("\nInvalid choise")
            continue

    while True:
        try:
            amount = float(input("Amount: "))
            break
        except ValueError:
            print("Enter a number")


    with open("expenses.txt", "a") as file:
        file.write(f"{date.today()} | {category} | {amount}\n")

    print("Expense added")


def show_expenses():
    try:
        with open("expenses.txt", "r") as file:
            print("\n--- Expenses ---")
            print(file.read())
    except FileNotFoundError:
        print("No expenses yet")


def total_sum():
    total = 0
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                amount = float(line.strip().split(" | ")[2])
                total += amount
        print("Total:", total)
    except FileNotFoundError:
        print("No expenses yet")

def show_expenses_by_category():
    print("\n---Category---")
    print("1. Food")
    print("2. Coffee")
    print("3. Other")
    
    operations = {
        "1": "Food",
        "2": "Coffee",
        "3": "Other"
    }

    while True:  
        choice = input("Choose: ")  
        if choice in operations:
            category = operations[choice]
            break
        else:
            print("\nInvalid choise")
            continue

    total = 0
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                if category == line.strip().split(" | ")[1]:
                    print(line.strip())
                    amount = float(line.strip().split(" | ")[2])
                    total += amount
        print("---Total:", total, "---")
    except FileNotFoundError:
        print("No expenses yet")

def show_total():
    total = 0
    try:
        with open("expenses.txt", "r") as file:
            print("\n--- Expenses ---")
            for line in file:
                print(line.strip())
                amount = float(line.strip().split(" | ")[2])
                total += amount
        print("---Total:", total, "---")
    except FileNotFoundError:
        print("No expenses yet")

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Total sum")
    print("4. Show expenses by category")
    print("5. Show total by all categories")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        total_sum()
    elif choice == "4":
        show_expenses_by_category()
    elif choice == "5":
        show_total()
    elif choice == "0":
        print("Goodbye")
        break
    else:
        print("Invalid choice")
