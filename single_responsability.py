# the single_responsability.py file is a module
# the module is a file that contains python code

"""
    Single Responsibility Principle(SRP):
    A class should have only one responsibility and only one reason to change. That means a class does not perform multiple jobs.
"""


"""
    Example:
        Violation of SRP
"""

class Account:
    """Demo bank account class
    """
    def __init__(self, account_no:str):
        self.account_no = account_no

    def get_account_no(self):
        """Get account number
        """
        return self.account_no

    def save(self):
        """Save account to database
        """
        pass


"""
How does it violate the SRP?
In the account class, I am performing two tasks. One is stored data and another one gets account number. So it violates the SRP.

Solution: A common solution to this problem is to apply the facade pattern. Let`s create another class and this class will handle database management job and the account class will only handle his properties.
"""

class AccountDB:
    """Account DB management class
    """
    def get_account_number(self, _id:int):
        """Get account number
        """
        pass

    def account_save(self, obj):
        """Save account to database
        """
        pass


class Account:
    """Demo bank account class
    """

    def __init__(self, account_no:str):
        self.account_no = account_no
        self._db = AccountDB()

    def get_account_number(self):
        """Get account number
        """
        return self.account_no

    def get(self, _id:int):
        """:param _id: Account id
           :return: Account object
        """
        return self._db.get_account_number(_id=_id)

    def save(self):
        """Save account to database
        """
        self._db.account_save(obj=self)