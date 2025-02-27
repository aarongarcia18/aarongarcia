class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Book: {self.title} by {self.author} ({self.year_published})")

book1 = Book("The Year of the Conquest", "David Howarth", 1066)
book2 = Book("Countdown to War", "Richard Overy", 1939)
book3 = Book("A Global History", "John E. Wills Jr.", 1688)

book1.describe()
book2.describe()
book3.describe()
