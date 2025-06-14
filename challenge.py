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

try:
    # Asks for a word or phrase
    palindrome_input = input("Enter a word or phrase: ").strip()

    # Checks if the input is a string
    if not isinstance(palindrome_input, str):
        raise ValueError("The input must be a string!")

    # Removes spaces and punctuation and converts to lowercase
    cleaned_input = ''.join(e for e in palindrome_input if e.isalnum()).lower()

    # Reverses the string
    reversed_input = cleaned_input[::-1]

    # Checks if it's a palindrome
    if reversed_input == cleaned_input:
        print("The input is a palindrome!")
    else:
        print("The input is not a palindrome.")

except ValueError as e:
    # Catches invalid input error and prints a detailed error message
    print(f"Error: {e} Please enter a valid string.")


# Exercise 23: Simple Calculator
# Develop a simple calculator that accepts two numeric inputs and an operator (+, -, *, /) from the user. Use try-except to handle division by zero and non-numeric inputs. Use if-elif-else to perform the mathematical operation based on the given operator. Print the result or an appropriate error message.

try:
    # Prompts the user for two numbers and an operator
    num1 = float(input("Enter the first number: ").strip())
    num2 = float(input("Enter the second number: ").strip())
    operator = input("Enter the operator (+, -, *, /): ").strip()

    # Checks which operation to perform based on the given operator
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        # Checks if dividing by zero
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        result = num1 / num2
    else:
        raise ValueError("Invalid operator! Please use +, -, * or /.")

    # Prints the result of the operation
    print(f"The result of {num1} {operator} {num2} is {result}.")

except ValueError as e:
    # Catches invalid input error and prints a detailed error message
    print(f"Error: {e}. Please enter valid numeric values and a valid operator.")
except ZeroDivisionError as e:
    # Catches division by zero error and prints a detailed error message
    print(f"Error: {e}")


# Exercise 24: Number Classifier
# Write a program that prompts the user to input a number. Use try-except to ensure the input is numeric, and use if-elif-else to classify the number as "positive", "negative", or "zero". Additionally, identify whether the number is "even" or "odd".

# Exercise 24: Number Classifier

try:
    # Prompts the user to input a number
    number = float(input("Enter a number: ").strip())

    # Classifies the number as positive, negative, or zero
    if number > 0:
        classification = "positive"
    elif number < 0:
        classification = "negative"
    else:
        classification = "zero"

    # Checks if the number is even or odd
    if number % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

    # Displays the classification of the number
    print(f"The number {number} is {classification} and {even_or_odd}.")

except ValueError as e:
    # Catches invalid input error and prints a detailed error message
    print(f"Error: {e} Please enter a valid number.")


# Exercise 25: Type Conversion with Validation
# Create a script that asks the user for a list of numbers separated by commas. The program should convert the input string into a list of integers. Use try-except to handle the conversion of each number and validate that each element of the converted list is an integer. If the conversion fails or an element is not an integer, print an error message. If the conversion is successful for all elements, print the list of integers.

try:
    # Prompts the user for a list of numbers separated by commas
    user_input = input("Enter a list of numbers separated by commas: ").strip()

    # Converts the input string into a list
    str_list = user_input.split(',')

    # Converts each element in the list to an integer
    int_list = []
    for item in str_list:
        try:
            int_list.append(int(item.strip()))
        except ValueError:
            raise ValueError(f"'{item.strip()}' is not a valid number.")

    # Prints the list of integers
    print(f"The list of integers is: {int_list}")

except ValueError as e:
    # Catches invalid input error and prints a detailed error message
    print(f"Error: {e} Please enter valid numbers.")