# 1

def f(x):
    """
    This function returns x squared
    :param x: int
    :return: x multiplied with 2
    """
    return x**2
print(f(2))

# 2
def print_string(str):
    """
    This function prints the string value
    :param str: str
    :return: any string that was stored in a variable
    """
    print(str)
print_string("1,2,3")

# 3
def third(x,y,z, a = 2, b = 3):
    """
    This function just prints out three mandatory arguments
    :param x: int
    :param y: int
    :param z: int
    :param a: int
    :param b: int
    :return: just the string
    """
    print(x,y,z)
third(1,2,3)

# 4
def divide(x):

    return x / 2

def multiply(z):
    return z * 4
y = divide(4)
z = multiply(y)

print(z)

# 5

input = "Test string"


def convert(string):
    """
    This functions converts string to float number and catches some exceptions

    :param string: str
    :return: string in float format
    """
    try:
        return float(string)
    except ValueError:
        print("Impossible to convert string to float")
print(convert("er"))