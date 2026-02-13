#Write a program to display basic exception handling in python.


try:
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    
    result = num1 / num2

except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid integer numbers!")

else:
    
    print("Result is:", result)

finally:
    
    print("Program execution completed.")
