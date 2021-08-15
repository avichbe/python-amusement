"""
in this file i'm impelented a simple singelton.
from it's name we can understand that this pattern allow only one instance of the class.
most common use for this pattern is in connection to DB, or when you want to save data after initialized new screen
(like in android)
"""

class DB_Connection:
    instance = None

    def __init__(self):
        raise RuntimeError("call instance instead")

    def instance(self, cls):
        if not cls.instance:
            print("creating new instance")
            cls.instance = cls.__new__(cls)
        return cls.instance
