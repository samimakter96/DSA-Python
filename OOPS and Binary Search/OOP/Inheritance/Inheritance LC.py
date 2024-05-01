class Father:
    def lands(self):
        print("Having 50 Acar Lands")


class Son(Father):
    def money(self):
        print("Having 10 Lakhs money")


s = Son()
s.lands()   # son can access father lands
s.money()


