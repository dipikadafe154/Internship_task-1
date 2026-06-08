import pandas as pd
import matplotlib.pyplot as plt

# Read data
data = pd.read_csv("expense_data.csv")

print("\nPersonal Expense Analytics")
print("-" * 30)

# Total Expense
total_expense = data["Amount"].sum()
print("Total Expense:", total_expense)

# Average Expense
average_expense = data["Amount"].mean()
print("Average Expense:", round(average_expense, 2))

# Category-wise expenses
expense_by_category = data.groupby("Category")["Amount"].sum()

print("\nCategory-wise Expenses:")
print(expense_by_category)

# Highest spending category
highest_category = expense_by_category.idxmax()
highest_amount = expense_by_category.max()

print("\nHighest Spending Category:")
print(f"{highest_category} : {highest_amount}")

# Bar Chart
plt.figure(figsize=(8,5))
expense_by_category.plot(kind="bar")
plt.title("Expense by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pie Chart
plt.figure(figsize=(6,6))
plt.pie(
    expense_by_category,
    labels=expense_by_category.index,
    autopct="%1.1f%%"
)
plt.title("Expense Distribution by Category")
plt.show()