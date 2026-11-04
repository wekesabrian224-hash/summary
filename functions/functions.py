# Define with def. Parameters go in (), and return sends a result back.
def greet(name):
    return f"Hello, {name}!"

message = greet("Lucky")
print(message)                 # Hello, Lucky!

# Multiple parameters
def add(a, b):
    return a + b

print(add(3, 4))               # 7

# Default parameter: used when the caller doesn't provide one
def greet_with_title(name, title="Student"):
    return f"Hello, {title} {name}!"

print(greet_with_title("Lucky"))             # Hello, Student Lucky!
print(greet_with_title("Lucky", "Dr."))      # Hello, Dr. Lucky!

# Keyword arguments: name the parameter when calling
print(greet_with_title(title="Eng.", name="Lucky"))

# Returning more than one value (Python packs them into a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 9, 1, 7])
print(low, high)               # 1 9

# print vs return
def show_double(n):
    print(n * 2)               # displays it, but the result is lost

def get_double(n):
    return n * 2               # hands the value back so you can use it

result = get_double(5) + 1
print(result)                  # 11

# A function with no return gives back None
x = show_double(5)             # prints 10
print(x)                       # None

# Docstring: a description of what the function does
def area(width, height):
    """Return the area of a rectangle."""
    return width * height

print(area(3, 5))              # 15