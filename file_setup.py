import os
import csv

file_path_users = "users.csv"
file_path_transactions = "transactions.csv"
file_path_assets = "assets.csv"
file_path_liabilities = "liabilities.csv"

users_list = [["User ID", "First Name", "Last Name", "Username", "PIN"]]
transactions_list = [["User ID", "Transaction ID", "Transaction Type", "Category", "Amount", "Description", "Date"]]
assets_list = [["User ID", "Asset ID", "Asset Type", "Asset Name", "Value"]]
liabilities_list = [["User ID", "Liability ID", "Liability Type", "Liability Name", "Principal", "Outstanding Value"]]


if not os.path.exists(file_path_users):
    with open(file_path_users, "w", newline="") as file1:
        writer = csv.writer(file1)
        for row in users_list:
            writer.writerow(row)


if not os.path.exists(file_path_transactions):
    with open(file_path_transactions, "w", newline="") as file2:
        writer = csv.writer(file2)
        for row in transactions_list:
            writer.writerow(row)


if not os.path.exists(file_path_assets):
    with open(file_path_assets, "w", newline="") as file3:
        writer = csv.writer(file3)
        for row in assets_list:
            writer.writerow(row)


if not os.path.exists(file_path_liabilities):
    with open(file_path_liabilities, "w", newline="") as file4:
        writer = csv.writer(file4)
        for row in liabilities_list:
            writer.writerow(row)
