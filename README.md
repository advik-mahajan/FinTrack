# FinTrack

A command-line Personal Finance Management Application built in Python using Object Oriented Programming (OOP) Principles.

FinTrack allows users to manage their personal finances directly through a terminal-based interface. Users can Record Income and Expenses, Register Assets and Liabilities, View Transaction History and Manage their Account.

Current Status: MVP (Actively in Development)

# FEATURES:

1) User Account Management:
- Create a new user account
- Login using username and PIN
- View account details
- Change PIN

2) Log Expenses:
- Record expenses across 10 categories: Food & Dining, Transportation, Shopping, Bills & Utilities, Entertainment, Health & Medical, Education, Travel, Personal, Miscellaneous

3) Log Income:
- Record income across 5 categories: Salary, Freelance, Business, Bonuses / Gifts / Refunds, Others

4) Register Assets:
- Track assets across 8 categories: Stocks, Mutual Funds, ETFs, Real Estate, Gold & Other Metals, Bonds, Cryptocurrencies, Bank Deposits

5) Register Liabilities:
- Track Liabilities across 7 categories: Car Loan, Home Loan, Educational Loan, Personal Loan, Business Loan, Credit Card Debt, Others

6) View Transaction History:
- View previously recorded transactions
- Displays transaction ID, type, category, amount, description and date

7) Persistent Storage:
- User data is stored in CSV (comma-separated files)
- Transactions, assets, liabilities and user accounts persist between sessions

# TECHNOLOGY & CONCEPTS:
- Python 3.x
- Object Oriented Programming - User, Transaction, Asset, Liability, FinanceManager
- CSV File Handling for persistent storage
- Input validation using loops, conditional checks and exceptional handling
- Datetime Module for automatic transaction date logging
- Modular programming using separate Python files for different components

# PROJECT STRUCTURE:
FinTrack/
|

|--fintrack_main.py

|--user.py

|--transaction.py

|--asset.py

|--liability.py

|--finance_manager.py

|--storage_manager.py

|--file_setup.py

|

|--users.csv

|--transactions.csv

|--assets.csv

|--liabilities.csv


# HOW TO RUN:
1) Clone the repository
2) Open the project directory in a terminal
3) Run the setup file (file_setup.py) to initialize the CSV Files
4) Start FinTrack (python main.py)
5) Create an account or log in using existing account

# FUTURE ROADMAP:
1) Editing and deleting transactions, assets and liabilities
2) Financial summary and analytics dashboard
3) Total income and expense calculations
4) Spending analysis by category
5) Budget tracking
6) Database based storage
7) Improved UI (possibly proper frontend)
