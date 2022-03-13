import math

def msg():
    return "Hola mundo"


class factorial:
    def __init__(self,n):
        self.n=n
        
    def __call__(self):
        return math.factorial(self.n)
    
    def factorial_menor(self):
        return math.factorial(self.n-1)