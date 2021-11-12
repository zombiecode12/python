class goldfishbread:
    def make_bread(self, ingredients, price):
        self.ingredients = ingredients
        self.price = price

    def see_bread(self):
        print(self.ingredients, self.price)



a = goldfishbread()
b = goldfishbread()

a.make_bread('팥', 30000)
b.make_bread('계피', 50000)

a.see_bread()
b.see_bread()
