# import sys
# from bank_account import BankAccount

# def main():
#     account = BankAccount(100)  # Example starting balance
    
#     if len(sys.argv) < 2:
#         print("Usage: python main-0.py <command>:<amount>")
#         print("Commands: deposit, withdraw, display")
#         sys.exit(1)

#     command, *params = sys.argv[1].split(':')
#     amount = float(params[0]) if params else None

#     if command == "deposit" and amount is not None:
#         account.deposit(amount)
#         print(f"Deposited: ${amount}")
#     elif command == "withdraw" and amount is not None:
#         if account.withdraw(amount):
#             print(f"Withdrew: ${amount}")
#         else:
#             print("Insufficient funds.")
#     elif command == "display":
#         account.display_balance()
#     else:
#         print("Invalid command.")

# if __name__ == "__main__":
#     main()

# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
