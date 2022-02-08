class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawal(self, amount):
        self.amount -= amount


    def display_user_balance(self):
        print(f"User: {self.name } Balance: {self.amount}")

    def transnfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()

zoe = User("Zoe")
athena = User("Athena")
maya = User("Maya")

zoe.make_deposit(110)
zoe.make_deposit(5)
zoe.make_deposit(20)
zoe.make_withdrawal(5)
zoe.display_user_balance()

athena.make_deposit(35)
athena.make_deposit(15)
athena.make_withdrawal(20)
athena.display_user_balance()

maya.make_deposit(10)
maya.make_withdrawal(1)
maya.make_withdrawal(2)
maya.make_withdrawal(2)
maya.display_user_balance()

zoe.transnfer_money(5, maya)

maya.transnfer_money(1, athena)