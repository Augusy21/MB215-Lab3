import math

# Part 1: For loop with range to print even numbers
print("Even numbers:")
for num in range(2, 21, 2):  # Starts at 2, goes up to 20, increments by 2
    print(num, end=' ')
print("\n")  # Newline for separation

# Part 2: Nested for loop to create a multiplication table for numbers 1 to 3
print("Multiplication table for numbers 1 to 3:")
for i in range(1, 4):  # Outer loop for numbers 1 to 3
    for j in range(1, 11):  # Inner loop for range 1 to 10
        print(f"{i} * {j} = {i*j}", end='\t')
    print()  # Newline after each inner loop
print("\n")  # Newline for separation 
    

# Part 3: For loop to reverse the characters of a given string and print them
given_string = "Hello"
reversed_string = ""
for char in given_string:
    reversed_string = char + reversed_string  # Prepend current character
print(f"Reversing the string '{given_string}': {reversed_string}")
print("\n")  # Newline for separation
