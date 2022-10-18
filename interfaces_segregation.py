# the interfaces segregation script
#  - this script is used to segregate the interfaces into different groups
#    based on the interface type

"""Interface Segregation Principle(ISP):
Actually, This principle suggests that “A client should not be forced to implement an interface that it does not use”

Example:
Violation of ISP
"""


class Shape:
   """A demo shape class"""
   def draw_circle(self):
       """Draw a circle"""
       raise NotImplemented
   def draw_square(self):
       """ Draw a square"""
       raise NotImplemented
   
class Circle(Shape):
    """A demo circle class"""
    def draw_circle(self):
        """Draw a circle"""
        pass
    def draw_square(self):
        """ Draw a square"""
        pass


"""In the above example, we need to call an unnecessary method in the Circle class. Hence the example violated the Interface Segregation Principle.
Solution:"""

class Shape:
   """A demo shape class"""
   def draw(self):
      """Draw a shape"""
      raise NotImplemented
class Circle(Shape):
   """A demo circle class"""
   def draw(self):
      """Draw a circle"""
      pass
class Square(Shape):
   """A demo square class"""
   def draw(self):
      """Draw a square"""
      pass
   

# Another example of the ISP

class BankAccount:
   """A demo Bank Account class"""
   def __init__(self, balance: float, account: str):
       self.account = {f"{account}": balance}
   def balance(self, account: str):
       """Get current balance"""
       raise NotImplemented
class Deposit(BankAccount):
   """A demo circle class"""
   def balance(self, account: str):
      """Get current balance"""
      return self.account.get(account)
   def deposit(self, amount: float, account: str):
       """Deposit a new amount"""
       current = self.balance(account)
       new_amount = current + amount
       self.account.update({account: new_amount})