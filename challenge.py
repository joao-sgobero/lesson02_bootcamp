# Exercise 21: Temperature Converter
# Write a program that converts the temperature from Celsius to Fahrenheit. The program should prompt the user for the temperature in Celsius and, using try-except, ensure the input is numeric, handling any ValueError. Print the result in Fahrenheit or an error message if the input is invalid.

try:
    # Asks for the temperature in Celsius and converts it directly to float
    celsius_input = float(input("Enter the temperature in Celsius (e.g., 25.5): ").strip())
    
    # Converts to Fahrenheit
    fahrenheit = (celsius_input * 9/5) + 32
    print(f"The temperature in Fahrenheit is {fahrenheit}°F")

except ValueError as e:
    # Catches invalid input error and prints a detailed error message
    print(f"Invalid input! {e} Please enter a valid numeric value for the temperature.")



# Exercise 22: Palindrome Checker
# Create a program that checks if a word or phrase is a palindrome (reads the same forwards and backwards, ignoring spaces and punctuation). Use try-except to ensure the input is a string. Tip: Use the isinstance() function to verify the type of the input.

# Exercise 23: Simple Calculator
# Develop a simple calculator that accepts two numeric inputs and an operator (+, -, *, /) from the user. Use try-except to handle division by zero and non-numeric inputs. Use if-elif-else to perform the mathematical operation based on the given operator. Print the result or an appropriate error message.

# Exercise 24: Number Classifier
# Write a program that prompts the user to input a number. Use try-except to ensure the input is numeric, and use if-elif-else to classify the number as "positive", "negative", or "zero". Additionally, identify whether the number is "even" or "odd".

# Exercise 25: Type Conversion with Validation
# Create a script that asks the user for a list of numbers separated by commas. The program should convert the input string into a list of integers. Use try-except to handle the conversion of each number and validate that each element of the converted list is an integer. If the conversion fails or an element is not an integer, print an error message. If the conversion is successful for all elements, print the list of integers.