# Array (list) of colors
colors = ["pink", "blue", "red", "green"]

# Lets try if code will work
try:
	print (colors[1])
	# Print non-existing item in array
	print (colors[1000])
# If not show error message
except:
	print ("ERROR: item doesn't exists!")

print("I am still running.")
# Exercise
# 1. Try same codou without try and except (delete print error too)
# 2. Divide by 0
