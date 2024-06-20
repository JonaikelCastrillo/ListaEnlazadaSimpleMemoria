class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
        
    def get_age(self):
        return self.age
    
    def set_age(self, new_age):
        self.age = new_age   
        
    def __str__(self):
        return f"Nombre: {self.name}, Edad: {self.age}"
    
        