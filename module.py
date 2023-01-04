from math import pi as p

def printName(name):
    print(f"Hello Mr/Ms {name}...we've been waiting for you!")
    

def findArea(width, length):
    area = width * length
    print(f"Your home is {area} square feet.")
    
def findCircumference(r):
    circumference = 2 * p * r
    print(f"The circumference of a circle given radius {r} is equal to {circumference}")
    