

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / (height ** 2)
print(bmi)

