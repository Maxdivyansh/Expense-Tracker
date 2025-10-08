
expenses = []   # list to store expenses (name, amount)

# Function to add expense
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    expenses.append((name, amount))
    print(" Expense added!")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
    else:
        total = 0
        print("\nExpenses List:")
        for item, amt in expenses:
            print(f"- {item}: ₹{amt}")
            total += amt
        print(f"Total = ₹{total}\n")

# Main program loop
while True:
    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Goodbye! ")
        break
    else:
        print("Invalid choice, try again.")