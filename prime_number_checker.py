# "Write a program that asks the user for a number
# check whether that number is prime number or not
# (Prime numbers only divisible by 1 and itself)
# 2 3 5 7 11 13 

number=int(input("Enter a number: "))

if number <=1:
    is_prime=False
else:
    is_prime=True

for i in range(2,number):
    if number % i==0:
        is_prime=False
        break
    
if is_prime:
    print(number," is a prime")
else:
    print(number," is not a prime")
