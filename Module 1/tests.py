# ----------------------------------------------------------
# Filename: tests.py
# Author: Nasheb Ismaily
# ----------------------------------------------------------

def test_collect_user_details():
    return [
        (("John", 25, "Blue"), ("John", 25, "Blue")),  # Test 1
        (("Alice", 30, "Red"), ("Alice", 30, "Red")),  # Test 2
        (("Bob", 22, "Green"), ("Bob", 22, "Green")),  # Test 3
        (("Eve", 28, "Yellow"), ("Eve", 28, "Yellow")),  # Test 4
        (("Tom", 24, "Black"), ("Tom", 24, "Black")),  # Test 5
        (("Mia", 21, "Purple"), ("Mia", 21, "Purple")),  # Test 6
        (("Chris", 26, "Orange"), ("Chris", 26, "Orange")),  # Test 7
        (("Zoe", 29, "Pink"), ("Zoe", 29, "Pink"))  # Test 8
    ]

def test_factorial():
    return [
        (0, 1),  # Test 9
        (1, 1),  # Test 10
        (5, 120),  # Test 11
        (6, 720),  # Test 12
        (7, 5040),  # Test 13
        (8, 40320),  # Test 14
        (4, 24),  # Test 15
        (3, 6)  # Test 16
    ]

def test_sort_numbers():
    return [
        ([5, 3, 1, 2, 4], [1, 2, 3, 4, 5]),  # Test 17
        ([], []),  # Test 18
        ([1], [1]),  # Test 19
        ([2, 1], [1, 2]),  # Test 20
        ([100, 99, 101], [99, 100, 101]),  # Test 21
        ([3, 3, 3, 3], [3, 3, 3, 3]),  # Test 22
        ([4, 2, 4, 2], [2, 2, 4, 4]),  # Test 23
        ([10, 20, 30], [10, 20, 30]),  # Test 24
        ([5], [5])  # Test 25
    ]
