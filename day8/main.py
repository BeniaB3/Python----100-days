def greet():
    print("Hello")
    print("Good Morning")
    print("Isn't the weather nice today?")


def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


greet_with(location="London", name="Angela")
