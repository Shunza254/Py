# squares = []
# for x in range(5):
#     squares.append(x**2)
# print(squares)

# # List comprehension
# squares = [x**2 for x in range(5)]
# print(squares)

# # Create a 4x4 matrix using nested list comprehensions
# matrix = [[i * j for i in range(1, 5)] for j in range(1, 4)]
# print(matrix)

# names = ["chilla", "brenda", "elsy"]
# uppercase_names = [name.upper() for name in names]
# print(uppercase_names)

# # Filtering data
# numbers = [12, 15, 10, 20, 22, 30]
# divisible_by_5 = [num for num in numbers if num % 5 == 0]
# print(divisible_by_5)

# # Advantages of List Comprehensions
# # Conciseness: More compact than traditional loops.
# # Readability: Easier to understand when used appropriately.
# # Performance: Faster than loops in many cases due to optimization.

# Functions
def greet(name):
    """Greet a person by their name."""
    return f"Hello, {name}!"

print(greet("Evans"))

def square(num):
    return num ** 2

results = square(5)
print(results)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))

# Create a function named large_power() that takes two parameters named base and exponent.
# If base raised to the exponent is greater than 5000, return True, otherwise return False

def large_power(base, exponent):
    if (base ** exponent) > 5000:
        return True
    return False

print(large_power(4, 10))