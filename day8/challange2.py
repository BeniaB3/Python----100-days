# Write your code below this line 👇
import math
def prime_checker(number):
    #zrob pierwiastek z liczby i zaokraglij w gore
    element = math.ceil(math.sqrt(number))
    for i in range(2, element):
        if number % i == 0:
            print("It's not a prime number.")
            break
    else:
        print("It's a prime number.")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
