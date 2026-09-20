import csv

file_path_users = "users.csv"
file_path_transactions = "transactions.csv"
file_path_assets = "assets.csv"
file_path_liabilities = "liabilities.csv"

def get_next_user_id():
    users = load_users()

    if not users:
        return 1

    user_ids = [int(row[0]) for row in users]
    return max(user_ids) + 1

def update_user_pin(user_id, new_pin):
    users = []

    with open(file_path_users, "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)

        for row in reader:
            if int(row[0]) == user_id:
                row[4] = str(new_pin)
                users.append(row)

    with open(file_path_users, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(users)

def add_user(user):
    with open(file_path_users, "a", newline="") as file1:
        writer = csv.writer(file1)
        writer.writerow([user.user_id, user.first_name, user.last_name, user.username, user.pin])

def add_transaction(transaction):
    with open(file_path_transactions, "a", newline="") as file2:
        writer = csv.writer(file2)
        writer.writerow([transaction.user_id, transaction.transaction_id, transaction.transaction_type, transaction.category, transaction.amount, transaction.description, transaction.date])

def add_asset(asset):
    with open(file_path_assets, "a", newline="") as file3:
        writer = csv.writer(file3)
        writer.writerow([asset.user_id, asset.asset_id, asset.asset_type, asset.name, asset.value])

def add_liability(liability):
    with open(file_path_liabilities, "a", newline="") as file4:
        writer = csv.writer(file4)
        writer.writerow([liability.user_id, liability.liability_id, liability.liability_type, liability.name, liability.principal, liability.outstanding_amount])

def load_users():
    users = []

    with open(file_path_users, "r", newline="") as file1:
        reader = csv.reader(file1)
        next(reader)

        for row in reader:
            users.append(row)

    return users

def load_transactions():
    transactions = []

    with open(file_path_transactions, "r", newline="") as file2:
        reader = csv.reader(file2)
        next(reader)

        for row in reader:
            transactions.append(row)
    return transactions

def load_assets():
    assets = []

    with open(file_path_assets, "r", newline="") as file3:
        reader = csv.reader(file3)
        next(reader)

        for row in reader:
            assets.append(row)
    return assets

def load_liabilities():
    liabilities = []

    with open(file_path_liabilities, "r", newline="") as file4:
        reader = csv.reader(file4)
        next(reader)

        for row in reader:
            liabilities.append(row)
    return liabilities
