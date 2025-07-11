def square_numbers(numbers):
    """
    Squares each number in the input list using map and lambda.

    Parameters:
        numbers (list): A list of integers.

    Returns:
        list: A list containing the squares of the input integers.
    """
    # YOUR CODE HERE
    mapped_numbers = list(map(lambda x: x**2, numbers))
    return mapped_numbers
print(square_numbers([1, 2, 3, 4]))

from functools import reduce

def product_of_numbers(numbers):
    """
    Calculates the product of all numbers in the list using reduce and lambda.

    Parameters:
        numbers (list): A list of integers.

    Returns:
        int: The product of all integers in the list, or 1 if the list is empty.
    """
    # YOUR CODE HERE
    cumul_l = lambda x,y: x*y
    out1 = reduce(cumul_l, numbers, 1)
    return out1
print(product_of_numbers([1, 2, 3, 4]))

def filter_even_numbers(numbers):
    """
    Filters the list to include only even numbers using filter and lambda.

    Parameters:
        numbers (list): A list of integers.

    Returns:
        list: A list containing only the even integers from the input list.
    """
    # YOUR CODE HERE
    return list(filter(lambda x : x%2 ==0 , numbers))
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))

def filter_and_square_even_numbers(numbers):
    """
    Filters the list to include only even numbers, then squares them using map and lambda.

    Parameters:
        numbers (list): A list of integers.

    Returns:
        list: A list containing the squared values of even integers from the input list.
    """
    # YOUR CODE HERE
    out1 = list(filter(lambda x: x%2 ==0, map(lambda x: x**2 , numbers)))
    return out1
print(filter_and_square_even_numbers([1, 2, 3, 4, 5, 6]))

def sum_of_positive_even_numbers(numbers):
    """
    Calculates the sum of positive even numbers using filter and reduce with lambda.

    Parameters:
        numbers (list): A list of integers.

    Returns:
        int: The sum of positive even integers from the input list, or 0 if none exist.
    """
    # YOUR CODE HERE
    filtered = filter(lambda x: x > 0 and x % 2 == 0, numbers)
    return reduce(lambda a, b: a + b, filtered, 0)
print(sum_of_positive_even_numbers([1, 2, 3, -4, 5, 6]))