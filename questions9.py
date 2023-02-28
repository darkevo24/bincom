# Initialize the first two Fibonacci numbers
fibonacci = [0, 1]

# Calculate the next 48 Fibonacci numbers and add them to the list
for i in range(48):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# Sum the first 50 Fibonacci numbers
fibonacci_sum = sum(fibonacci)

# Print the result
print("Sum of the first 50 Fibonacci numbers:", fibonacci_sum)
