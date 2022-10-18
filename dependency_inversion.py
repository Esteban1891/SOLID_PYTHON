# the dependency inversion principle
# the dependency inversion principle states that high-level modules should not depend on low-level modules. Both should depend on abstractions.
# abstractions should not depend on details. Details should depend on abstractions.

# Example:
"""Dependency Inversion Principle(DIP):
This principle suggests that below two points.
a. High-level modules should not depend on low-level modules. Both should depend on abstractions.
b. Abstractions should not depend on details. Details should depend on abstractions.

Example:
Violation of DIP
"""
class BackendDeveloper:
    """This is a low-level module"""
    @staticmethod
    def python():
        print("Writing Python code")
class FrontendDeveloper:
    """This is a low-level module"""
    @staticmethod
    def javascript():
        print("Writing JavaScript code")
class Project:
    """This is a high-level module"""
    def __init__(self):
        self.backend = BackendDeveloper()
        self.frontend = FrontendDeveloper()
    def develop(self):
        self.backend.python()
        self.frontend.javascript()
        return "Develop codebase"
project = Project()
print(project.develop())



"""The project class is a high-level module and backend & frontend are the low-level modules. In this example, we found that the high-level module depends on the low-level module. Hence this example are violated the Dependency Inversion Principle. Let’s solve the problem according to the definition of DIP.
Solution:
Example 1
"""
class BackendDeveloper:
   """This is a low-level module"""
   def develop(self):
       self.__python_code()
   @staticmethod
   def __python_code():
       print("Writing Python code")
class FrontendDeveloper:
   """This is a low-level module"""
   def develop(self):
       self.__javascript()
   @staticmethod
   def __javascript():
       print("Writing JavaScript code")
class Developers:
   """An Abstract module"""
   def __init__(self):
       self.backend = BackendDeveloper()
       self.frontend = FrontendDeveloper()
   def develop(self):
       self.backend.develop()
       self.frontend.develop()
class Project:
   """This is a high-level module"""
   def __init__(self):
       self.__developers = Developers()
   def develops(self):
       return self.__developers.develop()
project = Project()
print(project.develops())