n, m = tuple(map(int,input().split()))
start, crafting, ndeg = list(map(int,input().split())), {i:[] for i in range(n)}, {i:0 for i in range(n)}
answer = start.copy()
for i in range(m):
    material, result, count = tuple(map(int,input().split()))
    crafting[result].append( (material, count) )
    ndeg[material] += 1
from queue import Queue
stack = []
for k in ndeg:
    if ndeg[k] == 0:
        stack.append(k)
while stack:
    curr = stack.pop()
    for adj, weight in crafting[curr]:
        ndeg[adj]-=1
        if ndeg[adj]==0:
            stack.append(adj)
        answer[adj] += answer[curr] * weight
print(' '.join([str(x) for x in answer]))