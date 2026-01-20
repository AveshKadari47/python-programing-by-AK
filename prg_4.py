# Program to enter 10 numbers and display Armstrong numbers

def is_armstrong(num):
    
    digits = str(num)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == num


numbers = []
print("Enter 10 numbers:")
for i in range(10):
    n = int(input(f"Number {i+1}: "))
    numbers.append(n)


armstrong_numbers = [n for n in numbers if is_armstrong(n)]


print("\nArmstrong numbers from the entered list are:")
if armstrong_numbers:
    print(*armstrong_numbers)
else:
    print("None found")
