# Exercises

# --- Integers (int) ---

# 1) Write a program that adds two integers entered by the user.
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
sum_n1_n2 = n1 + n2

print(f"The sum of {n1} + {n2} is {sum_n1_n2}")


# 2) Create a program that receives a number from the user and calculates the remainder of this number divided by 5.
num_user = int(input("Enter a number: "))
remainder_division = num_user % 5

print(f"The remainder of the division of {num_user} by 5 is {remainder_division}")


# 3) Develop a program that multiplies two numbers provided by the user and displays the result.
mult_1 = int(input("Enter the first number: "))
mult_2 = int(input("Enter the second number: "))
multiplication = mult_1 * mult_2

print(f"The multiplication of {mult_1} and {mult_2} is {multiplication}")


# 4) Write a program that asks for two integers and prints the integer division of the first by the second.
div_1 = int(input("Enter the first number: "))
div_2 = int(input("Enter the second number: "))
division = div_1 // div_2

print(f"The division of {div_1} and {div_2} is {division}")


# 5) Write a program that calculates the square of a number provided by the user.
quad_1 = int(input("Enter a number: "))
square = quad_1 ** 2

print(f"The square of the number {quad_1} is {square}")

# --- Integers (int) ---

# 6) Write a program that receives two floating-point numbers and performs their addition.
float_num1 = float(input("Enter the first floating-point number: "))
float_num2 = float(input("Enter the second floating-point number: "))

float_sum = float_num1 + float_num2

print(f"The sum of {float_num1} + {float_num2} is {float_sum}")

# 7) Create a program that calculates the average of two floating-point numbers provided by the user.
float_num1 = float(input("Enter the first floating-point number: "))
float_num2 = float(input("Enter the second floating-point number: "))

float_avg = (float_num1 + float_num2) / 2

print(f"The average of the numbers {float_num1} and {float_num2} is {float_avg}")

# 8) Develop a program that calculates the power of a number (base and exponent provided by the user).
base_float = float(input("Enter the base: "))
expoente_float = float(input("Enter the exponent: "))

float_power = base_float ** expoente_float

print(f"The result of {base_float} raised to the power of {expoente_float} is {float_power}")

# 9) Write a program that converts the temperature from Celsius to Fahrenheit.
celsius_float = float(input("Enter the temperature in Celsius: "))

fahrenheit_float = (celsius_float * 9/5) + 32

print(f"The temperature of {celsius_float}°C is equivalent to {fahrenheit_float}°F")

# 10) Write a program that calculates the area of a circle, receiving the radius as input.
import math

radius_float = float(input("Enter the radius of the circle: "))

circle_area = math.pi * (radius_float ** 2)

print(f"The area of the circle with radius {radius_float} is {circle_area:.2f}")

# --- Strings (str) ---

# 11) Convert a string to uppercase
user_input = input("Enter a phrase: ")
print(user_input.upper())

# 12) Program that converts the full name to lowercase
full_name = input("Enter your full name: ")
print(full_name.lower())

# 13) Program that removes leading and trailing spaces from a string
sentence = input("Enter a sentence: ")
print(sentence.strip())

# 14) Program that splits a date into day, month, and year
date_input = input("Enter a date in the format dd/mm/yyyy: ")
day, month, year = date_input.split('/')
print(f'Day: {day}, Month: {month}, Year: {year}')

# 15) Program that concatenates two strings
string_one = input("Enter the first string: ")
string_two = input("Enter the second string: ")
print(string_one + string_two)