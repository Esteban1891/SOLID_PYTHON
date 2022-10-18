# the liskov substitution principle
#   - if S is a subtype of T, then objects of type T may be replaced with objects of type S without altering any of the desirable properties of the program
#   - the liskov substitution principle is a refinement of the open closed principle

"""
Liskov Substitution Principle(LSP):
    Let φ(x) be a property provable about objects x of type T. Then φ(y) should be true for objects y of type S where S is a subtype of T.
    More formally, this is the original definition (LISKOV 01) of Liskov`s substitution principle: if S is a subtype of T, then objects of type T
    may be replaced by objects of type S, without breaking the program.
"""



"""Example
Violation of LSP
"""
class Vehicle:
   """A demo Vehicle class"""

   def __init__(self, name: str, speed: float):
       self.name = name
       self.speed = speed

   def get_name(self) -> str:
       """Get vehicle name"""
       return f"The vehicle name {self.name}"

   def get_speed(self) -> str:
       """Get vehicle speed"""
       return f"The vehicle speed {self.speed}"

   def engine(self):
       """A vehicle engine"""
       pass

   def start_engine(self):
       """A vehicle engine start"""
       self.engine()


class Car(Vehicle):
   """A demo Car Vehicle class"""
   def start_engine(self):
       pass


class Bicycle(Vehicle):
   """A demo Bicycle Vehicle class"""
   def start_engine(self):
       pass
   

"""In Bicycle class violates the LSP. Cause in the Vehicle class has an engine method. But naturally, a bicycle has no engine. So we could not start any engine.
Refactor the code and make a solution for this problem.
Solution:
"""

class Vehicle:
   """A demo Vehicle class"""
   def __init__(self, name: str, speed: float):
       self.name = name
       self.speed = speed
   def get_name(self) -> str:
       """Get vehicle name"""
       return f"The vehicle name {self.name}"
   def get_speed(self) -> str:
       """Get vehicle speed"""
       return f"The vehicle speed {self.speed}"
   

class VehicleWithoutEngine(Vehicle):
   """A demo Vehicle without engine class"""
   def start_moving(self):
      """Moving"""
      raise NotImplemented
   

class VehicleWithEngine(Vehicle):
   """A demo Vehicle engine class"""
   def engine(self):
      """A vehicle engine"""
      pass
   def start_engine(self):
      """A vehicle engine start"""
      self.engine()


class Car(VehicleWithEngine):
   """A demo Car Vehicle class"""
   def start_engine(self):
       pass
   

class Bicycle(VehicleWithoutEngine):
   """A demo Bicycle Vehicle class""" 
   def start_moving(self):
       pass
   
"""Actually, LSP is a concept that applies to all kinds of polymorphism. Only if you don’t use polymorphism of all you don’t need to care about the LSP.
"""