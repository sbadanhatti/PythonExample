# **ChatGPT Prompt Example:**  
# _"Why am I getting a syntax error and missing argument error here?"_

# **ChatGPT Key Suggestion:**  
# - Add missing colon after function definition.  
# - Provide both arguments when calling the function.

# # Original Broken Code
# def add_numbers(a, b)
#     return a + b

# print(add_numbers(5))

#     def add_numbers(a, b)
#                          ^
# SyntaxError: expected ':'

# Fixed Code
def add_numbers(a, b):
    return a + b

total = add_numbers(5, 10)
print(total)  # Output: 15

#-------------------------------------------------
# **ChatGPT Prompt Example:**  
# _"Why is my for loop giving syntax error?"_

# **ChatGPT Key Suggestion:**  
# - Add colon `:` after `for` loop.  
# - Or loop directly over items instead of using range.  


# Original Broken Code
# items = ["apple", "banana", "cherry"]
# for i in range(len(items))
#     print(items[i])

#fixed code
items = ["apple", "banana", "cherry"]
for item in items:
    print(item)


# Original Broken Code
# rate = "5"  # percent as string
# months = 12
# monthly = 10000 * (rate/12)
# print(monthly)
# TypeError: unsupported operand type(s) for /: 'str' and 'int'

# Fixed Code
rate = 5  # percent as integer
months = 12
monthly = 10000 * (rate/12)
print(monthly)  # Output: 416.6666666666667 