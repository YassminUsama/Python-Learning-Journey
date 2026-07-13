# Ask the user to enter a password.
# Your program should check if the password is strong based on these rules:
# At least 8 characters long, 1 uppercase, 1 lowercase, 1 number.

password=input("Enter password: ")

has_upper=False
has_lower=False
has_number=False
long_enough=len(password)>=8

for char in password:
     if char.isupper():
        has_upper=True
     if char.islower():
        has_lower=True
     if char.isdigit():
        has_number=True

if  long_enough and has_upper and has_lower and has_number:
    print("Strong password")
else:
     print("Weak password")
     if not long_enough:
        print("At least 8 characters long")
     if not has_upper: 
        print("At least one uppercase letter")
     if not has_lower:
        print("At least one lowercase letter")
     if not has_number:
        print("At least one number")
