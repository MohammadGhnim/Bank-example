'''
Bank example:

      - create client (name, age )
      - withdrow
      - deposite
      - show details
      - show balance

'''
class User:
    def __init__(self, name, age):
        print(f'welcome {name}')
        self.name = name
        self.age = age


    def show_details(self):
        print(f'Name : {self.name}')
        print(f'Age  : {self.age}')

        
    
class Bank(User):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.balance = 0



    def withdrow(self, amount):
        if amount > self.balance:
            print(f'you don not have enough balance : {self.balance}')
            return
        
        self.balance -= amount
        self.show_balance()
        

    def deposite(self, amount):
        self.balance += amount
        self.show_balance()


    

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
