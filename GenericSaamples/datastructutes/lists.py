# Python List Examples with Different Functions
"""
This script demonstrates comprehensive usage of Python lists and their various methods.
Lists are mutable, ordered sequences that can contain elements of different data types.
They are one of the most fundamental and versatile data structures in Python.
"""

# 1. Creating Lists
"""
Lists can be created in several ways:
- Using square brackets [] (literal syntax)
- Using the list() constructor
- Using list comprehensions for more complex initialization
- Lists can contain mixed data types (heterogeneous)
"""
print("=== Creating Lists ===")

# Empty list - useful as a starting point for dynamic list building
empty_list = []
print(f"Empty list: {empty_list}")

# List with elements - basic way to create a list with initial values
numbers = [1, 2, 3, 4, 5]
print(f"Numbers list: {numbers}")

# Mixed data types - Python lists can store different types of data
mixed_list = [1, "hello", 3.14, True]
print(f"Mixed list: {mixed_list}")

# Using list() constructor - converts iterables (like strings) to lists
string_to_list = list("hello")
print(f"String to list: {string_to_list}")

# List comprehension - concise way to create lists with transformations
# Syntax: [expression for item in iterable if condition]
squares = [x**2 for x in range(1, 6)]
print(f"Squares using comprehension: {squares}")

print()

# 2. Accessing Elements
"""
List elements can be accessed using:
- Positive indexing (0-based)
- Negative indexing (from the end)
- Slicing [start:end:step] for sublists
"""
print("=== Accessing Elements ===")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Indexing - accessing individual elements
print(f"First fruit: {fruits[0]}")      # Index 0 is the first element
print(f"Last fruit: {fruits[-1]}")     # Index -1 is the last element
print(f"Third fruit: {fruits[2]}")     # Index 2 is the third element (0-based)

# Slicing - extracting sublists
print(f"First three fruits: {fruits[:3]}")     # From start to index 3 (exclusive)
print(f"Fruits from index 1 to 3: {fruits[1:4]}")  # From index 1 to 4 (exclusive)
print(f"Every other fruit: {fruits[::2]}")     # Step of 2 (every other element)
print(f"Reversed list: {fruits[::-1]}")       # Negative step reverses the list

print()

# 3. Modifying Lists
"""
Lists are mutable, meaning their contents can be changed after creation.
Common modification methods include append, insert, extend, remove, and pop.
"""
print("=== Modifying Lists ===")

# Append - adds an element to the end of the list
fruits.append("fig")
print(f"After append: {fruits}")

# Insert - adds an element at a specific position
fruits.insert(2, "apricot")  # Insert at index 2
print(f"After insert at index 2: {fruits}")

# Extend - adds multiple elements from another iterable
fruits.extend(["grape", "honeydew"])
print(f"After extend: {fruits}")

# Remove - removes the first occurrence of a specific value
fruits.remove("apricot")
print(f"After remove 'apricot': {fruits}")

# Pop - removes and returns an element (default is last element)
popped = fruits.pop()
print(f"Popped element: {popped}")
print(f"After pop: {fruits}")

# Pop at specific index - removes and returns element at given index
popped_index = fruits.pop(1)
print(f"Popped at index 1: {popped_index}")
print(f"After pop at index 1: {fruits}")

print()

# 4. List Methods
"""
Python lists have several built-in methods for common operations:
- sort(): sorts the list in place
- reverse(): reverses the list in place
- count(): counts occurrences of an element
- index(): finds the index of an element
- clear(): removes all elements
- copy(): creates a shallow copy
"""
print("=== List Methods ===")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Sort - sorts the list in ascending order (modifies original list)
numbers.sort()
print(f"Sorted numbers: {numbers}")

# Reverse - reverses the order of elements (modifies original list)
numbers.reverse()
print(f"Reversed numbers: {numbers}")

# Count - returns the number of times an element appears
count_ones = numbers.count(1)
print(f"Count of 1s: {count_ones}")

# Index - returns the index of the first occurrence of an element
index_of_five = numbers.index(5)
print(f"Index of 5: {index_of_five}")

# Clear - removes all elements from the list
numbers_copy = numbers.copy()  # Make a copy first to preserve original
numbers_copy.clear()
print(f"After clear: {numbers_copy}")

print()

# 5. Built-in Functions with Lists
"""
Python has several built-in functions that work with lists:
- len(): returns the number of elements
- sum(): returns the sum of numeric elements
- max()/min(): returns the largest/smallest element
- sorted(): returns a new sorted list (doesn't modify original)
- reversed(): returns a reverse iterator
"""
print("=== Built-in Functions with Lists ===")

numbers = [1, 2, 3, 4, 5]

# Length - number of elements in the list
print(f"Length of numbers: {len(numbers)}")

# Sum - sum of all numeric elements
print(f"Sum of numbers: {sum(numbers)}")

# Maximum and Minimum - largest and smallest elements
print(f"Max: {max(numbers)}, Min: {min(numbers)}")

# Sorted - returns a new sorted list without modifying the original
unsorted = [3, 1, 4, 1, 5]
sorted_list = sorted(unsorted)
print(f"Original: {unsorted}")
print(f"Sorted copy: {sorted_list}")

# Reversed - returns an iterator that yields elements in reverse order
reversed_list = list(reversed(numbers))  # Convert iterator to list
print(f"Reversed: {reversed_list}")

print()

# 6. List Operations
"""
Lists support various operations:
- Concatenation (+) : combining two lists
- Repetition (*) : repeating a list multiple times
- Membership testing (in/not in) : checking if an element exists
"""
print("=== List Operations ===")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation - combining two lists into a new list
combined = list1 + list2
print(f"Concatenated: {combined}")

# Repetition - repeating the list elements multiple times
repeated = list1 * 3
print(f"Repeated 3 times: {repeated}")

# Membership testing - checking if an element is in the list
print(f"Is 2 in list1? {2 in list1}")
print(f"Is 7 not in list1? {7 not in list1}")

print()

# 7. Advanced List Operations
"""
Advanced list techniques include:
- List comprehensions with conditions
- Nested list comprehensions for multi-dimensional lists
- zip() function for combining multiple iterables
"""
print("=== Advanced List Operations ===")

# List comprehension with condition - filtering while transforming
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehension - creating matrices or multi-dimensional lists
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"Multiplication table: {matrix}")

# Zip function - combines multiple iterables element-wise
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped = list(zip(names, ages))
print(f"Zipped: {zipped}")

# Unzip - separating zipped tuples back into individual lists
unzipped_names, unzipped_ages = zip(*zipped)
print(f"Unzipped names: {list(unzipped_names)}")
print(f"Unzipped ages: {list(unzipped_ages)}")

print()

# 8. Common List Patterns
"""
Common programming patterns with lists:
- Filtering: selecting elements that meet a condition
- Transforming: applying operations to each element
- Finding elements: extracting elements based on criteria
- Removing duplicates: creating unique element lists
"""
print("=== Common List Patterns ===")

# Filter elements - using list comprehension to select specific elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

# Transform elements - applying operations to each element
doubled = [x * 2 for x in numbers]
print(f"Doubled: {doubled}")

# Find elements meeting condition - filtering with different criteria
greater_than_five = [x for x in numbers if x > 5]
print(f"Greater than 5: {greater_than_five}")

# Remove duplicates while preserving order - using dict.fromkeys()
duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = list(dict.fromkeys(duplicates))
print(f"Unique elements: {unique}")

print()

# 9. List as Stack and Queue
"""
Lists can be used as simple stacks and queues:
- Stack: Last In, First Out (LIFO) - use append() and pop()
- Queue: First In, First Out (FIFO) - use append() and pop(0)
Note: For production code, use collections.deque for queues as it's more efficient
"""
print("=== List as Stack and Queue ===")

# Stack (LIFO - Last In, First Out)
stack = []
stack.append(1)  # Push operation
stack.append(2)
stack.append(3)
print(f"Stack after pushes: {stack}")

top = stack.pop()  # Pop operation (removes last element)
print(f"Popped from stack: {top}")
print(f"Stack after pop: {stack}")

# Queue (FIFO - First In, First Out) - using deque is better, but list works
queue = []
queue.append(1)  # Enqueue operation
queue.append(2)
queue.append(3)
print(f"Queue after enqueues: {queue}")

front = queue.pop(0)  # Dequeue operation (removes first element)
print(f"Dequeued from queue: {front}")
print(f"Queue after dequeue: {queue}")

print()

# 10. List Copying
"""
Understanding list copying is crucial:
- Assignment (=) creates a reference, not a copy
- Shallow copy: copies the list but shares nested objects
- Deep copy: creates completely independent copies of nested objects
"""
print("=== List Copying ===")

original = [1, 2, [3, 4]]

# Shallow copy - copies the list but nested objects are shared
shallow = original.copy()
shallow[2][0] = 99  # Modifies the nested list in both original and shallow copy
print(f"Original after shallow copy modification: {original}")
print(f"Shallow copy: {shallow}")

# Deep copy - creates completely independent copies
import copy
original2 = [1, 2, [3, 4]]
deep = copy.deepcopy(original2)
deep[2][0] = 100  # Only modifies the deep copy
print(f"Original after deep copy modification: {original2}")
print(f"Deep copy: {deep}")
