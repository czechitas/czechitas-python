# My name
name = "Stepan"

# Print Hi message
if name == "Stepan":
    print("Hi Stepan!")
elif name == "Eva":
    print("Hi Eva!")
else:
    print("Hi friend!")

# Array (list) of colors
colors = [["pink", 0xFF1493],
          ["blue", 0x0000FF],
          ["red", 0xFF0000],
          ["green", 0x00FF00]]

# My favorite color
favorite = "blue"

# Print only favorite color number
for color in colors:
    # Check if color is my favorite one
    if color[0] == favorite:
        print ("I like 0x{0:06X}".format(color[1]))

# Exercise
# 1. If the color is not your favorite print a message like this (if-else statement):
# Don't like pink color
# I like x:ff
# Don't like red color
# Don't like green color
