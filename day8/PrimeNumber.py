# Write your code below this line ๐
import math
def prime_checker(number):
    element = math.ceil(math.sqrt(number))
    for i in range(2, element):
        if number % i == 0:
            print("It's not a prime number.")
            break
    else:
        print("It's a prime number.")

# Write your code above this line ๐

# Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
