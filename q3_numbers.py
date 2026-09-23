# Question No 3 - 10 Numbers Calculation
numbers = []

# Take 10 numbers from user
for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

# Calculations
total = sum(numbers)
average = total / len(numbers)
largest = max(numbers)
smallest = min(numbers)

# Count even and odd
even_count = 0
odd_count = 0
for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Display results
print(f"\nSum: {total}")
print(f"Average: {average:.2f}")
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")