def fractional_knapsack(values, weights, capacity):
    """
    Solve the fractional knapsack problem and return the maximum value that can be obtained.
    """
    value, weight = values, weights
    if not value or not weight or capacity == 0:
        return 0
    else:
        n = len(value)
        table = [value,weight, [0]*n]
        weight_used = 0
        totvalue = 0
        weight_remaining = capacity - weight_used
        for x in value:
            y = int(x/weight[value.index(x)])
            table[2].pop(value.index(x))
            table[2].insert(value.index(x), y)
        while weight_remaining >= 0:
            if not value or not weight or capacity == 0:
                return int(totvalue)
            else:
                if weight_used + weight[table[2].index(max(table[2]))] > capacity:
                    totvalue += value[table[2].index(max(table[2]))]*(weight_remaining/weight[table[2].index(max(table[2]))])
                    weight_used += weight[table[2].index(max(table[2]))]
                else:
                    totvalue += value[table[2].index(max(table[2]))]
                    weight_used += weight[table[2].index(max(table[2]))]
                    table[0].pop(table[2].index(max(table[2])))
                    table[1].pop(table[2].index(max(table[2])))
                    table[2].pop(table[2].index(max(table[2])))
            weight_remaining = capacity - weight_used
        return int(totvalue)
    pass

def coin_change_greedy(coins, amount):
    """
    Using a greedy approach, determine the minimum number of coins needed to make the given amount.
    If it's not possible to make the amount using the given coin denominations, return -1.
    """
    counter = 0
    money = 0
    while money < amount:
        if not coins:
            return -1
        else:
            if money + max(coins) <= amount:
                money += max(coins)
                counter += 1
            else:
                coins.pop(coins.index(max(coins)))
    return counter
    pass

def activity_selection(activities):
    """
    Given a list of 'activities' where each activity is represented as a tuple (start_time, end_time),
    determine the maximum number of activities that can be scheduled without any conflicts.
    Return the list of selected activities.
    """
    # lesson Credit: https://youtu.be/Qz6D7mrxaJM?si=XnSGI13FcHaUqHkM
    activities.sort(key=lambda x: x[1])
    start = []
    finish = []
    a = [activities[0]]
    for x in activities:
        start.append(x[0])
        finish.append(x[1])
    n = len(start)
    k = 0
    for m in range(1, n):
        if start[m] >= finish[k]:
            a.append(activities[m])
            k = m
    return a
    pass
