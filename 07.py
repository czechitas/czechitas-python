def printColor(c):
	# return statement returns value
	return "{0}:x:{1:x}".format(c[0], c[1])

# Array (list) of colors
colors = [["pink", 0xFF1493], ["blue", 0x0000FF], ["red", 0xFF0000], ["green", 0x00FF00]]
	
for color in colors:
	# printColor returns string value
	print printColor(color)
	
# Exercise
# 1. Try to move function to the end of code
# 2. Change function to accept two parameters color and color number