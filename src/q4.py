def reverse_string(s):
    """
    Reverses the given string.

    Parameters:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        ValueError: If the input is not a string.
    """
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    
    return s[::-1]



# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

reverse_string("Hello World")
reverse_string("Python")