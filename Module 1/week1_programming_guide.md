**Week 1: Introduction to Algorithms and Python**

1. **collect_user_details**:

- **Guide**:
  - This function aims to collect user details such as name, age, and favorite color, and return them in a structured manner. Given that we want to return multiple pieces of data from a function, consider how Python facilitates this. A tuple, being an ordered and immutable sequence type, is an excellent choice to group together diverse types of data.
- **Pseudocode**:
- FUNCTION collect_user_details(name, age, color):  
    CREATE a tuple with name, age, and color  
    RETURN the tuple

1. **factorial**:

- **Guide**:
  - Factorials possess a recursive nature; the factorial of n is n multiplied by the factorial of n-1. The challenge here is to implement a recursive function. Remember to handle the base case where n equals 0 or 1, as the factorial of both these values is 1.
- **Pseudocode**:
- FUNCTION factorial(n):  
    IF n is 0 or 1:  
    RETURN 1  
    ELSE:  
    RETURN n multiplied by factorial(n-1)

1. **sort_numbers**:

- **Guide**:
  - The objective here is to manually order a list of numbers in ascending order. While there are many sorting algorithms, a simple one to consider for this function might be the Bubble Sort or Insertion Sort. At a high level, you’ll be comparing elements and swapping them if they’re out of order, iterating through the list multiple times until it’s sorted.
- **Pseudocode**:
- FUNCTION sort_numbers(nums):  
    FOR i from 0 to length of nums:  
    FOR j from 0 to length of nums minus i minus 1:  
    IF nums\[j\] is greater than nums\[j+1\]:  
    SWAP nums\[j\] and nums\[j+1\]  
    RETURN nums