# Step 1: Declare two Boolean variables
bool_var1 = True
bool_var2 = False

# Step 2: Demonstrate logical operations (AND, OR, NOT)
logical_and = bool_var1 and bool_var2  # Logical AND
logical_or = bool_var1 or bool_var2    # Logical OR
logical_not1 = not bool_var1           # Logical NOT for the first variable
logical_not2 = not bool_var2           # Logical NOT for the second variable

# Step 3: Use a Boolean variable in a conditional statement
if bool_var1:
    conditional_result = "bool_var1 is True"
else:
    conditional_result = "bool_var1 is False"

# Print results of logical operations
print(f"""
Logical AND of bool_var1 and bool_var2: {logical_and}
Logical OR of bool_var1 and bool_var2: {logical_or}
Logical NOT of bool_var1: {logical_not1}
Logical NOT of bool_var2: {logical_not2}
""")

print(conditional_result) # Print result of the conditional statement
