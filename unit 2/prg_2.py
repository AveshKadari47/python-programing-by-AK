#Write a program to execute user defined exception in python.

class InvalidMarksError(Exception):
    pass   # No constructor used

try:
    marks = int(input("Enter your marks (0-100): "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks should be between 0 and 100!")

    print("Marks entered:", marks)

except InvalidMarksError as e:
    print("User Defined Exception:", e)

except ValueError:
    print("Invalid input! Please enter a number.")

finally:
    print("Program execution completed.")
