# Python workshop Part 3 by Khiati Zakaria
# Example 17 (Object Oriented Programming)

class Puppy(object):
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def bark(self):
        print("I am "+ self.color +" "+ self.name+".")
         
         
puppy1 = Puppy("Max", "brown")
puppy1.bark()

puppy2 = Puppy("Ruby", "black")
puppy2.bark()
