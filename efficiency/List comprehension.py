degrees = [12, 21, 15, 32]
to_fahrenheit = [num*(9/5) + 32 for num in degrees]
print(to_fahrenheit)

print("\n")

num = int(input("Enter an integer up to 100 (inclusive): "))
divisible = [i for i in range(1, 101) if i % num == 0]
print(divisible)
