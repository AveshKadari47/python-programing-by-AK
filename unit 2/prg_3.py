#Write a program to generate arithmetic exception and log the exception in system.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2   # May cause ZeroDivisionError
    print("Result is:", result)

except ZeroDivisionError as e:
    print("Arithmetic Exception Occurred!")

    # Logging error manually into a file
    file = open("error_log.txt", "a")
    file.write("ZeroDivisionError: " + str(e) + "\n")
    file.close()

except ValueError as e:
    print("Invalid Input!")

    file = open("error_log.txt", "a")
    file.write("ValueError: " + str(e) + "\n")
    file.close()

finally:
    print("Program execution completed.")

