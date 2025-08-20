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
        self.price = price 
    
    def set_title(self, title):
        self.title = title  
        
    def set_author(self, author):
        self.author = author
        
book1 = Book("gfkf", "John Doe", 250)

print(book1.get_price())
