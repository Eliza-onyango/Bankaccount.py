class BankAccount:
    def __init__(self,balance):
        self.balance = balance
        print('HELLO!!!!!! WELCOME TO EQUITY BANK')
    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount =float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n Your withdrawal is successful:", amount)
        else:
            print("\n Insufficient balance  ")
    def check_balance(self):
        print("\n My  Balance is =", self.balance)
    def customer_details(self):
        name = input('Enter your name:')
        account = int(input('Enter your account number: '))
        date_of_opening =input('Enter date of opening the account :')
        print(f'my name is {name} and my account number is {account} and date of opening the account is {date_of_opening} ')
        print("\n Net Available Balance =", self.balance)


bank = BankAccount(10000)

bank.deposit()
bank.withdraw()
bank.customer_details()
