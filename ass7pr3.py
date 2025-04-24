class BankAccount:
    def __init__(self, acc_no, holder, bal=0.0):
        self.acc_no = acc_no
        self.holder = holder
        self.bal = bal

    def deposit(self, amt):
        if amt > 0:
            self.bal += amt
            print(f"Deposited: ${amt}. New Balance: ${self.bal}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amt):
        if 0 < amt <= self.bal:
            self.bal -= amt
            print(f"Withdrawn: ${amt}. New Balance: ${self.bal}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        print(f"Account Balance: ${self.bal}")
        return self.bal

class Bank:
    def __init__(self, name):
        self.name = name
        self.accts = {}

    def create_account(self, acc_no, holder, init_bal=0.0):
        if acc_no in self.accts:
            print("Account already exists.")
        else:
            self.accts[acc_no] = BankAccount(acc_no, holder, init_bal)
            print(f"Account created for {holder} with balance ${init_bal}")

    def get_account(self, acc_no):
        return self.accts.get(acc_no, None)

    def display_accounts(self):
        print(f"Accounts in {self.name}:")
        for acc_no, acc in self.accts.items():
            print(f"{acc_no}: {acc.holder}, Balance: ${acc.bal}")

# Menu-driven Interface
bank = Bank("MyBank")
while True:
    print("\nMenu:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Accounts")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        acc_no = int(input("Enter account number: "))
        holder = input("Enter account holder name: ")
        init_bal = float(input("Enter initial balance: "))
        bank.create_account(acc_no, holder, init_bal)
    elif choice == '2':
        acc_no = int(input("Enter account number: "))
        account = bank.get_account(acc_no)
        if account:
            amt = float(input("Enter deposit amount: "))
            account.deposit(amt)
        else:
            print("Account not found.")
    elif choice == '3':
        acc_no = int(input("Enter account number: "))
        account = bank.get_account(acc_no)
        if account:
            amt = float(input("Enter withdrawal amount: "))
            account.withdraw(amt)
        else:
            print("Account not found.")
    elif choice == '4':
        bank.display_accounts()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")
