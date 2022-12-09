# Import libraries
import time # https://docs.python.org/3/library/time.html
import math # https://docs.python.org/3/library/math.html 

# Print local time
print(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime()))
# https://stackoverflow.com/questions/9525944/python-datetime-formatting-without-zero-padding
#print(time.strftime("%-d.%-m.%Y %H:%M:%S", time.localtime()))  # only on GNU/Linux
# https://stackoverflow.com/a/9526118/2556118
#print(time.localtime())
print("{d.tm_mday}.{d.tm_mon}.{d.tm_year} {d.tm_hour}:{d.tm_min:02}:{d.tm_sec:02}".format(d=time.localtime()))

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
