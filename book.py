

class Book:
    def __init__ (self, id = 0, name = "", rating = 0, currency = 'pound', money = 0.0, picture = ""):
        self.ID = id
        self.name = name
        self.rating = rating
        self.price = { currency : money }
        self.picture = picture
        self.text = {}

    def set_price(self, currency, money):
        self.price[currency] = money

    def set_text(self, language, text):
        self.text[language] = text

    def show_book_info(self):
        print("The book " + self.name + " costs " + self.price + " and has a rating of " + self.rating + " star.")
    
    def get_all_info(self):
        data = [self.ID, self.name, self.rating]

        for curr in self.price.keys():
            data.append(self.price[curr])

        data.append(self.picture)

        for lang in self.text.keys():
            data.append(self.text[lang])

        return data