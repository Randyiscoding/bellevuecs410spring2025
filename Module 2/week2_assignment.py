def calculate_execution_time(func, *args):
    """
    Calculate and return the time taken for function 'func' to execute with arguments '*args'.
    """
    import datetime
    getstartdatetime = datetime.datetime.now()
    func(*args)
    getenddatetime = datetime.datetime.now()
    time = getenddatetime - getstartdatetime
    return time
    pass

def bubble_sort(nums):
    """
    Sort the list 'nums' using the bubble sort algorithm. Return the sorted list.
    """
    # start = nums
    # unsorted = [int(num) for num in start.split(',')]  # per google
    unsorted = nums
    a = len(unsorted)
    for x in range(a - 1):
        for y in range(a - x - 1):
            if unsorted[y] > unsorted[y + 1]:
                unsorted[y], unsorted[y + 1] = unsorted[y + 1], unsorted[y]

    return unsorted
    pass

def insertion_sort(nums):
    """
    Sort the list 'nums' using the insertion sort algorithm. Return the sorted list.
    """
    # start = nums
    # unsorted = [int(num) for num in start.split(',')]  # per google
    unsorted = nums
    a = len(unsorted)
    if a <=1:
        return unsorted
    else:
        for x in range(1, a):
            store = unsorted[x]
            readback = x-1
            while readback >=0 and store < unsorted[readback]:
                unsorted[readback+1] = unsorted[readback]
                readback -= 1
            unsorted[readback+1] = store
        return unsorted
    pass

def fibonacci_recursive(n):
    """
    Return the nth Fibonacci number using a recursive approach.
    """
    match n:
        case 0:
            return n
        case 1:
            return n
        case _:
            start = n
            prevnum = 0
            nextnum = 1
            store = nextnum
            nx = 0

            while nx != start - 2:
                nx += 1
                prevnum = nextnum
                nextnum = store
                store = prevnum + nextnum
            return store

    pass
