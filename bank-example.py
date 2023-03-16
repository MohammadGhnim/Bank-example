'''
Bank example:

      - create client (name, age )
      - withdrow
      - deposite
      - show details
      - show balance

'''

class Bank:
    def __init__(self, name, age):
        print(f'welcome {name}')
        self.name = name
        self.age = age
        self.balance = 0



    def withdrow(self, amount):
        self.balance -= amount
        print(f'Your current balance : {self.balance}')

    def deposite(self, amount):
        self.balance += amount
        print(f'Your current balance : {self.balance}')


    def show_details(self):
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')

    def show_balance(self):
        print(f'Your current balance : {self.balance}')
c1 = Bank('ahmad', 23)

c1.deposite(500)
c1.withdrow(200)
c1.show_details()
c1.show_balance()
