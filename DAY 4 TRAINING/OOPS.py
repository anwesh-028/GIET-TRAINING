#OOPS concept
#Q1

'''class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num

obj=Example(10) 
print(obj.get_num()) 
obj.set_num(15)
print(obj.get_num())


class Customer:
    def __init__(self , cust_id):
        cust_id = 90
        
cust_id = Customer()
print(c1.cust_id)

#Q2

class Book:
    def init(self):
        self.title=None

my_fav=Book()
my_fav.title="Head First Programming"
your_fav=Book()
your_fav.title="Learn Python the hard way"
my_fav.title="Learning Python"

print("My favorite is",my_fav.title)
print("Your's is",your_fav.title)

#Q3

class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
s1=Shoe(2000,"Canvas")
print("The unique id of the object is ",id(s1))
print(s1)
print(s1.price,s1.material)


#Q4

class Mobile:
    def display(self):
        print("Displaying details")

        
    def purchase(self):
        self.display()
        print("calculating price")
Mobile().purchase()

#Q5

class Mobile:
    def __init__(self, brand, price):
        self.brand=brand
        self.price=price
        self.total_price = None
    def purchase(self):
        if self.brand=="Apple":
            discount=10
        else:
            discount=5
        self.total_price = self.price- self.price*(discount/100)
        print("Total price of", self.brand, "mobile is", self.total_price)
    def amount_returned(self):
        return (self.price - self.total_price)

mob1=Mobile("Apple",20000)
mob2=Mobile("Samsung",10000)
mob1.purchase()
mob2.purchase()
print(mob1.amount_returned())
print(mob2.amount_returned())'''


#Q6

class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id= cust_id
        self.name = name
        self.age = age
        self.wallet_balance = wallet_balance
    def update_balance(self, amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount
    def show_balance(self):
        print("The balance is ", self.wallet_balance)
c1=Customer(100, "Gopal", 24, 1000)
c1.update_balance(500)
c1.show_balance()














