# Unbounded Knapsack Problem
def UnboundedKnapsack(Capacity,n,weight,val):
    k=[]
    for i in range(Capacity+1):
        k.append(0)
    for i in range(0,Capacity+1):
        for j in range(0,n):
            if weight[j] < i:
                k[i] = max(k[i] , k[i-weight[j]]+val[j])
    return k[Capacity]


# No. of items
n = 3
# Weights of all items
weight = [7,3,20]
# Values of all items
val = [12,2,41]
# Capacity of Knapsack
Capacity = 58
print("The maximum value possible is ",UnboundedKnapsack(Capacity,n,weight,val))




# cap2best_val[w]= max(cap2best_val[w], cap2best_val[w - weights[i]] + values[i])