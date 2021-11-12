class goldfishbread:
    def make_bread(self, ingredients, price):
        self.ingredients = ingredients
        self.price = price
    def see_bread(self):
        print(self.ingredients, self.price)

    def __add__(self, other):
        return self.price + other.price
a = goldfishbread()
b = goldfishbread()

a.make_bread("팥", 30000)
b.make_bread("슈크림", 40000)


print("붕어빵 2개에 %d원"%int(a+b))
