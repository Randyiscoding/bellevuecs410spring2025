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
    num = n
    math = [n]
    final = 1
    while num > 0:
        num = num - 1
        math.append(num)
    for num in math:
        if num == 0:
            num = 1
            final *= num
        else:
            final *= num
    pairs = [n, final]
    return final
    pass

def sort_numbers(nums):
    """
    Sort the list 'nums' in ascending order without using built-in functions.
    Return the sorted list.
    """
    #start = nums
    #unsorted = [int(num) for num in start.split(',')]  # per google
    unsorted = nums
    a = len(unsorted)
    for x in range(a - 1):
        for y in range(a - x - 1):
            if unsorted[y] > unsorted[y + 1]:
                unsorted[y], unsorted[y + 1] = unsorted[y + 1], unsorted[y]

    return unsorted
    pass
