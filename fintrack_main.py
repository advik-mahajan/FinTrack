import datetime 

class User:
    user_id_counter = 0
    def __init__(self, firstname, lastname, username, pin):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.pin = pin
        User.user_id_counter += 1
        self.user_id = User.user_id_counter

    def display_details(self):
        print("=====ACCOUNT DETAILS=====")
        print(f"Name: {self.firstname} {self.lastname}")
        print(f"Username: {self.username}")
        print(f"User ID (auto-generated): {self.user_id}")

class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def display_expense_details(self, context="LOGGED"):
        print()
        print(f"===EXPENSE {context}===")
        print(f"Category: {self.category}")
        print(f"Amount: ${self.amount}")
        print(f"Description: {self.description}")
        print(f"Date: {self.date}")

class Income:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date
    def display_income_details(self, context="LOGGED"):
        print()
        print(f"===INCOME {context}===")
        print(f"Category: {self.category}")
        print(f"Amount: ${self.amount}")
        print(f"Description: {self.description}")
        print(f"Date: {self.date}")

class Asset:
    def __init__(self, amount, category, date, name):
        self.amount = amount
        self.category = category
        self.date = date
        self.name = name               
    def display_asset_details(self, context="REGISTERED"):
        print()
        print(f"===ASSET {context}===")
        print(f"Asset Type: {self.category}")
        print(f"Name / Description: {self.name}")
        print(f"Amount Invested: ${self.amount}")
        print(f"Date of Investment: {self.date}")

class Liability:
    def __init__(self, amount, category, name, date):
        self.amount = amount
        self.category = category
        self.name = name
        self.date = date

    def display_liability_details(self, context="REGISTERED"):
        print()
        print(f"===LIABILITY {context}===")
        print(f"Liability Type: {self.category}")
        print(f"Name / Description: {self.name}")
        print(f"Amount: ${self.amount}")
        print(f"Date: {self.date}")

first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
username = input("Enter a Username: ")

expenses_list = []
income_list = []
asset_list = []
liability_list = []

while True:
    try:
        pin = int(input("Enter a 6-digit PIN: "))
        if 100000 <= pin <= 999999:
            break
        else:
            print("PIN should be exactly 6-digits")
            continue
    except ValueError:
        print("Invalid Input")

user1 = User(first_name, last_name, username, pin)

while True:
    print()
    print("===FINTRACK MENU===")
    print("1. Log Expense")
    print("2. Log Income")
    print("3. Register Assets")
    print("4. Register Liabilities")
    print("5. View Account Details")
    print("6. View History")
    print("7. Exit")

    while True:
        try:
            choice = int(input("Enter your Choice (1-7): "))
            if 1 <= choice <= 7:
                break
            else:
                print("Enter a number between 1 and 7")
        except ValueError:
            print("Invalid Input")

    if choice == 7:
        print("Thank you for using FinTrack!!")
        break

    match choice:

        case 1:
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

            while True:
                try:
                    choice_of_expense = int(input("Enter your Expense Category Number: "))
                    if 1 <= choice_of_expense <= 10:
                        break
                    else:
                        print("Enter a number between 1 and 10")
                        continue
                except ValueError:
                    print("Invalid Input")
                
            expense_categories = {1:"Food & Dining",
                                2: "Transportation",
                                3: "Shopping",
                                4: "Bills & Utilities",
                                5: "Entertainment",
                                6: "Health & Medical",
                                7: "Education",
                                8: "Travel",
                                9: "Personal",
                                10: "Miscellaneous"}
            
            category = expense_categories[choice_of_expense]

            while True:
                try:
                    amount_expense = float(input("Enter your Expense Amount: "))
                    if amount_expense > 0:
                        break
                    else:
                        print("Enter an amount greater than zero")
                        continue
                except ValueError:
                    print("Invalid Input")
            description = input("Enter a Description: ")
            expense = Expense(amount_expense, category, description, datetime.date.today().strftime("%d-%m-%Y"))  # noqa: DTZ011
            expense.display_expense_details()
            expenses_list.append(expense)
            
        case 2:
            income_categories = {1:"Salary",
                                2:"Freelance / Business",
                                3:"Interest",
                                4:"Bonuses",
                                5:"Gifts",
                                6:"Refunds",
                                7:"Other"
                                }
            
            print("===INCOME CATEGORIES===")
            print("1. Salary")
            print("2. Freelance / Business")
            print("3. Interest")
            print("4. Bonuses")
            print("5. Gifts")
            print("6. Refunds")
            print("7. Other")

            while True:
                try:
                    choice_of_income = int(input("Enter your Income Category Number: "))
                    if 1 <= choice_of_income <= 7:
                        break
                    else:
                        print("Enter a number between 1 and 7")
                        continue
                except ValueError:
                    print("Invalid Input")

            income_category = income_categories[choice_of_income]

            while True:
                try:
                    income_amount = float(input("Enter the Income Amount: "))
                    if income_amount > 0:
                        break
                    else:
                        print("Enter a positive amount")
                        continue
                except ValueError:
                    print("Invalid Input")

            description = input("Enter a Description: ")

            income = Income(income_amount, income_category, description, datetime.date.today().strftime("%d-%m-%Y"))      # noqa: DTZ011
            income.display_income_details()
            income_list.append(income)

        case 3:
            asset_categories = {1:"Stocks",
                                2:"Mutual Funds",
                                3:"ETFs",
                                4:"Real Estate",
                                5:"Gold / Other Metals",
                                6:"Bonds",
                                7:"Cryptocurrency",
                                8:"Bank Deposits",}
            print("===ASSET CATEGORIES===")
            print("1. Stocks")
            print("2. Mutual Funds")
            print("3. ETFs")
            print("4. Real Estate")
            print("5. Gold / Other Metals")
            print("6. Bonds")
            print("7. Cryptocurrency")
            print("8. Bank Deposits")

            while True:
                try:
                    asset_choice = int(input("Enter your Asset Category Number: "))
                    if 1 <= asset_choice <= 8:
                        break
                    else:
                        print("Enter a number between 1 and 8")
                        continue
                except ValueError:
                    print("Invalid Input")

            asset_category = asset_categories[asset_choice]

            while True:
                try:
                    asset_amount = float(input("Enter the Amount Invested: "))
                    if asset_amount > 0:
                        break
                    else:
                        print("Enter a value greater than zero")
                except ValueError:
                    print("Invalid Input")

            asset_name = input("Enter the Name of the Asset or a Short Description: ")

            asset = Asset(asset_amount, asset_category, datetime.date.today().strftime("%d-%m-%Y"), asset_name)      # noqa: DTZ011
            asset.display_asset_details()
            asset_list.append(asset)

        case 4:
            liability_categories = {1:"Car Loan",
                                    2:"Home Loan",
                                    3:"Educational Loan",
                                    4:"Personal Loan",
                                    5:"Credit Card Debt",
                                    6:"Business Loan",
                                    7:"Others"}
            print()
            print("1. Car Loan")
            print("2. Home Loan")
            print("3. Educational Loan")
            print("4. Personal Loan")
            print("5. Credit Card Debt")
            print("6. Business Loan")
            print("7. Others")

            while True:
                try:
                    liability_choice = int(input("Enter the Liability Category Number: "))
                    if 1 <= liability_choice <= 7:
                        break
                    else:
                        print("Enter a number between 1 and 7")
                        continue
                except ValueError:
                    print("Invalid Input")

            while True:
                try:
                    liability_amount = float(input("Enter the Liability Amount: "))
                    if liability_amount > 0:
                        break
                    else:
                        print("Enter a positive value")
                        continue
                except ValueError:
                    print("Invalid Input")

            liability_category = liability_categories[liability_choice]

            liability_name = input("Enter a Name or Description: ")

            liability = Liability(liability_amount, liability_category, liability_name, datetime.date.today().strftime("%d-%m-%Y"))    # noqa: DTZ011
            liability.display_liability_details()
            liability_list.append(liability)

        case 5:
            print()
            user1.display_details()

        case 6:
            print("===MENU===")
            print("1. Expense History")
            print("2. Income History")
            print("3. Asset Registration History")
            print("4. Liability Registration History")
            while True:
                try:
                    choice_of_history = int(input("Enter your History Category Number: "))
                    if 1 <= choice_of_history <= 4:
                        break
                    else:
                        print("Enter a number between 1 and 4")
                        continue
                except ValueError:
                    print("Invalid Input")
            match choice_of_history:
                case 1:
                    for entry in expenses_list:
                        entry.display_expense_details(context="HISTORY")
                case 2:
                    for entry in income_list:
                        entry.display_income_details(context="HISTORY")
                case 3:
                    for entry in asset_list:
                        entry.display_asset_details(context="REGISTRATION HISTORY")
                case 4:
                    for entry in liability_list:
                        entry.display_liability_details(context="REGISTRATION HISTORY")
