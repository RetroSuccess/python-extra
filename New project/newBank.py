class Account:
    account_number = ""
    balance = 0
    
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self):
        self.balance += float(input("Enter amount to deposit: "))
        print(f"Deposited. New balance: {self.balance}")
        
    def withdraw(self,amount):
        self.balance -= amount
        

accn = input("Enter account number: ")
john = Account(accn, 1000)
accn = input("Enter account number: ")
rose = Account(accn, 2000)
print("Acoount number>>", john.account_number)
print("Balance>>", john.balance)
print("New balance after deposit:",john.deposit())
print("")
print("Acoount number>>", rose.account_number)
print("Balance>>", rose.balance)
print("New balance after deposit:",rose.deposit())
