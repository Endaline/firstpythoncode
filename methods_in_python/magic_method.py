# magic method = A magic method is a special method in Python that starts and ends with double underscores (e.g., __init__, __str__, __add__).
# Magic methods allow you to define the behavior of your objects for built-in operations, such as addition, string representation, and comparison.
# They are also known as dunder methods (short for "double underscore").
# Magic methods are not called directly; instead, they are invoked by Python when you perform certain operations on objects.

class Book:

    def __init__(self,author,title,num_of_pages):
        self.author = author
        self.title = title
        self.num_of_pages = num_of_pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.num_of_pages}" 

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_of_pages < other.num_of_pages
    
    def __gt__(self, other):
        return self.num_of_pages > other.num_of_pages
    
    def __add__(self, other):
        return f'{self.num_of_pages + other.num_of_pages} pages'
    
    def __contains__(self, word):
        return word in self.title or word in self.author
    
    def __getitem__(self,key):
        if key =="title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_of_pages":
            return self.num_of_pages
        else:
            return "Invalid key"

book1 = Book("J.K. Rowling", "Harry Potter and the Philosopher's Stone", 223)
book2 = Book("J.R.R. Tolkien", "The Hobbit", 310)
book3 = Book("George R.R. Martin", "A Game of Thrones", 694)
print(book3)
print(book1 == book2) 
print(book1 < book2) 
print(book3 > book2) 
print(book3 + book2) 
print("Harry" in book1)
print("Lion" in book2)
print("Game" in book3)
print(book1["title"])
print(book2["title"])
print(book3["title"])
print(book1["author"])
print(book2["author"])
print(book3["author"])
print(book1["num_of_pages"])
print(book2["num_of_pages"])
print(book3["num_of_pages"])