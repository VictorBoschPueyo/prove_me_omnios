

class Book:
    def __init__ (self, name = "", rating = 0, price = 0.0, picture = ""):
        self.name = name
        self.rating = rating
        self.price = price
        self.picture = picture

    def show_book_info(self):
        print("The book " + self.name + " costs " + self.price + " and has a rating of " + self.rating + " star.")