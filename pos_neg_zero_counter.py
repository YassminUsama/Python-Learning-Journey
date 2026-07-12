# "Write a program that asks the user to enter several numbers separated by spaces.
# Your task is to count how many numbers are:
# Positive-Negative-Zero
# Then print the 3 results.

numbers = input("Enter numbers separated by spaces: ").split()
new_Numbers = []
 
# Fixed the indentation space here
for x in numbers:
    new_Numbers.append(int(x))

pos=0
neg=0
zero=0
for i in new_Numbers:
    if i>0:
        pos+=1
    elif i<0:
        neg+=1
    else:
        zero+=1

print("+ : ", pos)
print("- : ", neg)
print("0 : ", zero)
