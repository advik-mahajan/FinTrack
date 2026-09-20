from user import User
from storage_manager import add_user, load_users, add_transaction, add_asset, add_liability, get_next_user_id, update_user_pin, load_assets, load_liabilities, load_transactions
from finance_manager import FinanceManager
from transaction import Transaction
from asset import Asset
from liability import Liability

def dashboard(finance_manager):
    while True:
        print()
        print("=====FinTrack Dashboard=====")
        print("1. Account Details")
        print("2. Log Transactions")
        print("3. Register Assets")
        print("4. Register Liabilities")
        print("5. Change PIN")
        print("6. View Transaction History")
        print("7. View Assets")
        print("8. View Liabilities")
        print("9. Exit")

        while True:
            try:
                user_choice = int(input("Enter the Number Corresponding to Your Choice: "))
                if 1 <= user_choice <= 9:
                    break
                else:
                    print("Enter a number between 1 and 9.")
                    continue
            except ValueError:
                print("Invalid Input! Please Try Again.")

        match user_choice:

            case 1:
                finance_manager.current_user.display_account_details()

            case 2:
                print()
                print("===TRANSACTION TYPE===")
                print("1. Expense")
                print("2. Income")
                while True:
                    try:
                        transaction_choice = int(input("Enter the Number Corresponding to Your Transaction Type: "))
                        if 1 <= transaction_choice <= 2:
                            break
                        else:
                            print("Enter either 1 or 2.")
                            continue
                    except ValueError:
                        print("Invalid Input! Please Try Again.")

                if transaction_choice == 1:
                    transaction_type_selected = "Expense"
                    print()
                    print("===EXPENSE CATEGORIES===")
                    print("1. Food & Dining")
                    print("2. Transportation")
                    print("3. Shopping")
                    print("4. Bills & Utilities")
                    print("5. Entertainment")
                    print("6. Health & Medical")
                    print("7. Education")
                    print("8. Travel")
                    print("9. Personal")
                    print("10. Miscellaneous")

                    expense_categories = {1:"Food & Dining",
                                          2:"Transportation",
                                          3:"Shopping",
                                          4:"Bills & Utilities",
                                          5:"Entertainment",
                                          6:"Health & Medical",
                                          7:"Education",
                                          8:"Travel",
                                          9:"Personal",
                                          10:"Miscellaneous"}

                    while True:
                        try:
                            choice_of_expense = int(input("Enter the Number Corresponding to Your Expense Category: "))
                            if 1 <= choice_of_expense <= 10:
                                break
                            else:
                                print("Enter a number between 1 and 10.")
                                continue
                        except ValueError:
                            print("Invalid Input! Please Try Again.")

                    category = expense_categories[choice_of_expense] 

                elif transaction_choice == 2:
                    transaction_type_selected = "Income"
                    print()
                    print("===INCOME CATEGORIES===")
                    print("1. Salary")
                    print("2. Freelance")
                    print("3. Business")
                    print("4. Bonuses / Gifts / Refunds")
                    print("5. Other")

                    income_categories = {1:"Salary",
                                         2:"Freelance",
                                         3:"Business",
                                         4:"Bonuses / Gifts / Refunds",
                                         5:"Other"}

                    while True:
                        try:
                            choice_of_income = int(input("Enter the Number Corresponding to Your Income Category: "))
                            if 1 <= choice_of_income <= 5:
                                break
                            else:
                                print("Enter a number between 1 and 5.")
                                continue
                        except ValueError:
                            print("Invalid Input! Please Try Again.")

                    category = income_categories[choice_of_income]


                while True:
                    try:
                        transaction_amount = float(input("Enter the Transaction Amount: "))
                        if transaction_amount > 0:
                            break
                        else:
                            print("Enter an Amount Greater than Zero.")
                            continue
                    except ValueError:
                        print("Invalid Input! Please Try Again.")

                description = input("Enter a Description: ")
                user_id = finance_manager.current_user.user_id

                transaction = Transaction(user_id, transaction_type_selected, category, transaction_amount, description)
                finance_manager.add_transaction(transaction)
                add_transaction(transaction)

            case 3:
                print()
                print("===ASSET CATEGORIES===")
                print("1. Stocks")
                print("2. Mutual Funds")
                print("3. ETFs")
                print("4. Real Estate")
                print("5. Gold / Other Metals")
                print("6. Bonds")
                print("7. Cryptocurrencies")
                print("8. Bank Deposits")

                asset_categories = {1:"Stocks",
                                    2:"Mutual Funds",
                                    3:"ETFs",
                                    4:"Real Estate",
                                    5:"Gold / Other Metals",
                                    6:"Bonds",
                                    7:"Cryptocurrencies",
                                    8:"Bank Deposits"}

                while True:
                    try:
                        choice_of_asset = int(input("Enter the Number Corresponding to Your Asset Category: "))
                        if 1 <= choice_of_asset <= 8:
                            break
                        else:
                            print("Enter a number between 1 and 8.")
                            continue
                    except ValueError:
                        print("Invalid Input! Please Try Again.")

                asset_category = asset_categories[choice_of_asset]
                user_id = finance_manager.current_user.user_id
                name = input("Enter the Name of the Asset: ").strip()

                while True:
                    try:
                        asset_value = float(input("Enter the Current Value of the Asset: "))
                        if asset_value > 0:
                            break
                        else:
                            print("Enter a Value Greater than Zero.")
                            continue
                    except ValueError:
                        print("Invalid Input! Please Try Again.")

                asset = Asset(user_id, asset_category, name, asset_value)
                finance_manager.add_assets(asset)
                add_asset(asset)

            case 4:
                print()
                print("===LIABILITY CATEGORIES===")
                print("1. Car Loan")
                print("2. Home Loan")
                print("3. Educational Loan")
                print("4. Personal Loan")
                print("5. Business Loan")
                print("6. Credit Card Debt")
                print("7. Others")

                liability_categories = {1:"Car Loan",
                                        2:"Home Loan",
                                        3:"Educational Loan",
                                        4:"Personal Loan",
                                        5:"Business Loan",
                                        6:"Credit Card Debt",
                                        7:"Others"}

                while True:
                    try:
                        liability_choice = int(input("Enter the Number Corresponding to Your Liability Category: "))
                        if 1 <= liability_choice <= 7:
                            break
                        else:
                            print("Enter a number between 1 and 7.")
                            continue
                    except ValueError:
                        print("Invalid Input! Please Try Again.")

                liability_category = liability_categories[liability_choice]
                user_id = finance_manager.current_user.user_id

                name = input("Enter the Name of the Liability: ").strip()

                while True:
                    try:
                        principal = float(input("Enter the Principal Amount: "))
                        if principal > 0:
                            break
                        else:
                            print("Enter a Value Greater than Zero.")
                            continue
                    except ValueError:
                        print("Invalid Input! Please Try Again.")

                while True:
                    try:
                        outstanding_amount = float(input("Enter your Outstanding Amount: "))
                        if outstanding_amount < 0:
                            print("Value Cannot be Negative. Please Try Again")
                            continue
                        else:
                            break
                    except ValueError:
                        print("Invalid Input! Please Try Again.")

                liability = Liability(user_id, liability_category, name, principal, outstanding_amount)
                finance_manager.add_liability(liability)
                add_liability(liability)

            case 5:
                finance_manager.current_user.change_pin()
                update_user_pin(finance_manager.current_user.user_id, finance_manager.current_user.pin)

            case 6:
                print()
                print("=====TRANSACTION HISTORY=====")
                transactions = load_transactions()
                for transaction in transactions:
                    print(f"Transaction ID: {transaction[1]}")
                    print(f"Type: {transaction[2]}")
                    print(f"Category: {transaction[3]}")
                    print(f"Amount: ₹{transaction[4]}")
                    print(f"Description: {transaction[5]}")
                    print(f"Date: {transaction[6]}")
                    print()

            case 7:
                print()
                print("=====REGISTERED ASSETS=====")
                assets = load_assets()
                for asset in assets:
                    print(f"Asset ID: {asset[1]}")
                    print(f"Asset Type: {asset[2]}")
                    print(f"Asset Name: {asset[3]}")
                    print(f"Value: ₹{asset[4]}")
                    print()

            case 8:
                print()
                print("=====REGISTERED LIABILITIES=====")
                liabilities = load_liabilities()
                for liability in liabilities:
                    print(f"Liability ID: {liability[1]}")
                    print(f"Liability Type: {liability[2]}")
                    print(f"Liability Name: {liability[3]}")
                    print(f"Principal Amount: ₹{liability[4]}")
                    print(f"Outstanding Amount: ₹{liability[5]}")

            case 9:
                break

while True:
    print("=====FinTrack=====")
    print("1. New User")
    print("2. Existing User")
    print("3. Exit")
    try:
        choice = int(input("Enter the number corresponding to your choice: "))
        print()
        if 1 <= choice <= 3:
            match choice:
                    case 1:
                        while True:
                            first_name = input("Enter your First Name: ").strip()
                            if len(first_name) > 0:
                                break
                            else:
                                print("Invalid Input! Enter a first name greater than 0 characters.")
                                continue
                        while True:
                            last_name = input("Enter your Last Name: ").strip()
                            if len(last_name) > 0:
                                break
                            else:
                                print("Invalid Input! Enter a last name greater than 0 characters.")
                                continue
                        while True:
                            username = input("Enter your Username: ").strip()
                            if len(username) > 0:
                                break
                            else:
                                print("Invalid Input! Enter a username greater than 0 characters.")
                                continue
                        while True:
                            try:
                                pin = int(input("Enter a 6-digit PIN: "))
                                if 100000 <= pin <= 999999:
                                    break
                                else:
                                    print("The PIN you entered is not 6-digits. Please enter a 6-digit PIN.")
                                    continue
                            except ValueError:
                                print("Invalid Input! Please Try Again.")

                        user_id = get_next_user_id()        
                        user = User(first_name, last_name, username, pin)
                        user.user_id = user_id
                        add_user(user)
                        finance_manager = FinanceManager(user)
                        dashboard(finance_manager)

                    case 2:
                        username = input("Enter your Username: ").strip()
                        while True:
                            try:
                                pin = int(input("Enter your PIN: "))
                                if 100000 <= pin <= 999999:
                                    break
                                else:
                                    print("The PIN you entered is not 6-digits. Please try again!")
                                    continue
                            except ValueError:
                                print("Invalid Input! Please Try Again.")
                        users = load_users()
                        pin = str(pin)
                        found = False

                        for row in users:
                            if row[3] == username and row[4] == pin:
                                user = User(row[1], row[2], row[3], int(row[4]))
                                finance_manager = FinanceManager(user)
                                found = True
                                dashboard(finance_manager)
                                break
                        if not found:
                            print("Invalid Username or PIN! Please Try Again.")

                    case 3:
                        print("Thank You for Using FinTrack!")
                        break
        else:
            print("Enter a number between 1 and 3")
            continue
    except ValueError:
        print("Invalid Input! Please Try Again.")
