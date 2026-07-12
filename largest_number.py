# Task: Find the largest among three numbers

# 1. User Input Initialization
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

# Approach 1: Nested Conditions (My Solution)
print("\n--- Running Approach 1 (Nested Conditions) ---")
if (num1 > num2):
    if (num1 > num3):
        print(num1, "is largest")
    else:
        print(num3, "is largest")
elif (num2 > num3):
    print(num2, "is largest")
else:
    print(num3, "is largest")
# ------------------------------------------
# Approach 2: Logical Operators (Pythonic Way)

print("\n--- Running Approach 2 (Logical Operators) ---")
if (num1 >= num2) and (num1 >= num3):
    print(num1, "is largest")
elif (num2 >= num1) and (num2 >= num3):
    print(num2, "is largest")
else:
    print(num3, "is largest")
