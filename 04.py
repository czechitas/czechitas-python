# Array (list) of colors
colors = ["pink", "blue", "red", "green", "gray"]

# Print all colors in list
for index, color in enumerate(colors):
    if index == 1:
        print("    ", color)
    else:
        print(color)
    print("-----")

print("I am not in loop anymore.")

# Exercise
# 1. Add item to array
# 2. Print reversed array
# 3. Try to change the indent for the 2nd print in loop