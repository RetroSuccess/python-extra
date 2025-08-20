# Define a class for a Bank Account
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner       # attribute
        self.balance = balance   # attribute

    # Deposit method
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    # Withdraw method
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    # Display account details
    def display(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}")


# 🔹 Create objects (bank accounts)
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

# 🔹 Use the objects
acc1.display()          # Owner: Alice, Balance: 1000
acc2.display()          # Owner: Bob, Balance: 500

acc1.deposit(200)       # Deposited 200. New balance: 1200
acc1.withdraw(1500)     # Insufficient funds!
acc2.withdraw(200)      # Withdrew 200. New balance: 300


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price  # Fixed assignment
    
    def set_title(self, title):
        self.title = title  
        
    def set_author(self, author):
        self.author = author
        
book1 = Book("Python Basics", "John Doe", 250)
print(book1.get_price())

book1.set_price(300)       # update price
print(book1.get_price())   # 300