def merge_sort(arr):
    """
    Sort 'arr' using the merge sort algorithm and return the sorted array.
    """
    if arr == []:
        return arr
    else:
        start = arr
        a = len(start)

        def splitmerge(arr):
            length = len(arr)
            leftlist = []
            rightlist = []
            x = 0
            for x in range(length):
                if x < (length / 2):
                    leftlist.append(arr[x])
            for x in range(length):
                if x >= (length / 2):
                    rightlist.append(arr[x])
            splitlist = (leftlist, rightlist)
            return splitlist

        def recursive_split(arr):
            """
            Recursively split the array until all subsets have at most 2 elements.
            Credit: Open AI
            """
            result = []
            queue = [arr]  # Start with the full array as the first item in the queue

            while queue:
                current = queue.pop(0)  # Remove the first element from queue

                if len(current) <= 2:
                    result.append(current)  # If the subset is small enough, store it
                else:
                    queue.extend(splitmerge(current))  # Otherwise, split and continue

            return result

        def sort(arr):
            unsorted = arr
            a = len(unsorted)
            if a <= 1:
                return unsorted
            else:
                for x in range(1, a):
                    store = unsorted[x]
                    readback = x - 1
                    while readback >= 0 and store < unsorted[readback]:
                        unsorted[readback + 1] = unsorted[readback]
                        readback -= 1
                    unsorted[readback + 1] = store
                return unsorted

        def remerge_and_sort(nameofargument):
            blah = recursive_split(start)
            remerge = []
            for x in blah:
                y = sort(x)
                z = y[0]
                remerge.append(z)
                try:
                    a1 = y[1]
                    remerge.append(a1)
                except:
                    pass
                sort(remerge)
            return remerge

        final = remerge_and_sort(start)
        return final
    pass

def quick_sort(arr):
    """
    Sort 'arr' using the quick sort algorithm and return the sorted array.
    """
    pass

def binary_search(arr, x):
    """
    Find 'x' in sorted 'arr' using binary search. Return the index of 'x', or -1 if not found.
    """
    pass
