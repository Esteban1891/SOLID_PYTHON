# open closed principle
# open for extension, closed for modification
# open for extension means that we can add new functionality to the code without modifying the existing code
# closed for modification means that we can modify the existing code without adding new functionality

"""
    Software entities (classes, function, module) open for extension, but not for modification (or closed for modification)

    Example:
        Violation of OCP
"""

class Discount:
   """Demo customer discount class"""
   def __init__(self, customer, price):
       self.customer = customer
       self.price = price
   def give_discount(self):
       """A discount method"""
       if self.customer == 'normal':
           return self.price * 0.2
       elif self.customer == 'vip':
           return self.price * 0.4
       

"""
But this solution violates the OCP. Because we can`t modify the give_discount method. Only we can extend the method.

    def give_discount(self):
       'A discount method'
       if self.customer == 'normal':
           return self.price * 0.2
       elif self.customer == 'vip':
           return self.price * 0.4
        # extra discount for vip customer
       elif self.customer ==  'supvip':
           return self.price * 0.8
"""

"""solution"""

class Discount:
   """Demo customer discount class"""
   def __init__(self, customer, price):
       self.customer = customer
       self.price = price
   def get_discount(self):
       """A discount method"""
       return self.price * 0.2
   

class VIPDiscount(Discount):
   """Demo VIP customer discount class"""
   def get_discount(self):
       """A discount method"""
       return super().get_discount() * 2
   
   
class SuperVIPDiscount(VIPDiscount):
   """Demo super vip customer discount class"""
   def get_discount(self):
       """A discount method"""
       return super().get_discount() * 2