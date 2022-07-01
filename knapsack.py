

def unbounded_knapsack(capacity, n, weights, values):
    """
    params:
        capacity(int): maximum weight of the knapsack
        n(int): number of items
        weights(list): list of item weights
        values(list): list of item values
    """
    cap2best_val = [0 for _ in range(capacity + 1)]
    cap2items = [[] for _ in range(capacity + 1)]
    for w in range(0, capacity + 1):
        cap2best_val[w]= 0
        for i in range(0, n):
            if weights[i] <= w:
                if cap2best_val[w] < cap2best_val[w - weights[i]] + values[i]:
                    cap2best_val[w] = cap2best_val[w - weights[i]] + values[i]
                    cap2items[w] = list(cap2items[w - weights[i]])
                    cap2items[w].append(i)
    return cap2items[capacity]



def zero_one_knapsack(capacity, n, weights, values):
    cap2best_val = [[0 for _ in range(n + 1)] for x in range(capacity + 1)]
    for w in range(0, capacity + 1):
        for i in range(0, n):
            cap2best_val[w][i] = cap2best_val[w][i-1]
            if weights[i] <= w:
                cap2best_val[w][i] = max(cap2best_val[w][i], cap2best_val[w - weights[i]][i - 1] + values[i])
    return cap2best_val[capacity][n]


n = 1
weights = [5]
values = [12]
capacity = 29

print(zero_one_knapsack(capacity, n, weights, values))
                
# n = len(val) !!