def hi():
    print("Hi there!")

hi()

def printColor(c):
    # return statement returns value
    return f"{c[0]}: 0x{c[1]:06x}"

# Array (list) of colors
colors = [["pink", 0xFF1493],
          ["blue", 0x0000FF],
          ["red", 0xFF0000],
          ["green", 0x00FF00]]

for color in colors:
    # printColor returns a string value
    message = printColor(color)
    print(message)

# Exercise
# 1. Try to move the function to the end of the code
# 2. Change the function to accept two parameters: color and color number
