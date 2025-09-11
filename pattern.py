import math

# Step 1: Take input
num = int(input("Enter a number: "))

# Step 2: Square
print(f"Square of {num} is {num ** 2}")

# Step 3: HCF with 4567
hcf = math.gcd(num, 4567)
print(f"HCF of {num} and 4567 is {hcf}")

# Step 4: Star pattern of last digit
last_digit = num % 10
print(f"\nStar pattern for last digit ({last_digit}):")

for i in range(1, last_digit + 1):
    print("* " * i)

