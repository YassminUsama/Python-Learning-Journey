# Ask user to enter a number.
# Print that number's Multiplication table from 1 to 12.

num = int(input("Enter a number : "))
for i in range(1, 13):
    print(i, "*", num, "=", (i * num))
