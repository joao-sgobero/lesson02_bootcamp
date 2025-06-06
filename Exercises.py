# Exercises
# Integers (int)

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

