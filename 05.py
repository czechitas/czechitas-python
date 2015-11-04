# Array (list) of colors
colors = [["pink", 0xFF1493], ["blue", 0x0000FF], ["red", 0xFF0000], ["green", 0x00FF00]]

# 2nd item of 3rd item
print colors[2][1]

# Print all colors in list
for color in colors:
	print color
	
for color in colors:
	# Documentation: https://docs.python.org/3/library/string.html#formatexamples
	print "{0}:x:{1:x}".format(color[0], color[1])

# Exercise
# 1. Create following output, try two ways (special characters, nested loops)
# pink
# x:ff1493
# blue
# x:ff
# red
# x:ff0000
# green
# x:ff00
# 
# 2. Read colors from text file colors.txt