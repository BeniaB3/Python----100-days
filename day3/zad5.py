# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

one_string = name1 + name2
lower_string = one_string.lower()

t = lower_string.count("t")
r = lower_string.count("r")
u = lower_string.count("u")
e = lower_string.count("e")

sum = lower_string.count("t") + lower_string.count("r") + lower_string.count("u") + lower_string.count("e")

true = t + r + u + e

print(true)
print(sum)

