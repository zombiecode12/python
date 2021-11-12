class goldfishbread:
    banjook = '밀가루'
    def make_bread(self, ingredients, price):
        self.ingredients = ingredients
        self.price = price
    def see_bread(self):
        print(self.ingredients, self.price)

    def see_banjook(cls):
        print(cls.banjook)


a = goldfishbread()
b = goldfishbread()

a.see_banjook()
b.see_banjook()
goldfishbread.banjook = "미숫가루"

a.see_banjook()
b.see_banjook()
