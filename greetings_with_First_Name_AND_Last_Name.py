# Create a Person class with a greet method that returns the first and last name of the person with a greeting.

# For example, if the first name is "Bob" and the last name is "Smith" then it should return "Hello, Bob Smith!".

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def greet(self):
        return f"Hello, {self.first_name} {self.last_name}!"