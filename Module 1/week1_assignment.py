def collect_user_details(name, age, color):
    """
    Accept user details as parameters: name, age, and favorite color.
    Return them as a tuple.
    """
    strName = input("Whats your Name?").replace(" ", "")
    intAge = int(input("How old are you?"))
    strColor = input("Whats your favorite color?").replace(" ", "")

    strName = strName.capitalize()
    strColor = strColor.capitalize()

    tplePersonality = (strName, intAge, strColor)
    return tplePersonality
    pass

def factorial(n):
    """
    Calculate and return the factorial of the given number 'n' using recursion.
    """
    pass

def sort_numbers(nums):
    """
    Sort the list 'nums' in ascending order without using built-in functions.
    Return the sorted list.
    """
    pass
