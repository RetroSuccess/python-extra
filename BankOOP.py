class Bank:
    def __init__(self, owwner, balance):
        self.owner = owwner
        self.balance = balance
        
    def deposit(self, balance):
        self.balance += balance
        print(f"Deposited: +{balance}")
        
    def withdraw(self, balance):
        if balance > self.balance:
            print("Error")
        else:
            self.balance -= balance
            print(f"Withdrew: -{balance}")
    
bank = Bank("Abdeyay", 2000)
print("\nBank info:")
print("Owner: ", bank.owner)
print("Balance: ", bank.balance)
bank.deposit(500)
print("Balance: ", bank.balance)
bank.withdraw(1000)
print("Balance: ", bank.balance)

class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title
        
    def get_author(self):
        return self.author
    
    def set_author(self, author):
        self.author = author
        
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year
        
book = Book("Python", "Tony", 2020)

print("\nBook info:")
print("Title: ", book.get_title())
print("Author: ", book.get_author())
print("Year: ", book.get_year())
