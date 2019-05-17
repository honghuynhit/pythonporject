# Call module math
import mymath
import Animal as animal

# call function add from math.py
print(mymath.add(12,10))
number1 = 100
number2 = 200

print('Tong hai so la: ', mymath.add(number1,number2))

#Call animal class
animall = animal.animal()
animall.show()
animall.run()
animall.go()

# call dog class
dogAnimal = animal.dog('Lucy',4)
dogAnimal.show()
dogAnimal.run()
dogAnimal.go()