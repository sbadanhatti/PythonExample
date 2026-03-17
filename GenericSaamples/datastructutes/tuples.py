# Python Tuple Examples with Different Functions
"""
This script demonstrates comprehensive usage of Python tuples and their various methods.
Tuples are immutable, ordered sequences that can contain elements of different data types.
They are more memory-efficient than lists and can be used as dictionary keys.
Tuples are often used for data that shouldn't be modified and for returning multiple values from functions.
"""

# 1. Creating Tuples
"""
Tuples can be created in several ways:
- Using parentheses () (literal syntax)
- Using tuple() constructor
- Using tuple comprehensions (actually generator expressions)
- Single element tuples require a comma
- Empty tuples and tuples from other iterables
"""
print("=== Creating Tuples ===")

# Empty tuple - useful as a placeholder
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Tuple with elements - using parentheses
coordinates = (10, 20, 30)
print(f"Coordinates tuple: {coordinates}")

# Single element tuple - requires comma to distinguish from parentheses
single_element = (42,)
print(f"Single element tuple: {single_element}")

# Tuple without parentheses (tuple packing)
packed_tuple = 1, 2, 3, "hello"
print(f"Packed tuple: {packed_tuple}")

# Using tuple() constructor - converts iterables to tuples
list_to_tuple = tuple([1, 2, 3, 4])
string_to_tuple = tuple("hello")
range_to_tuple = tuple(range(1, 6))
print(f"List to tuple: {list_to_tuple}")
print(f"String to tuple: {string_to_tuple}")
print(f"Range to tuple: {range_to_tuple}")

# Mixed data types - tuples can contain any data types
mixed_tuple = (1, "hello", 3.14, True, [1, 2, 3], {"key": "value"})
print(f"Mixed data types tuple: {mixed_tuple}")

# Tuple from generator expression (not comprehension - tuples don't have comprehensions)
generated_tuple = tuple(x**2 for x in range(1, 6))
print(f"Generated tuple: {generated_tuple}")

print()

# 2. Accessing Elements
"""
Tuple elements can be accessed using:
- Positive indexing (0-based)
- Negative indexing (from the end)
- Slicing [start:end:step] for subtuple
- Tuples support all the same indexing operations as lists
"""
print("=== Accessing Elements ===")

colors = ("red", "green", "blue", "yellow", "purple")

# Indexing - accessing individual elements
print(f"First color: {colors[0]}")      # Index 0 is the first element
print(f"Last color: {colors[-1]}")     # Index -1 is the last element
print(f"Third color: {colors[2]}")     # Index 2 is the third element (0-based)

# Slicing - extracting subtuple
print(f"First three colors: {colors[:3]}")     # From start to index 3 (exclusive)
print(f"Colors from index 1 to 3: {colors[1:4]}")  # From index 1 to 4 (exclusive)
print(f"Every other color: {colors[::2]}")     # Step of 2 (every other element)
print(f"Reversed tuple: {colors[::-1]}")       # Negative step reverses the tuple

# Accessing nested structures within tuples
nested_tuple = (1, 2, (3, 4, 5), [6, 7, 8])
print(f"Nested element: {nested_tuple[2][1]}")  # Access 4 from inner tuple
print(f"List element: {nested_tuple[3][0]}")    # Access 6 from inner list

print()

# 3. Tuple Methods
"""
Tuples have only two built-in methods due to their immutable nature:
- count(): counts occurrences of an element
- index(): finds the index of the first occurrence of an element
Tuples cannot be modified, so they don't have methods like append, remove, etc.
"""
print("=== Tuple Methods ===")

numbers = (1, 2, 3, 2, 4, 2, 5, 2)

# Count - returns the number of times an element appears
count_twos = numbers.count(2)
print(f"Count of 2s: {count_twos}")

# Index - returns the index of the first occurrence of an element
index_of_four = numbers.index(4)
print(f"Index of 4: {index_of_four}")

# Index with start parameter
index_of_two_from_position = numbers.index(2, 2)  # Start searching from index 2
print(f"Index of 2 starting from position 2: {index_of_two_from_position}")

# Index with start and end parameters
index_in_range = numbers.index(2, 1, 5)  # Search between indices 1 and 5
print(f"Index of 2 between positions 1-5: {index_in_range}")

print()

# 4. Built-in Functions with Tuples
"""
Python has several built-in functions that work with tuples:
- len(): returns the number of elements
- max()/min(): returns the largest/smallest element
- sum(): returns the sum of numeric elements
- sorted(): returns a sorted list (tuple itself remains unchanged)
- reversed(): returns a reverse iterator
- any()/all(): check conditions on elements
"""
print("=== Built-in Functions with Tuples ===")

scores = (85, 92, 78, 96, 88)

# Length - number of elements in the tuple
print(f"Number of scores: {len(scores)}")

# Maximum and Minimum - largest and smallest elements
print(f"Highest score: {max(scores)}, Lowest score: {min(scores)}")

# Sum - sum of all numeric elements
print(f"Total score: {sum(scores)}")

# Average calculation
average = sum(scores) / len(scores)
print(f"Average score: {average:.2f}")

# Sorted - returns a sorted list (tuple remains unchanged)
sorted_scores = sorted(scores)
print(f"Original tuple: {scores}")
print(f"Sorted list: {sorted_scores}")

# Reversed - returns an iterator that yields elements in reverse order
reversed_scores = tuple(reversed(scores))  # Convert iterator to tuple
print(f"Reversed tuple: {reversed_scores}")

# Any/All - check conditions
has_passing = any(score >= 60 for score in scores)
all_excellent = all(score >= 90 for score in scores)
print(f"All scores passing (>=60): {has_passing}")
print(f"All scores excellent (>=90): {all_excellent}")

print()

# 5. Tuple Operations
"""
Tuples support various operations:
- Concatenation (+) : combining two tuples
- Repetition (*) : repeating a tuple multiple times
- Membership testing (in/not in) : checking if an element exists
- Comparison operators work element-wise
"""
print("=== Tuple Operations ===")

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation - combining two tuples into a new tuple
combined = tuple1 + tuple2
print(f"Concatenated: {combined}")

# Repetition - repeating the tuple elements multiple times
repeated = tuple1 * 3
print(f"Repeated 3 times: {repeated}")

# Membership testing - checking if an element is in the tuple
print(f"Is 2 in tuple1? {2 in tuple1}")
print(f"Is 7 not in tuple1? {7 not in tuple1}")

# Comparison operations
tuple_a = (1, 2, 3)
tuple_b = (1, 2, 4)
tuple_c = (1, 2, 3)
print(f"tuple_a == tuple_c: {tuple_a == tuple_c}")
print(f"tuple_a < tuple_b: {tuple_a < tuple_b}")  # Lexicographical comparison

print()

# 6. Advanced Tuple Operations
"""
Advanced tuple techniques include:
- Tuple unpacking (multiple assignment)
- Extended unpacking with * operator
- Nested tuple operations
- Tuple as return values from functions
"""
print("=== Advanced Tuple Operations ===")

# Tuple unpacking - assigning tuple elements to multiple variables
person = ("Alice", 30, "Engineer")
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Extended unpacking - using * to capture remaining elements
first, *middle, last = (1, 2, 3, 4, 5)
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Ignoring values with underscore
coordinates = (10, 20, 30)
x, _, z = coordinates  # Ignore y coordinate
print(f"X: {x}, Z: {z}")

# Tuple as function return value
def get_user_info():
    return ("John", 25, "Developer", "New York")

user_name, user_age, user_job, user_city = get_user_info()
print(f"User: {user_name}, {user_age} years old, {user_job} from {user_city}")

# Swapping values using tuple unpacking
a, b = 10, 20
print(f"Before swap: a={a}, b={b}")
a, b = b, a  # Swap using tuple unpacking
print(f"After swap: a={a}, b={b}")

print()

# 7. Common Tuple Patterns
"""
Common programming patterns with tuples:
- Using tuples as immutable records
- Returning multiple values from functions
- Using tuples as dictionary keys
- Grouping related data
- Creating constants or configuration
"""
print("=== Common Tuple Patterns ===")

# Tuple as immutable record
employee = ("John Doe", "Software Engineer", 75000, "john@example.com")
name, title, salary, email = employee
print(f"Employee: {name}, {title}, Salary: ${salary}")

# Multiple return values
def calculate_stats(numbers):
    return len(numbers), sum(numbers), sum(numbers)/len(numbers), min(numbers), max(numbers)

count, total, average, minimum, maximum = calculate_stats([10, 20, 30, 40, 50])
print(f"Stats - Count: {count}, Total: {total}, Avg: {average:.1f}, Min: {minimum}, Max: {maximum}")

# Tuple as dictionary key (lists cannot be used as keys)
location_data = {}
locations = [
    ((40.7128, -74.0060), "New York"),    # Tuple of coordinates as key
    ((34.0522, -118.2437), "Los Angeles"),
    ((41.8781, -87.6298), "Chicago")
]

for coords, city in locations:
    location_data[coords] = city

print(f"Location data: {location_data}")

# Constants using tuples
DAYS_OF_WEEK = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
MONTHS = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

print(f"First day: {DAYS_OF_WEEK[0]}, Last month: {MONTHS[-1]}")

print()

# 8. Named Tuples
"""
Named tuples provide a way to create tuple subclasses with named fields.
They make code more readable and self-documenting compared to regular tuples.
"""
print("=== Named Tuples ===")

from collections import namedtuple

# Define a named tuple class
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instances
point1 = Point(10, 20)
point2 = Point(x=5, y=15)  # Can use keyword arguments
person1 = Person("Alice", 30, "New York")

print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
print(f"Person: {person1}")

# Access by index (like regular tuple)
print(f"Point1 x-coordinate: {point1[0]}, y-coordinate: {point1[1]}")

# Access by name (named tuple feature)
print(f"Point1 x: {point1.x}, y: {point1.y}")
print(f"Person name: {person1.name}, age: {person1.age}")

# Named tuples have useful methods
print(f"Point1 as dict: {point1._asdict()}")
print(f"Fields: {point1._fields}")

# Replace values (returns new named tuple)
point3 = point1._replace(x=100)
print(f"Point1 modified: {point3}")

print()

# 9. Tuple vs List Comparison
"""
Understanding when to use tuples vs lists:
- Use tuples for immutable data that won't change
- Use tuples as dictionary keys
- Use tuples for returning multiple values from functions
- Use lists for data that needs to be modified
- Tuples are more memory efficient than lists
"""
print("=== Tuple vs List Comparison ===")

# Memory efficiency comparison
import sys

large_list = list(range(1000))
large_tuple = tuple(range(1000))

print(f"List size: {sys.getsizeof(large_list)} bytes")
print(f"Tuple size: {sys.getsizeof(large_tuple)} bytes")
print(f"Memory savings with tuple: {sys.getsizeof(large_list) - sys.getsizeof(large_tuple)} bytes")

# Immutability demonstration
mutable_list = [1, 2, 3]
immutable_tuple = (1, 2, 3)

# List can be modified
mutable_list[0] = 999
print(f"Modified list: {mutable_list}")

# Tuple cannot be modified (would raise TypeError)
try:
    immutable_tuple[0] = 999
except TypeError as e:
    print(f"Tuple modification error: {e}")

# Tuple containing mutable objects can have those objects modified
tuple_with_list = (1, 2, [3, 4, 5])
tuple_with_list[2].append(6)  # This works - modifies the list inside the tuple
print(f"Tuple with modified inner list: {tuple_with_list}")

print()

# 10. Tuple Copying and Immutability
"""
Tuples are immutable, but understanding copying behavior is still important:
- Assignment (=) creates a reference to the same tuple
- Tuples containing mutable objects share references to those objects
- To create truly independent copies, use copy.deepcopy()
"""
print("=== Tuple Copying and Immutability ===")

original_tuple = (1, 2, [3, 4])

# Assignment creates reference (but since tuple is immutable, this is usually fine)
reference_tuple = original_tuple
print(f"Same object? {reference_tuple is original_tuple}")

# Tuples containing mutable objects
tuple_with_mutable = (1, 2, [3, 4])

# Modifying the mutable object inside the tuple
tuple_with_mutable[2].append(5)
print(f"After modifying inner list: {tuple_with_mutable}")

# Creating a deep copy for complete independence
import copy
original_with_nested = (1, 2, [3, 4])
deep_copied = copy.deepcopy(original_with_nested)
deep_copied[2].append(5)  # Only affects the deep copy
print(f"Original: {original_with_nested}")
print(f"Deep copy: {deep_copied}")

# Tuple methods for copying (though tuples are already immutable)
copied_tuple = original_tuple[:]  # Slice copy
print(f"Copied tuple: {copied_tuple}")
print(f"Same object? {copied_tuple is original_tuple}")  # False for different objects
