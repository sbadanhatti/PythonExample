# Python Set Examples with Different Functions
"""
This script demonstrates comprehensive usage of Python sets and their various methods.
Sets are unordered collections of unique, hashable elements. They are highly efficient for membership testing,
removing duplicates, and performing mathematical set operations like union, intersection, and difference.
Sets are mutable by default, but Python also provides immutable frozensets.
"""

# 1. Creating Sets
"""
Sets can be created in several ways:
- Using curly braces {} (literal syntax) - cannot create empty set this way
- Using set() constructor
- Using set comprehensions
- Converting from other iterables (automatically removes duplicates)
- Frozensets for immutable sets
"""
print("=== Creating Sets ===")

# Empty set - must use set() constructor, not {} (which creates empty dict)
empty_set = set()
print(f"Empty set: {empty_set}")

# Set with elements - using curly braces
fruits = {"apple", "banana", "cherry", "apple"}  # Duplicates are automatically removed
print(f"Fruits set: {fruits}")

# Using set() constructor
numbers = set([1, 2, 3, 4, 5, 1, 2])  # Removes duplicates from list
print(f"Numbers set from list: {numbers}")

# Converting string to set (gets unique characters)
string_set = set("hello world")
print(f"Set from string: {string_set}")

# Set comprehension - concise way to create sets with transformations
squares = {x**2 for x in range(1, 6)}
print(f"Squares using comprehension: {squares}")

# Frozenset - immutable set
frozen_fruits = frozenset(["apple", "banana", "cherry"])
print(f"Frozenset: {frozen_fruits}")

# Set from range
range_set = set(range(1, 11, 2))  # Odd numbers from 1 to 9
print(f"Set from range: {range_set}")

print()

# 2. Accessing Elements
"""
Sets are unordered, so they don't support indexing or slicing like lists.
However, you can:
- Check membership with 'in' operator
- Iterate through elements
- Convert to other data types for ordered access
"""
print("=== Accessing Elements ===")

colors = {"red", "green", "blue", "yellow", "purple"}

# Membership testing - very efficient O(1) average time complexity
print(f"Is 'red' in colors? {'red' in colors}")
print(f"Is 'black' not in colors? {'black' not in colors}")

# Iteration - order is arbitrary (implementation-dependent)
print("Iterating through colors:")
for color in colors:
    print(f"  {color}")

# Convert to list for ordered access (sorted)
sorted_colors = sorted(colors)
print(f"Sorted colors: {sorted_colors}")

# Get arbitrary element (useful for processing until set is empty)
if colors:
    arbitrary_color = next(iter(colors))
    print(f"Arbitrary color: {arbitrary_color}")

print()

# 3. Modifying Sets
"""
Sets are mutable, meaning their contents can be changed after creation.
Common modification methods include add, remove, discard, pop, and clear.
Note: Sets only store hashable (immutable) elements.
"""
print("=== Modifying Sets ===")

# Add - adds a single element (if not already present)
colors.add("orange")
print(f"After add 'orange': {colors}")

# Update - adds multiple elements from another iterable
colors.update(["pink", "brown", "orange"])  # 'orange' won't be added again
print(f"After update with list: {colors}")

# Remove - removes a specific element (raises KeyError if not present)
colors.remove("red")
print(f"After remove 'red': {colors}")

# Discard - removes a specific element (no error if not present)
colors.discard("black")  # No error even though 'black' is not in set
print(f"After discard 'black': {colors}")

# Pop - removes and returns an arbitrary element
popped_color = colors.pop()
print(f"Popped color: {popped_color}")
print(f"After pop: {colors}")

# Clear - removes all elements
colors_copy = colors.copy()
colors_copy.clear()
print(f"After clear: {colors_copy}")

print()

# 4. Set Methods
"""
Python sets have several built-in methods for mathematical set operations:
- union(): returns union of sets (elements in either set)
- intersection(): returns intersection (elements in both sets)
- difference(): returns difference (elements in first but not second)
- symmetric_difference(): returns symmetric difference (elements in either but not both)
- issubset()/issuperset(): check subset/superset relationships
- isdisjoint(): check if sets have no common elements
"""
print("=== Set Methods ===")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {1, 2, 3}

# Union - elements in either set
union_result = set_a.union(set_b)
print(f"Union of A and B: {union_result}")

# Intersection - elements in both sets
intersection_result = set_a.intersection(set_b)
print(f"Intersection of A and B: {intersection_result}")

# Difference - elements in A but not in B
difference_result = set_a.difference(set_b)
print(f"Difference A - B: {difference_result}")

# Symmetric difference - elements in either set but not both
symmetric_diff = set_a.symmetric_difference(set_b)
print(f"Symmetric difference: {symmetric_diff}")

# Subset and superset checks
print(f"C is subset of A: {set_c.issubset(set_a)}")
print(f"A is superset of C: {set_a.issuperset(set_c)}")

# Disjoint check - no common elements
disjoint_sets = {1, 2, 3}
other_set = {4, 5, 6}
print(f"Sets are disjoint: {disjoint_sets.isdisjoint(other_set)}")

print()

# 5. Built-in Functions with Sets
"""
Python has several built-in functions that work with sets:
- len(): returns the number of elements
- max()/min(): returns the largest/smallest element
- sorted(): returns a sorted list of elements
- sum(): returns the sum of numeric elements
- any()/all(): check conditions on elements
"""
print("=== Built-in Functions with Sets ===")

numbers = {15, 3, 8, 42, 7, 23}

# Length - number of elements in the set
print(f"Number of elements: {len(numbers)}")

# Maximum and Minimum - largest and smallest elements
print(f"Max: {max(numbers)}, Min: {min(numbers)}")

# Sum - sum of all numeric elements
print(f"Sum: {sum(numbers)}")

# Sorted - returns a sorted list (set itself remains unordered)
sorted_numbers = sorted(numbers)
print(f"Sorted list: {sorted_numbers}")

# Any/All - check conditions
has_even = any(x % 2 == 0 for x in numbers)
all_positive = all(x > 0 for x in numbers)
print(f"Has even numbers: {has_even}")
print(f"All positive: {all_positive}")

print()

# 6. Set Operations
"""
Sets support mathematical operations using operators:
- | : union (elements in either set)
- & : intersection (elements in both sets)
- - : difference (elements in first but not second)
- ^ : symmetric difference (elements in either but not both)
- <= : subset (all elements of first are in second)
- >= : superset (first contains all elements of second)
"""
print("=== Set Operations ===")

set_x = {1, 2, 3, 4}
set_y = {3, 4, 5, 6}

# Union operator
union_op = set_x | set_y
print(f"X | Y (union): {union_op}")

# Intersection operator
intersection_op = set_x & set_y
print(f"X & Y (intersection): {intersection_op}")

# Difference operator
difference_op = set_x - set_y
print(f"X - Y (difference): {difference_op}")

# Symmetric difference operator
symmetric_op = set_x ^ set_y
print(f"X ^ Y (symmetric difference): {symmetric_op}")

# Subset operators
subset_check = {1, 2} <= set_x
superset_check = set_x >= {1, 2}
print(f"{{1, 2}} <= X (subset): {subset_check}")
print(f"X >= {{1, 2}} (superset): {superset_check}")

print()

# 7. Advanced Set Operations
"""
Advanced set techniques include:
- Set comprehensions with conditions
- Multiple set operations
- Set algebra with complex expressions
- Converting between sets and other data types
"""
print("=== Advanced Set Operations ===")

# Set comprehension with condition - filtering while transforming
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares set: {even_squares}")

# Complex set operations
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {5, 6, 7, 8, 9}

# Multiple operations combined
complex_result = (set1 | set2) - (set2 & set3)
print(f"(set1 | set2) - (set2 & set3): {complex_result}")

# Symmetric difference of multiple sets
symmetric_multiple = set1 ^ set2 ^ set3
print(f"set1 ^ set2 ^ set3: {symmetric_multiple}")

# Set of unique characters from multiple strings
text1 = "hello"
text2 = "world"
unique_chars = set(text1) | set(text2)
print(f"Unique characters: {unique_chars}")

print()

# 8. Common Set Patterns
"""
Common programming patterns with sets:
- Removing duplicates from sequences
- Finding unique elements
- Membership testing (very fast)
- Set algebra for data analysis
- Finding differences between collections
"""
print("=== Common Set Patterns ===")

# Remove duplicates from list while preserving order
original_list = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_list = list(dict.fromkeys(original_list))  # Preserves order
unique_set = set(original_list)  # Doesn't preserve order
print(f"Original list: {original_list}")
print(f"Unique (order preserved): {unique_list}")
print(f"Unique set: {unique_set}")

# Find common elements in multiple lists
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
list_c = [5, 6, 7, 8, 9]

common_elements = set(list_a) & set(list_b) & set(list_c)
print(f"Common in all three lists: {common_elements}")

# Find elements unique to each list
unique_to_a = set(list_a) - (set(list_b) | set(list_c))
unique_to_b = set(list_b) - (set(list_a) | set(list_c))
unique_to_c = set(list_c) - (set(list_a) | set(list_b))
print(f"Unique to A: {unique_to_a}")
print(f"Unique to B: {unique_to_b}")
print(f"Unique to C: {unique_to_c}")

# Fast membership testing
large_set = set(range(1, 10001))  # 1 to 10000
test_values = [500, 15000, 7500, 1, 10000]

for value in test_values:
    is_present = value in large_set
    print(f"{value} in large set: {is_present}")

print()

# 9. Set as Data Structure
"""
Sets are excellent for various use cases:
- Removing duplicates
- Fast membership testing
- Mathematical set operations
- Tracking unique items
- Implementing algorithms (like finding unique visitors)
"""
print("=== Set as Data Structure ===")

# Example: Finding unique words in text
text = """
Python is a programming language. Python is versatile.
Programming with Python is fun. Python programming is powerful.
"""

words = text.lower().split()
unique_words = set(words)
print(f"Total words: {len(words)}")
print(f"Unique words: {len(unique_words)}")
print(f"Unique words: {sorted(unique_words)}")

# Example: Finding common interests between people
person1_interests = {"reading", "music", "coding", "gaming"}
person2_interests = {"music", "sports", "coding", "cooking"}
person3_interests = {"reading", "coding", "painting", "music"}

common_interests = person1_interests & person2_interests & person3_interests
all_interests = person1_interests | person2_interests | person3_interests
unique_to_person1 = person1_interests - (person2_interests | person3_interests)

print(f"Common interests: {common_interests}")
print(f"All interests: {all_interests}")
print(f"Unique to person 1: {unique_to_person1}")

print()

# 10. Frozensets and Set Copying
"""
Frozensets are immutable sets that can be used as dictionary keys or set elements.
Understanding set copying is important for avoiding unintended modifications.
"""
print("=== Frozensets and Set Copying ===")

# Frozenset creation and usage
normal_set = {1, 2, 3}
frozen_set = frozenset([1, 2, 3])

# Frozensets can be used as dictionary keys (normal sets cannot)
set_dict = {frozen_set: "frozen", frozenset([4, 5]): "another"}
print(f"Dictionary with frozenset keys: {set_dict}")

# Frozensets can be elements of other sets
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Set of frozensets: {set_of_sets}")

# Set copying
original = {1, 2, 3}

# Assignment creates reference
reference = original
reference.add(4)
print(f"Original after reference modification: {original}")

# Copy creates shallow copy (sufficient for sets since they don't contain mutable objects)
copied = original.copy()
copied.add(5)
print(f"Original after copy modification: {original}")
print(f"Copy after modification: {copied}")

# Frozenset operations
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])

print(f"Frozenset union: {fs1 | fs2}")
print(f"Frozenset intersection: {fs1 & fs2}")
print(f"Frozenset difference: {fs1 - fs2}")
