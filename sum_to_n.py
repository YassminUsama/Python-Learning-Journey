# write a program that asks the user to enter a number N
# calulate and print the sum of all number from 1 to N 

num = int(input("Enter number: "))
print("\n--- Running Approach 1 ---")
total = 0
for N in range(num + 1):
    total += N 
print("SUM =", total)    

print("\n--- Running Approach 2 ---")
print("SUM =", (num * (num + 1)) // 2) 
