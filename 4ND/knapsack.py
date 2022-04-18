def knapsack_packing(name, size, value, M, N):
    best = [0] * (M+1)
    cost = [0] * (M+1)
    for j in range(1, N+1):
        for i in range(1, M+1):
            if (i - size[j]) >= 0:
                if cost[i] < (cost[i - size[j]] + value[j]):
                    cost[i] = cost[i - size[j]] + value[j]
                    best[i] = j
        print("j=" + str(j))
        print(cost)
        print(best)
    for i in range(1, M+1):
        print(name[best[i]], end=" ")
    return cost, best


if __name__ == '__main__':
    knapsack_packing(['0', 'A', 'B', 'C', 'D', 'E'], [
                     0, 3, 4, 5, 7, 9], [0, 5, 7, 9, 12, 15], 19, 5)
