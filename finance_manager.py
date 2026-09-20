from transaction import Transaction
from asset import Asset
from liability import Liability



class FinanceManager:
    def __init__(self, current_user):
        self.current_user = current_user
        self.transactions = []
        self.assets = []
        self.liabilities = []

    def add_transaction(self, transaction):
        if transaction.user_id == self.current_user.user_id:
            self.transactions.append(transaction)

    def view_transaction(self, transaction):
        transaction.display_transaction_details()

    def add_assets(self, asset):
        if asset.user_id == self.current_user.user_id:
            self.assets.append(asset)

    def view_asset(self, asset):
        asset.display_asset_details()

    def add_liability(self, liability):
        if liability.user_id == self.current_user.user_id:
            self.liabilities.append(liability)

    def view_liability(self, liability):
        liability.display_liability_details()
