# Python Dictionary Examples with Different Functions
"""
This script demonstrates comprehensive usage of Python dictionaries and their various methods.
Dictionaries are mutable, unordered collections of key-value pairs. They are also known as associative arrays or hash maps.
Keys must be immutable (strings, numbers, tuples), while values can be any data type.
Dictionaries are highly efficient for lookups, insertions, and deletions (average O(1) time complexity).
"""

# 1. Creating Dictionaries
"""
Dictionaries can be created in several ways:
- Using curly braces {} (literal syntax)
- Using dict() constructor
- Using dictionary comprehensions
- From sequences using dict() with zip
- From keyword arguments
"""
print("=== Creating Dictionaries ===")

# Empty dictionary - useful as a starting point for dynamic dictionary building
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# Dictionary with key-value pairs - basic way to create a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Person dictionary: {person}")

# Using dict() constructor with keyword arguments
person2 = dict(name="Bob", age=25, city="London")
print(f"Person2 using dict(): {person2}")

# Using dict() constructor with list of tuples
person3 = dict([("name", "Charlie"), ("age", 35), ("city", "Paris")])
print(f"Person3 using dict() with tuples: {person3}")

# Mixed data types - values can be any type, keys must be immutable
mixed_dict = {
    "string": "hello",
    "number": 42,
    "list": [1, 2, 3],
    "boolean": True,
    42: "number as key",  # Numbers can be keys
    (1, 2): "tuple as key"  # Tuples can be keys (immutable)
}
print(f"Mixed data types dictionary: {mixed_dict}")

# Dictionary comprehension - concise way to create dictionaries
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares using comprehension: {squares}")

# From two sequences using zip
keys = ["a", "b", "c"]
values = [1, 2, 3]
zipped_dict = dict(zip(keys, values))
print(f"Dictionary from zip: {zipped_dict}")

print()

# 2. Accessing Elements
"""
Dictionary elements can be accessed using:
- Square bracket notation dict[key]
- get() method (safer, returns None if key doesn't exist)
- Keys must be exact matches (case-sensitive)
"""
print("=== Accessing Elements ===")

student = {
    "name": "John Doe",
    "age": 20,
    "grades": {"math": 85, "english": 92, "science": 78},
    "courses": ["Python", "Data Science", "Machine Learning"]
}

# Direct access using square brackets - raises KeyError if key doesn't exist
print(f"Student name: {student['name']}")
print(f"Student age: {student['age']}")

# Using get() method - safer, returns None (or specified default) if key doesn't exist
print(f"Student GPA (using get): {student.get('gpa', 'Not available')}")
print(f"Student major (using get): {student.get('major', 'Undeclared')}")

# Accessing nested dictionary
print(f"Math grade: {student['grades']['math']}")

# Accessing list within dictionary
print(f"First course: {student['courses'][0]}")

print()

# 3. Modifying Dictionaries
"""
Dictionaries are mutable, meaning their contents can be changed after creation.
Common modification operations include adding, updating, and removing key-value pairs.
"""
print("=== Modifying Dictionaries ===")

# Adding new key-value pairs
student["major"] = "Computer Science"
print(f"After adding major: {student}")

# Updating existing values
student["age"] = 21
print(f"After updating age: {student}")

# Using update() method to merge dictionaries
additional_info = {"gpa": 3.8, "graduation_year": 2025}
student.update(additional_info)
print(f"After update with additional info: {student}")

# Modifying nested structures
student["grades"]["history"] = 88
student["courses"].append("Web Development")
print(f"After modifying nested structures: {student}")

print()

# 4. Dictionary Methods
"""
Python dictionaries have several built-in methods for common operations:
- keys(): returns view of all keys
- values(): returns view of all values
- items(): returns view of key-value pairs
- pop(): removes and returns value for a key
- popitem(): removes and returns last inserted key-value pair
- clear(): removes all items
- copy(): creates a shallow copy
"""
print("=== Dictionary Methods ===")

scores = {"Alice": 95, "Bob": 87, "Charlie": 92, "Diana": 88}

# Get all keys
print(f"Keys: {list(scores.keys())}")

# Get all values
print(f"Values: {list(scores.values())}")

# Get all key-value pairs
print(f"Items: {list(scores.items())}")

# Pop a specific key-value pair
bob_score = scores.pop("Bob")
print(f"Popped Bob's score: {bob_score}")
print(f"Dictionary after pop: {scores}")

# Pop the last inserted item (Python 3.7+ maintains insertion order)
last_item = scores.popitem()
print(f"Popped last item: {last_item}")
print(f"Dictionary after popitem: {scores}")

# Clear all items
scores_copy = scores.copy()
scores_copy.clear()
print(f"After clear: {scores_copy}")

print()

# 5. Built-in Functions with Dictionaries
"""
Python has several built-in functions that work with dictionaries:
- len(): returns the number of key-value pairs
- in/not in: checks if a key exists
- sorted(): returns sorted keys (for ordered dictionaries)
- max()/min(): works with keys
"""
print("=== Built-in Functions with Dictionaries ===")

grades = {"math": 85, "english": 92, "science": 78, "history": 88}

# Length - number of key-value pairs
print(f"Number of subjects: {len(grades)}")

# Membership testing - check if key exists
print(f"Is 'math' in grades? {'math' in grades}")
print(f"Is 'art' not in grades? {'art' not in grades}")

# Get all keys and sort them
sorted_subjects = sorted(grades.keys())
print(f"Sorted subjects: {sorted_subjects}")

# Find subject with highest/lowest grade
best_subject = max(grades, key=grades.get)
worst_subject = min(grades, key=grades.get)
print(f"Best subject: {best_subject} ({grades[best_subject]})")
print(f"Worst subject: {worst_subject} ({grades[worst_subject]})")

print()

# 6. Dictionary Operations
"""
Dictionaries support various operations:
- Equality comparison (==) : compares key-value pairs
- Iteration: can loop through keys, values, or items
- Dictionary unpacking (**) : merge dictionaries
"""
print("=== Dictionary Operations ===")

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"a": 1, "b": 2}

# Equality comparison
print(f"dict1 == dict3: {dict1 == dict3}")
print(f"dict1 == dict2: {dict1 == dict2}")

# Iteration over keys (default)
print("Iterating over keys:")
for key in dict1:
    print(f"  {key}: {dict1[key]}")

# Iteration over values
print("Iterating over values:")
for value in dict1.values():
    print(f"  {value}")

# Iteration over items
print("Iterating over items:")
for key, value in dict1.items():
    print(f"  {key} -> {value}")

# Dictionary unpacking (merge)
merged = {**dict1, **dict2}
print(f"Merged dictionary: {merged}")

print()

# 7. Advanced Dictionary Operations
"""
Advanced dictionary techniques include:
- Dictionary comprehensions with conditions
- Nested dictionary comprehensions
- Default dictionaries
- Ordered dictionaries
"""
print("=== Advanced Dictionary Operations ===")

# Dictionary comprehension with condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares dict: {even_squares}")

# Transform existing dictionary
uppercase_names = {k.upper(): v for k, v in {"alice": 25, "bob": 30, "charlie": 35}.items()}
print(f"Uppercase names: {uppercase_names}")

# Nested dictionary comprehension
matrix_dict = {f"row_{i}": {f"col_{j}": i*j for j in range(1, 4)} for i in range(1, 4)}
print(f"Matrix dictionary: {matrix_dict}")

# Using setdefault for conditional assignment
fruit_counts = {}
fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]

for fruit in fruits:
    fruit_counts.setdefault(fruit, 0)
    fruit_counts[fruit] += 1

print(f"Fruit counts using setdefault: {fruit_counts}")

print()

# 8. Common Dictionary Patterns
"""
Common programming patterns with dictionaries:
- Counting frequencies
- Grouping data
- Creating lookup tables
- Memoization/caching
- Configuration storage
"""
print("=== Common Dictionary Patterns ===")

# Frequency counting
text = "hello world hello python world"
word_counts = {}
for word in text.split():
    word_counts[word] = word_counts.get(word, 0) + 1
print(f"Word frequencies: {word_counts}")

# Grouping data
students = [
    {"name": "Alice", "grade": "A", "age": 20},
    {"name": "Bob", "grade": "B", "age": 21},
    {"name": "Charlie", "grade": "A", "age": 19},
    {"name": "Diana", "grade": "A", "age": 22}
]

# Group by grade
grouped_by_grade = {}
for student in students:
    grade = student["grade"]
    if grade not in grouped_by_grade:
        grouped_by_grade[grade] = []
    grouped_by_grade[grade].append(student["name"])

print(f"Students grouped by grade: {grouped_by_grade}")

# Lookup table
grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
student_grades = ["A", "B", "A", "C"]
gpa = sum(grade_points[grade] for grade in student_grades) / len(student_grades)
print(f"GPA calculation: {gpa:.2f}")

print()

# 9. Dictionary as Data Structure
"""
Dictionaries are excellent for representing structured data:
- JSON-like data structures
- Configuration objects
- Caches and memoization
- Sparse arrays/matrices
"""
print("=== Dictionary as Data Structure ===")

# JSON-like structure
user_profile = {
    "personal": {
        "name": "John Doe",
        "age": 30,
        "email": "john@example.com"
    },
    "preferences": {
        "theme": "dark",
        "notifications": True,
        "language": "en"
    },
    "activity": {
        "last_login": "2024-01-15",
        "posts_count": 42,
        "friends_count": 128
    }
}

print(f"User profile structure: {user_profile}")
print(f"User's preferred theme: {user_profile['preferences']['theme']}")

# Simple cache/memoization
def fibonacci_memo(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fibonacci_memo(n-1, cache) + fibonacci_memo(n-2, cache)
    return cache[n]

print(f"Fibonacci(10) with memoization: {fibonacci_memo(10)}")

print()

# 10. Dictionary Copying and Comparison
"""
Understanding dictionary copying is important:
- Assignment (=) creates a reference, not a copy
- copy(): creates a shallow copy
- deepcopy(): creates completely independent copies
- Comparison operators work with dictionaries
"""
print("=== Dictionary Copying and Comparison ===")

original = {"a": 1, "b": [2, 3], "c": {"nested": 4}}

# Assignment creates reference
reference = original
reference["a"] = 999
print(f"Original after reference modification: {original}")

# Shallow copy
import copy
original2 = {"a": 1, "b": [2, 3], "c": {"nested": 4}}
shallow = original2.copy()
shallow["b"].append(4)  # Modifies nested list in both
shallow["c"]["nested"] = 5  # Modifies nested dict in both
print(f"Original after shallow copy modification: {original2}")
print(f"Shallow copy: {shallow}")

# Deep copy
original3 = {"a": 1, "b": [2, 3], "c": {"nested": 4}}
deep = copy.deepcopy(original3)
deep["b"].append(4)  # Only modifies deep copy
deep["c"]["nested"] = 5  # Only modifies deep copy
print(f"Original after deep copy modification: {original3}")
print(f"Deep copy: {deep}")

# Dictionary comparison
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 2, "x": 1}  # Same content, different order
dict_c = {"x": 1, "y": 3}

print(f"dict_a == dict_b (same content): {dict_a == dict_b}")
print(f"dict_a == dict_c (different content): {dict_a == dict_c}")
