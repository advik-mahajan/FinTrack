# USER ACCOUNT CREATION / ACCOUNT LOGIN

class User:
    user_id_counter = 0
    def __init__(self, first_name, last_name, username, pin):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.pin = pin
        User.user_id_counter += 1
        self.user_id = User.user_id_counter

    def display_account_details(self):
        print("===ACCOUNT DETAILS===")
        print(f"NAME: {self.first_name} {self.last_name}")
        print(f"USERNAME: {self.username}")
        print(f"USER ID (auto-generated): {self.user_id}")

    def change_pin(self):
        while True:
            try:
                current_pin = int(input("Enter your Current PIN: "))
                if 100000 <= current_pin <= 999999:
                    if current_pin == self.pin:
                        print("PIN Authentication Successful!")

                        while True:
                            try:
                                new_pin = int(input("Enter your New PIN: "))
                                if 100000 <= new_pin <= 999999:
                                    self.pin = new_pin
                                    print("Your new PIN has been updated successfully!")
                                    break
                                else:
                                    print("Enter a 6-digit PIN")
                                    continue
                            except ValueError:
                                print("Invalid Input! Please Try Again.")
                        break
                    else:
                        print("PIN Authentication Unsuccessful! Please Try Again.")
                        continue
                else:
                    print("The PIN you entered was not 6-digits. Please try again")
                    continue
            except ValueError:
                print("Invalid Input! Please Try Again.")
