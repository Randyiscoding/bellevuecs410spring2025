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
    Code based on this visualization: https://www.tiktok.com/t/ZT2suqEoL/ --RE
    """
    def quicksort(final):
        if final == [] or len(final) == 1:
            return final
        else:
            check = -2
            result = []
            queue = list(quicksortpartition(final))  # Start with the full array as the first item in the queue
            while queue:
                try:
                    current = queue.pop(0)  # Remove the first element from queue
                except:
                    current = queue
                if isinstance(current, int) or len(current) <= 1:
                    if isinstance(current, int):
                        if result == []:
                            result.append(current)  # If the subset is small enough, store it
                        else:
                            check = current
                            for x in result:
                                if check == 0:
                                    result.insert(0, current)
                                    break
                                elif check in result:
                                    result.insert(result.index(check), current)
                                    break
                                elif check == x - 1:
                                    result.insert(result.index(x), current)
                                    break
                                elif check == x + 1:
                                    result.insert(result.index(x) + 1, current)
                                    break
                                else:
                                    if check > result[-1]:
                                        result.append(current)
                                        break
                                    elif check < result[0]:
                                        result.insert(0, current)
                                        break
                                    else:
                                        for y in range(0, len(result) - 1):
                                            if check >= result[y] and check <= result[y + 1]:
                                                result.insert(y + 1, current)
                                                break
                                        break
                    else:
                        if result == []:
                            result.append(current[0])  # If the subset is small enough, store it
                        else:
                            check = current[0]
                            for x in result:
                                if check == 0:
                                    result.insert(0, current[0])
                                    break
                                elif check in result:
                                    result.insert(result.index(check), current[0])
                                    break
                                elif check == x - 1:
                                    result.insert(result.index(x), current[0])
                                    break
                                elif check == x + 1:
                                    result.insert(result.index(x) + 1, current[0])
                                    break
                                else:
                                    if check > result[-1]:
                                        result.append(current[0])
                                        break
                                    elif check < result[0]:
                                        result.insert(0, current[0])
                                        break
                                    else:
                                        for y in range(0, len(result) - 1):
                                            if check >= result[y] and check <= result[y + 1]:
                                                result.insert(y + 1, current[0])
                                                break
                                        break
                else:
                    queue.extend(quicksortpartition(current))  # Otherwise, split and continue

            return result

    def quicksortpartition(next):
        if isinstance(next, int):
            return next
        elif len(next) == 1:
            return next[0]
        else:
            current_array, partition_value = quicksortstart(next)
            index = current_array.index(partition_value)
            rightlist = current_array[index + 1:]
            leftlist = current_array[:index]
            if rightlist == []:
                return partition_value, leftlist
            elif leftlist == []:
                return rightlist, partition_value
            else:
                # splitlist = [leftlist, rightlist, partition_value]
                # return splitlist
                return leftlist, partition_value, rightlist

    def quicksortstart(start):
        if len(start) <= 1:
            return start
        else:
            pivot_value = start[-1]
            swap_maker = -1
            for index, value in enumerate(start, start=0):
                if value <= start[-1]:
                    swap_maker += 1
                    if index > swap_maker:
                        start[index], start[swap_maker] = start[swap_maker], start[index]
                    elif index == swap_maker:
                        pass
            return start, pivot_value

    help = quicksort(arr)
    return help

def binary_search(arr, x):
    """
    Find 'x' in sorted 'arr' using binary search. Return the index of 'x', or -1 if not found.
    """
    pass
