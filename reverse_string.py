# Ask the user to enter a word or sentence.
# Your program should print the reverse version of that text. 

text = input("Enter sentence: ")

reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print("reversed:", reversed_text)
