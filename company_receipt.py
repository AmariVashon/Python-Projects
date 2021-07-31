p1_name, p1_price = "Books", 49.95
p2_name, p2_price = "Computer", 579.99
p3_name, p3_price = "Monitor", 124.89

company_name = "coding temple, inc."
company_address = "283 Franklin St."
company_city = "Boston, MA"

message = "Thanks for shopping with us today!"

print("*" * 50)

print(f"\t\t{company_name.title()}")
print(f"\t\t{company_address}")
print(f"\t\t{company_city}")

print("=" * 50)

print("\tProduct Name\tProduct Price")

print(f"\t{p1_name}\t\t${p1_price}")
print(f"\t{p2_name}\t${p2_price}")
print(f"\t{p3_name}\t\t${p3_price}")

print("=" * 50)

total = p1_price + p2_price + p3_price

print(f"\t\t\tTotal\n\t\t\t${total}")

print("=" * 50)

print(f"\n\t{message}\n")

print("*" * 50)