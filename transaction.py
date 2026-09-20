import datetime

class Transaction:
    transaction_id_counter = 0
    def __init__(self, user_id, transaction_type, category, amount, description):
        self.user_id = user_id
        self.transaction_type = transaction_type
        self.category = category
        self.amount = amount
        self.date = datetime.date.today().strftime("%d/%m/%Y")
        self.description = description
        Transaction.transaction_id_counter += 1
        self.transaction_id = Transaction.transaction_id_counter

    def display_transaction_details(self):
        print("===TRANSACTION DETAILS===")
        print(f"TRANSACTION ID (auto-generated) : {self.transaction_id}")
        print(f"TRANSACTION TYPE: {self.transaction_type}")
        print(f"CATEGORY: {self.category}")
        print(f"AMOUNT:  ₹{self.amount}")
        print(f"DESCRIPTION: {self.description}")
        print(f"DATE: {self.date}")
