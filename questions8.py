import random

# Generate a random 4-digit binary number
binary_num = ""
for i in range(4):
    binary_num += str(random.randint(0, 1))

# Convert the binary number to base 10
decimal_num = int(binary_num, 2)

# Print the results
print("Binary number:", binary_num)
print("Decimal equivalent:", decimal_num)
