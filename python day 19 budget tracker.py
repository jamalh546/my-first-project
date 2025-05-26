income = float(input("Enter your monthly income : "))
num_expense = int(input("How many expenses do you want to add: "))

expenses = []
for i in range(num_expense):
    expense = float(input(f"Enter expense {i + 1}: "))
    expenses.append(expense)

    total_expenses = sum(expenses)
    balance = income - total_expenses

print()
print("----------Budget summary-------")
print(f"Your monthly income is: {income}")
print(f"Your total expenses is: {total_expenses} ")
print(f"Remaining balance is: {balance}")

if balance > 0:
    print("You are saving money great job!")
elif balance == 0:
    print("You are breaking even.Watch your spending!")
else:
    print("You are overspending! Try cutting back.")        
