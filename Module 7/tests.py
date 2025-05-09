def test_selection_sort():
    return [
        ([64, 25, 12, 22, 11], [11, 12, 22, 25, 64]),  # Test 1
        ([5, 1, 9, 3, 7, 6, 8, 2, 4, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),  # Test 2
        ([5], [5]),  # Test 3
        ([], []),  # Test 4
        ([3, 3, 3, 3, 3], [3, 3, 3, 3, 3]),  # Test 5
        ([99, 1, 45, 23, 67, 2, 3, 89], [1, 2, 3, 23, 45, 67, 89, 99]),  # Test 6
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # Test 7
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),  # Test 8
        ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5]),  # Test 9
        ([], []),  # Test 10
    ]

def test_quick_sort():
    return [
        ([64, 25, 12, 22, 11], [11, 12, 22, 25, 64]),  # Test 11
        ([10, 7, 8, 9, 1, 5], [1, 5, 7, 8, 9, 10]),  # Test 12
        ([], []),  # Test 13
        ([5], [5]),  # Test 14
        ([9, 8, 7, 6, 5], [5, 6, 7, 8, 9]),  # Test 15
        ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5]),  # Test 16
        ([1, 2, 3, 4], [1, 2, 3, 4]),  # Test 17
        ([4, 3, 2, 1], [1, 2, 3, 4]),  # Test 18
        ([10, 20, 15, 30, 25], [10, 15, 20, 25, 30]),  # Test 19
        ([100, 10, 1000, 1], [1, 10, 100, 1000]),  # Test 20
    ]

def test_binary_search_first_occurrence():
    return [
        ([1, 2, 2, 2, 3, 4, 5], 2, 1),  # Test 21
        ([1, 2, 3, 4, 5, 5, 5, 6], 5, 4),  # Test 22
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6, 5),  # Test 23
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 0),  # Test 24
        ([], 5, -1),  # Test 25
    ]
