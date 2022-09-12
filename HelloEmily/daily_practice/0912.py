# Functions with Inputs
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Bill")

# parameter = name
# argument = "Bill"

# Functions with more than one input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Bill", "Tokyo")

# keyword argument
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with(name="Bill", location="Tokyo")
