import sys
sys.setrecursionlimit(1000000000)

n, m = tuple(map(int,input().split()))
stack, zeroes = [], set()
for i in range(n):
    for j, num in enumerate(str(input())):
        if not int(num):
            zeroes.add((i,j))
            if (i == 0 or i == n-1 or j == 0 or j == m-1): stack.append((i,j))
visited, locs = set(), set(range(m*n))

while stack:
    y,x = stack.pop()
    if (y,x) in visited or (y,x) not in zeroes: continue
    if y >= n or x >= m or y < 0 or x < 0: continue

    visited.add((y,x))
    if (y,x-1) not in visited: stack.append((y,x-1))
    if (y,x+1) not in visited: stack.append((y,x+1))
    if (y-1,x) not in visited: stack.append((y-1,x))
    if (y+1,x) not in visited: stack.append((y+1,x))

edges, doubled = set(), set()
for loc in locs:
    y,x=divmod(loc,m)
    if (y,x) not in visited:
        if (y-1,x,y,x) in doubled: pass
        elif (y-1,x,y,x) in edges:
            edges.remove((y-1,x,y,x))
            doubled.add((y-1,x,y,x))
        else: edges.add((y-1,x,y,x))

        if (y,x-1,y,x) in doubled: pass
        elif (y,x-1,y,x) in edges:
            edges.remove((y,x-1,y,x))
            doubled.add((y,x-1,y,x))
        else: edges.add((y,x-1,y,x))

        if (y,x,y+1,x) in doubled: pass
        elif (y,x,y+1,x) in edges:
            edges.remove((y,x,y+1,x))
            doubled.add((y,x,y+1,x))
        else: edges.add((y,x,y+1,x))

        if (y,x,y,x+1) in doubled: pass
        elif (y,x,y,x+1) in edges:
            edges.remove((y,x,y,x+1))
            doubled.add((y,x,y,x+1))
        else: edges.add((y,x,y,x+1))
        
print(len(edges))