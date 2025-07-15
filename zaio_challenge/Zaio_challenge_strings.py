def access_string_section(text, start, end):
    """
    Accesses a section of the string from start (inclusive) to end (exclusive).

    Parameters:
        text (str): The input string.
        start (int): The starting index.
        end (int): The ending index.

    Returns:
        str: The substring from start to end.

    Raises:
        IndexError: If start or end is out of bounds.
    """
    # YOUR CODE HERE
    if not (0 <= start <= len(text)) or not (0 <= end <= len(text)):
        raise IndexError("Start or end index is out of bounds.")
    
    return text[start:end]

print(access_string_section("python programming" , 7, 18))

def merge_strings(strings, sep):
    """
    Merges a list of strings using the given separator.

    Parameters:
        strings (list): A list of strings to merge.
        sep (str): The separator string.

    Returns:
        str: The merged string.
    """
    # YOUR CODE HERE
    return sep.join(strings)
print(merge_strings(["python", "is", "fun"], "-"))

def count_vowels(text):
    """
    Counts the number of vowels in the input string.

    Parameters:
        text (str): The input string.

    Returns:
        int: The count of vowels in the string.
    """
    # YOUR CODE HERE
    vowels = 'aeiou'
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count
print(count_vowels("hello world"))

def contains_substring(text, substring):
    """
    Checks if a substring is present in the main string.

    Parameters:
        text (str): The main string.
        substring (str): The substring to check.

    Returns:
        bool: True if the substring is found, False otherwise.
    """
    # YOUR CODE HERE
    return substring in text
print(contains_substring("hello world", "world"))

def format_with_fstring(name, age, city):
    """
    Formats the input values into a string using an f-string.

    Parameters:
        name (str): The name of the person.
        age (int): The age of the person.
        city (str): The city where the person lives.

    Returns:
        str: A formatted string with the person's details.
    """
    # YOUR CODE HERE
    return f"Name: {name}, Age: {age}, City: {city}"
print(format_with_fstring("Bob", 25, "San Francisco"))

def format_with_method(name, age, city):
    """
    Formats the input values into a string using the .format() method.

    Parameters:
        name (str): The name of the person.
        age (int): The age of the person.
        city (str): The city where the person lives.

    Returns:
        str: A formatted string with the person's details.
    """
    # YOUR CODE HERE
    return "Name: {name}, Age: {age}, City: {city}".format(name =name, age =age, city= city)
print(format_with_method("Bob", 25, "San Francisco"))

def split_string(text):
    """
    Splits a string into a list of words.

    Parameters:
        text (str): The input string.

    Returns:
        list: A list of words in the string.
    """
    # YOUR CODE HERE
    return text.split()
print(split_string("Split this string into words"))

# Informative Section
# Joining Strings
# To join multiple strings together, Python provides the .join() method. It allows you to combine a list of strings into a single string using a specified separator.

# Example:
# words = ["Python", "is", "fun"]
# sentence = " ".join(words)
# print(sentence)  # Output: "Python is fun"
# You can also use other separators like commas or hyphens:

# hyphenated = "-".join(words)
# print(hyphenated)  # Output: "Python-is-fun"
# Replacing Portions of Strings
# To replace a portion of a string with another value, you can use the .replace() method. It creates a new string with the specified substitutions.

# Example:
# text = "Hello world"
# new_text = text.replace("world", "Python")
# print(new_text)  # Output: "Hello Python"
# You can also replace multiple occurrences of a substring:

# text = "aa bb aa"
# new_text = text.replace("aa", "cc")
# print(new_text)  # Output: "cc bb cc"
# The upper() Method
# The .upper() method converts all the characters in a string to uppercase.

# Example:
# text = "hello"
# uppercase_text = text.upper()
# print(uppercase_text)  # Output: "HELLO"






# The lower() Method
# The .lower() method converts all the characters in a string to lowercase.

# Example:
# text = "HELLO"
# lowercase_text = text.lower()
# print(lowercase_text)  # Output: "hello"