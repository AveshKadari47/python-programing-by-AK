# Program to enter 10 numbers and display the largest odd number

numbers = []
print("Enter 10 numbers:")


for i in range(10):
    n = int(input(f"Number {i+1}: "))
    numbers.append(n)


odd_numbers = [n for n in numbers if n % 2 != 0]


if odd_numbers:
    largest_odd = max(odd_numbers)
    print("\nThe largest odd number is:", largest_odd)
else:
    print("\nNo odd numbers were entered.")
