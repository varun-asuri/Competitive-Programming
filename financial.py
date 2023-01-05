from math import inf, ceil
line = list(map(int, input().split()))
n, m = line[0], line[1]
opps = []
for i in range(n):
    line = list(map(int, input().split()))
    opps.append([line[1]/line[0], line[1], line[0]])
opps = sorted(opps)

days, cost, daily = inf, 0, 0
for i in range(n):
    cost += opps[i][1]
    daily += opps[i][2]
    temp = (cost+m) / daily
    if temp < days: days = temp
    else: break
print(ceil(days))