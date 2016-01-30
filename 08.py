# Import libraries
# https://docs.python.org/3/library/time.html
import time
# https://docs.python.org/3/library/math.html 
import math
# Print local time
print (time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))

# Pythagorean theorem
# https://en.wikipedia.org/wiki/Pythagorean_theorem
# calcultes hypotenuse
# input are legs
def calculateHypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

c1 = calculateHypotenuse(1, 2)
print(c1)

# Excercise
# 1. Try to move the import statement after the print function
# 2. Import urllib2 and download content of any website