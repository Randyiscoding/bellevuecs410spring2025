# ----------------------------------------------------------
# Filename: tester.py
# Author: Nasheb Ismaily
# ----------------------------------------------------------

import tests
from week1_assignment import *

def run_tests(test_cases, function_to_test):
    total_tests = sum(len(test_cases[func]) for func in test_cases)
    test_counter = 0
    passed_tests = 0

    for func in test_cases:
        for case in test_cases[func]:
            test_counter += 1
            args, expected = case[:-1], case[-1]
            try:
                if func == "collect_user_details":
                    got = function_to_test[func](*args[0])  # Unpack the tuple for this function
                elif isinstance(args, tuple):
                    got = function_to_test[func](*args)
                else:
                    got = function_to_test[func](args)

                if got == expected:
                    passed_tests += 1
                    print(f"Test {test_counter}/{total_tests}: Correct.")
                else:
                    print(f"Test {test_counter}/{total_tests}: Incorrect. Expected: {expected}, Got: {got}")

            except Exception as e:
                print(f"Test {test_counter}/{total_tests}: Error occurred: {e}")


    print(f"Passed {passed_tests} of {total_tests} tests.")


if __name__ == "__main__":
    test_cases = {
        "collect_user_details": tests.test_collect_user_details(),
        "factorial": tests.test_factorial(),
        "sort_numbers": tests.test_sort_numbers()
    }

    functions_to_test = {
        "collect_user_details": collect_user_details,
        "factorial": factorial,
        "sort_numbers": sort_numbers
    }

    run_tests(test_cases, functions_to_test)
