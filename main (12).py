class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited {amount} units. New balance: {self.__account_balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew {amount} units. New balance: {self.__account_balance}")
        else:
            print("Withdrawal amount must be greater than zero and less than or equal to the account balance.")

    def display_balance(self):
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Balance: {self.__account_balance}")


# Testing the BankAccount class
if __name__ == "__main__":
    account = BankAccount("1234567890", "John Doe", 1000)

    account.display_balance()  # Should display the initial balance

    account.deposit(500)  # Depositing 500 units
    account.withdraw(200)  # Withdrawing 200 units

    account.display_balance()  # Should display the updated balance after transactions