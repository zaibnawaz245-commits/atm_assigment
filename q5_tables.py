# Question No 5 - Tables from 1 to n
n = int(input("Enter a number n: "))

for i in range(1, n + 1):
    print(f"\nTable of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")