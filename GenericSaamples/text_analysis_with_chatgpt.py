# ### 2. Choose ONE Track

# #### Track A — Improve This Prompt

# Start with the weak prompt below. Iterate 2–3 times to improve specificity, constraints, and outputs.

# **Weak prompt:**

# ```
# "Write some Python code for text analysis."
# ```

# **Your target (what an improved prompt should require):**

# - A function `analyze_text(text, top_n=3)` returning `word_count`, `char_count`, and top `top_n` words with frequencies.
# - Ignore case and punctuation; handle empty strings gracefully.
# - Include 2 concrete examples and expected outputs.
# - Add 2–3 basic tests (asserts) in the final cell.

# #### Track B — Refactor This with ChatGPT

# Use ChatGPT to refactor the following script for readability, edge cases, and testing.

# **Original script:**

# ```python
# def greet(name):
#     return "Hello " + name

# print(greet(" ada "))
# ```

# **Refactor goals:**

# - Strip whitespace; title-case names; handle non-string inputs safely.
# - Add inline docstring and type hints.
# - Provide 3 unit tests (simple asserts).

#--------------Original code return by chatgpt-----------------
import re
from collections import Counter

def analyze_text(text):
    # Remove punctuation and convert to lowercase
    clean_text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Split into words
    words = clean_text.split()
    
    # Word frequency
    word_freq = Counter(words)
    
    # Basic stats
    total_words = len(words)
    unique_words = len(word_freq)
    avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0
    
    # Most common words
    top_words = word_freq.most_common(5)
    
    return {
        'total_words': total_words,
        'unique_words': unique_words,
        'avg_word_length': round(avg_word_length, 2),
        'top_words': top_words
    }

# Example usage
sample_text = "This is a sample text for analysis. It contains words, and some repeated words like text and analysis."
result = analyze_text(sample_text)
print(result)
# Output: {'total_words': 18, 'unique_words': 14, 'avg_word_length': 4.22, 'top_words': [('and', 2), ('text', 2), ('analysis', 2), ('this', 1), ('is', 1)]}


