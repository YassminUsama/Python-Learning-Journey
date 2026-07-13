# "Write a program that asks the user to enter several numbers separated by spaces.
# Remove all duplicated values and print the list contaning only unique elements 

numbers = input("Enter numbers separated by spaces: ").split()

unique= []

for item in numbers :
    if item not in unique :
        unique.append(item)
    
print("Original list: ",numbers)
print("modify list ",unique)    
