def longest_common_subsequence(s1, s2):
    """
    Find and return the longest common subsequence between 's1' and 's2'.
    """
    lcs_str = []
    x, y = len(s1), len(s2)
    if s1 == 0 or s2 == 0:
        return 0
    else:
        tbl = [[0] * (y + 1) for X in range(x + 1)]
        for A in range(1, x + 1):
            for B in range(1, y + 1):
                if s2[B - 1] == s1[A - 1]:
                    tbl[A][B] = tbl[A - 1][B - 1] + 1
                else:
                    tbl[A][B] = max(tbl[A - 1][B], tbl[A][B - 1])
        # builds table back in reverse to get string
        while x > 0 and y > 0:
            if s1[x - 1] == s2[y - 1]:
                lcs_str.append(s1[x - 1])
                x -= 1
                y -= 1
            elif tbl[x - 1][y] > tbl[x][y - 1]:
                x -= 1
            else:
                y -= 1

        return "".join(reversed(lcs_str))
    pass

def knapsack(weights, values, W):
    """
    Solve the 0/1 knapsack problem and return the maximum total value that can be obtained with the given weights and values and a knapsack of capacity 'W'.
    """
    capacity = W
    weight_value_map = {w: v for w, v in zip(weights, values)}

    def perm(arr, cap):
        import itertools
        wcombos = []
        for n in range(1, len(arr) + 1):
            for x in itertools.combinations(arr, n):
                combosum = sum(x)
                if combosum <= cap:
                    wcombos.append(x)
        return wcombos

    def sumit(wcombos):
        if not wcombos:
            return 0
        else:
            valuesums = []
            for x in range(len(wcombos)):
                # for y in range(len(wcombos[x])):
                value_sum = sum(weight_value_map[weight] for weight in wcombos[x])
                # value_sum = sum(table[1][table[0].index(weight)] for weight in wcombos[x][y])
                valuesums.append(value_sum)
            return max(valuesums)

    if not weights or not values or not capacity:
        return 0
    else:
        return sumit(perm(weights, capacity))
    pass

def coin_change(coins, amount):
    """
    Given different coin denominations in 'coins' and a total amount 'amount', find the minimum number of coins that make up that amount.
    Return -1 if that amount cannot be made up by any combination of the coins.
    """
    import itertools
    def determine_coins(coins, amount):
        combosum = []
        n = len(coins)
        while n > -1:
            for y in itertools.combinations_with_replacement(coins, n):
                if sum(y) == amount:
                    combosum.append(y)
            n -= 1
        return combosum

    def count_elements(combosum):
        if not combosum:
            return -1
        else:
            return len(min(combosum, key=len))

    return count_elements(determine_coins(coins, amount))
    pass
''' If i end up submitting this before updating the code. I dont understand dynamic programing
        or 2D arrays and unfortunately brute forced my way through. I perfer not to just copy and 
        paste code especially if i dont fully understand how it works. '''