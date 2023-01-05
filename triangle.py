n = int(input())
rel = []

for i in range(n):
    line = list(map(int, input().split()))
    rel.append(line)

drama, indx, pots = -1, [], []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            curr = sorted([rel[i][j], rel[i][k], rel[j][k]])
            pot = rel[i][j] * rel[i][k] * rel[j][k]
            if pot > drama or pot == drama and (curr[0] > pots[0] or curr[0] == pots[0] and curr[1] > pots[1] or curr[0] == pots[0] and curr[1] == pots[1] and curr[2] > pots[2]):
                drama = pot
                pots = curr
                indx = [i, j, k]

for x in indx: print(x+1, end=' ')