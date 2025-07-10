def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
print(calculate_area(5, 3))

def describe_person(name, age):
    """
    Generate a descriptive string containing a person's name and age.

    Parameters:
        name (str): The name of the person.
        age (int): The age of the person.

    Returns:
        str: A formatted string in the format "Name: [name], Age: [age]".
    """
    return f"Name: {name}, Age: {age}"
print(describe_person("John", 23))

def calculate_rectangle_properties(length, width):
    """
    Calculate properties of a rectangle.

    Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        tuple: A tuple containing:
            - The area of the rectangle (float).
            - The perimeter of the rectangle (float).
            - A string indicating if it is a "Square" or "Rectangle".
    """
    # YOUR CODE HERE
    area = length * width
    perimeter = 2 * (length + width)
    shape_type = "Square" if length == width else "Rectangle"
    return area, perimeter, shape_type

print(calculate_rectangle_properties(5, 3))

#### STUDENT CODE CELL

# Global variable
counter = 10

def scope_demo():
    """
    Demonstrates the scope of variables.

    Returns:
        tuple: A tuple containing:
            - The local `counter` after incrementing it (int).
            - The global `counter` value (int).
    """
    # YOUR CODE HERE
    counter = 5
    counter += 1
    return counter, globals()["counter"]
print(scope_demo())

