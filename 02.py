# Array (list) of colors
colors = ["pink", "blue", "red", "green"]

# Print 2nd item in array
print (colors[1])

# Variable
color = 2
# Print variable value
print (color)
# Print 3rd item in array
print (colors[color])

# Add new item to first position
colors.insert(0, "orange")
# Print 3rd item in array
# https://docs.python.org/3/library/string.html#formatspec
print ("1st color is {0} and 2nd is {1}".format(colors[0], colors[1]))

# Reverse item order in array
colors.reverse()

# Delete third item in array
del colors[2]

# Exercise
# 1. Open documentation https://docs.python.org/2/library/array.html and find how to 
#    add new item to the end of array
# 2. Find how to get count of items in array
