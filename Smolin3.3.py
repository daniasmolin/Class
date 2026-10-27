class BankAccount:
    def __init__(self, owner_name, account_number, balance=0.0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Рахунок {self.account_number}: поповнено на {amount:.2f} грн.")
        else:
            print("Сума поповнення має бути більшою за нуль.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Рахунок {self.account_number}: знято {amount:.2f} грн.")
        else:
            print(f"Рахунок {self.account_number}: недостатньо коштів або невірна сума.")

    def __str__(self):
        return f"Рахунок: {self.account_number} | Власник: {self.owner_name} | Баланс: {self.balance:.2f} грн"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, owner_name, account_number, initial_balance=0.0):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(owner_name, account_number, initial_balance)

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def transfer(self, from_account_number, to_account_number, amount):
        sender = self.get_account(from_account_number)
        receiver = self.get_account(to_account_number)

        if not sender:
            print(і := f"Рахунок відправника {from_account_number} не знайдено.")
            return
        if not receiver:
            print(f"Рахунок отримувача {to_account_number} не знайдено.")
            return

        if 0 < amount <= sender.balance:
            sender.balance -= amount
            receiver.balance += amount
            print(f"Переказано {amount:.2f} грн з рахунку {from_account_number} на рахунок {to_account_number}.")
        else:
            print(f"Рахунок {from_account_number}: недостатньо коштів для переказу.")

    def display_accounts(self):
        for acc in self.accounts.values():
            print(acc)


bank = Bank()
bank.add_account("Олександр", "UA12345", 1000.0)
bank.add_account("Марія", "UA67890", 500.0)

acc1 = bank.get_account("UA12345")
acc1.withdraw(200.0)

bank.transfer("UA12345", "UA67890", 300.0)

print("\nОновлені баланси:")
bank.display_accounts()