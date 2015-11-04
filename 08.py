# Import time library
# https://docs.python.org/2/library/time.html
import time

# Print local time
print time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())


# Excercise
# 1. Try to move import statement after print function
# 2. Import urllib2 and download content of any website