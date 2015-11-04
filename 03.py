# Array (list) of colors
colors = ["pink", "blue", "red", "green"]

# Lets try if code will work
try:
	# Print non-existing item in array
	print colors[1000]
# If not show error message
except:
	print "ERROR: item doesn't exists!"
	
# Exercise
# 1. Divide by 0