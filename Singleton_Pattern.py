# In software engineering, the singleton pattern is a design pattern that restricts the instantiation of a class to one object. This is useful when exactly one object is needed to coordinate actions across the system.

# Create a Singleton class, so that there is always a unique instance of Singleton in the session.

# Example:

# a, b = Singleton(), Singleton()
# isinstance(a, Singleton) # true
# a is b # true
# a.x = 5
# b.x # 5

class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance