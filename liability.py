class Liability:
    liability_id_counter = 0
    def __init__(self, user_id, liability_type, name, principal, outstanding_amount):
        self.user_id = user_id
        self.liability_type = liability_type
        self.name = name
        self.principal = principal
        self.outstanding_amount = outstanding_amount
        Liability.liability_id_counter += 1
        self.liability_id = Liability.liability_id_counter

    def display_liability_details(self):
        print("===LIABILITY DETAILS===")
        print(f"LIABILITY ID (auto-generated): {self.liability_id}")
        print(f"LIABILITY TYPE: {self.liability_type}")
        print(f"NAME: {self.name}")
        print(f"PRINCIPAL: {self.principal}")
        print(f"OUTSTANDING AMOUNT: {self.outstanding_amount}")
