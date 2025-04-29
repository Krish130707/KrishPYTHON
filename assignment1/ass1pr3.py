conversions = ["inches", "yards", "miles", "millimeters", "centimeters", "meters", "kilometers"]
factors = [12, 1/3, 1/5280, 304.8, 30.48, 0.3048, 0.0003048]

feet = float(input("Enter a length in feet: "))
print("Choose a conversion:")
for i, unit in enumerate(conversions, start=1):
    print(f"{i}. {unit}")

choice = int(input("Enter your choice (1-7): "))
if 1 <= choice <= len(conversions):
    result = feet * factors[choice - 1]
    print(f"{feet} feet is {result} {conversions[choice - 1]}")
else:
    print("Invalid choice.")
