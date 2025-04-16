def selection_sort(nums):
    """
    Implement the selection sort algorithm to sort the list 'nums' in ascending order.
    Return the sorted list.
    """
    nums_length = len(nums) - 1
    for i in range(nums_length):
        ahh = min(nums[i + 1:])
        if ahh < nums[i]:
            nums[nums.index(ahh)], nums[i] = nums[i], nums[nums.index(ahh)]
    return nums
    pass

def quick_sort(arr):
    """
    Implement the quick sort algorithm to sort the list 'arr' in ascending order.
    Return the sorted list.
    """
    # a mass improvement from week 3 but i'm a bit confused if i got the "ascending" part of it right
    if len(arr) <= 1 or len(set(arr)) == 1:
        return arr
    else:
        midpoint_index = int((len(arr)-1)/2)
        midpoint = arr[midpoint_index]
        leftside = []
        rightside = []
        for x in arr:
            if x == midpoint:
                pass
            elif x < midpoint:
                leftside.append(x)
            else:
                rightside.append(x)
    return quick_sort(leftside) + [midpoint] + quick_sort(rightside)
    pass

def binary_search_first_occurrence(arr, x):
    """
    Implement a variation of binary search to find the first occurrence of 'x' in the sorted list 'arr'.
    Return the index of the first occurrence of 'x'. If 'x' is not present in 'arr', return -1.
    """
    low = 0
    high = len(arr) - 1
    result = -1
    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] == x:
            result = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return result
    pass
