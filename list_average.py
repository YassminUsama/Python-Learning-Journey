# "Ask the user to type several numbers separated by spaces (example: 10 20 30).
# Store them in a list and print the average of these numbers."

numbers = input("Enter numbers separated by spaces: ").split()
new_Numbers = []
 
# Fixed the indentation space here
for x in numbers:
    new_Numbers.append(int(x))

total=sum(new_Numbers)
count = len(new_Numbers)
    
avr =(total / count)
print("Average = ", avr)
