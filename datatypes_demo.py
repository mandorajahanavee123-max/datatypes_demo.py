# Point 2: Variables and Data Types

# Integer data type
age = 22
print("Age:", age)
print("Data type of age:", type(age))
print("----------------------")

# Float data type
height = 5.6
print("Height:", height)
print("Data type of height:", type(height))
print("----------------------")

# String data type
name = "Jahanavee"
print("Name:", name)
print("Data type of name:", type(name))
print("----------------------")

# Boolean data type
is_intern = True
print("Is Intern:", is_intern)
print("Data type of is_intern:", type(is_intern))
print("----------------------")

# -----------------------------------
# Point 3: Checking Data Types using type()
# -----------------------------------

num = 100
price = 49.99
text = "Python Internship"
status = False

print("Value:", num, "| Type:", type(num))
print("Value:", price, "| Type:", type(price))
print("Value:", text, "| Type:", type(text))
print("Value:", status, "| Type:", type(status))

# -----------------------------------
# Point 4: Arithmetic Operations
# -----------------------------------

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Exponent:", a ** b)

# -----------------------------------
# Point 5: Type Conversion
# -----------------------------------

# Taking input from user
user_input = input("Enter a number: ")

# Converting string input to integer
number_int = int(user_input)

# Converting string input to float
number_float = float(user_input)

print("Original value:", user_input)
print("Type before conversion:", type(user_input))

print("After int conversion:", number_int)
print("Type after int conversion:", type(number_int))

print("After float conversion:", number_float)
print("Type after float conversion:", type(number_float))

# -----------------------------------
# Point 6: Error Handling using try-except
# -----------------------------------

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Division Result:", result)

except ValueError:
    print("Error: Please enter valid numeric values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

else:
    print("Calculation completed successfully.")

finally:
    print("Program execution finished.")

    # -----------------------------------
# Point 7: String Concatenation & Formatting
# -----------------------------------

name = "Jahanavee"
age = 22
height = 5.6

# Method 1: Using comma (automatic spacing)
print("Name:", name, "Age:", age)

# Method 2: Using + operator with str()
print("My name is " + name + " and my age is " + str(age))

# Method 3: Using f-strings (recommended)
print(f"My name is {name}, I am {age} years old and my height is {height} feet.")

# -----------------------------------
# Point 8: Dynamic Typing in Python
# -----------------------------------

value = 10
print("Value:", value, "| Type:", type(value))

value = "Python"
print("Value:", value, "| Type:", type(value))

value = 10.5
print("Value:", value, "| Type:", type(value))

# -----------------------------------
# Point 8: Dynamic Typing in Python
# -----------------------------------

value = 10
print("Value:", value, "| Type:", type(value))

value = "Python"
print("Value:", value, "| Type:", type(value))

value = 10.5
print("Value:", value, "| Type:", type(value))

# -----------------------------------
# Final Summary Output
# -----------------------------------

print("Task 2 completed successfully.")
print("Concepts covered: Variables, Data Types, Type Conversion, Error Handling, and Dynamic Typing.")