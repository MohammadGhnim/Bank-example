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
        self.balance = 0



    def withdrow(self, amount):
        self.balance -= amount
        print(f'Your current balance : {self.balance}')

    def deposite(self, amount):
        self.balance += amount
        print(f'Your current balance : {self.balance}')

c1= Bank('ahmad', 23)

c1.deposite(500)
c1.withdrow(200)
    
