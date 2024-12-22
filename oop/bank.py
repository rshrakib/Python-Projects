class Transaction:
    def __init__(self, amount, transaction_type):
        self.amount = amount
        self.transaction_type = transaction_type




class Account:
    def __init__(self, acc_no, holder_name, balance=0):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.balance = balance
        self.Transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance+= amount
            self.Transactions.append(Transaction(amount, 'Deposit'))
            print(f"Deposit Successful of amount {amount}. New balance : {self.balance}")
        else:
            print("Invalid Deposit amount.")
    def withdraw(self, amount):
        if 0< amount <= self.balance:
            self.balance-=amount
            self.Transactions.append(Transaction(amount,'Withdraw'))
            print(f"Withdraw {amount} is successful. New balance: {self.balance}")
        else:
            print("Withdraw unsuccessful. Invalid amount")
    def display_transaction(self):
        print("\nTransaction History")
        for transaction in self.Transactions:
            print(f"{transaction.amount}: {transaction.transaction_type}")
    def display_balance(self):
        print(f"\n Current balance for Account {self.acc_no}: {self.balance}")


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
    def create_account(self, acc_no, holder_name, initial_balance=0):
        if acc_no not in self.accounts:
            new_acc = Account(acc_no, holder_name, initial_balance)
            self.accounts[acc_no] = new_acc
            print(f"Account Created successful for the {holder_name}. Account number: {acc_no}. Balance : {initial_balance}")
        else:
            print("Account number already exists")

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)



bank = Bank("AB Bank")

rakib_acc = bank.create_account(1, "Rakibul Hasan", 500)
riyad_acc = bank.create_account(2, "Riyad", 1000)


riyad_acc = bank.get_account(2)
rakib_acc = bank.get_account(1)


rakib_acc.deposit(200)
riyad_acc.deposit(500)

rakib_acc.withdraw(500)
riyad_acc.withdraw(2000)


rakib_acc.displa