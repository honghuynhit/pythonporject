class animal():
    name = ''
    age = 0
    def __init__(self, name = '', age = 0):
        self.name = name
        self.age = age
        
    def show(self):
        if(self.age <= 0 ):
            self.age = ''
        print('My name is', self.name,'. Age: ' if self.age != '' else '', self.age)
    def run(self):
        print('Animal is running...')
    def go(self):
        print('Animal is going...')
class dog(animal):
    def run(self):
        print(self.name,' is running...')

class cat(animal):
    def go(self):
        print(self.name,'is going....')
    def roam(self):
        print(self.name, ' is roam...')