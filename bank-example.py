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
        if (self.balance - amount) < -501:
            print(self.balance - amount)
            print(f'you don not have enough balance : {self.balance}')
        else:
            self.balance -= amount
            self.show_balance()
        

    def deposite(self, amount):
        self.balance += amount
        self.show_balance()


    def show_details(self):
        print(f'Name : {self.name}')
        print(f'Age  : {self.age}')

    def show_balance(self):
        print(f'Your current balance : {self.balance}')

        
c1 = Bank('ahmad', 23)

c1.withdrow(200)
c1.withdrow(200)
c1.withdrow(100)

c1.show_details()
c1.show_balance()



'''
#add more client

c2 = Bank('hassan', 25)
c2.deposite(1000)
c2.withdrow(100)
c2.show_details()
c2.show_balance()
'''
