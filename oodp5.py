"""Create a class Book with attributes title, author, and price. Create 5 objects and print the details."""


class book():
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("title of the book is:", self.title)
        print("the author of the book is:", self.author)
        print("the price of the book is:", self.price)


b1 = book("harry potter", "JK rowling", 2400)
b2 = book("the jungle book", "raman", 2400)
b1.display()
b2.display()

