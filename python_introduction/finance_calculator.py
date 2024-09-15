# finance_calculator.py

# User input for financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with interest (simplified formula)
annual_interest_rate = 0.05  # 5% annual interest (simple)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

# Print the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
