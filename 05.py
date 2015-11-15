# Array (list) of colors
# It works like table - rows and columns
colors = [["pink", 0xFF1493], 
          ["blue", 0x0000FF], 
		  ["red", 0xFF0000], 
		  ["green", 0x00FF00]]

# first index is rows
# second index is column
print (colors[2][1])

# Print all colors in list
# {1:X} prints number in hexadecimal format
for color in colors:
	print ("Color {0} is in decimal {1} and hexadecimal 0x{1:06X}.".format(color[0], color[1]))

# Exercise
# 1. Create following output, try two ways (special characters, nested loops)
# pink
# 	x:ff1493
# blue
# 	x:ff
# red
# 	x:ff0000
# green
# 	x:ff00
# 
# 2. Read colors from text file colors.txt
