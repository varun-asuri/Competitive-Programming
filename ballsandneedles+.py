import sys
sys.setrecursionlimit(100000)

k = int(input())
paths3d, paths2d = {}, {}
start3d, start2d = (), ()
for i in range(k):
    line = list(map(int, input().split()))
    point1, point2, point1f, point2f = (line[0], line[1], line[2]), (line[3], line[4], line[5]), (line[0], line[1]), (line[3], line[4])
    if not i:
        start3d = point1
        start2d = point1f
    if point1 in paths3d: paths3d[point1].add(point2)
    else: paths3d[point1] = {point2}
    if point2 in paths3d: paths3d[point2].add(point1)
    else: paths3d[point2] = {point1}
    if point1f != point2f:
        if point1f in paths2d: paths2d[point1f].add(point2f)
        else: paths2d[point1f] = {point2f}
        if point2f in paths2d: paths2d[point2f].add(point1f)
        else: paths2d[point2f] = {point1f}

x = 0
seen = set()

def checkTrue(prev, curr):
    seen.add(curr)
    locs = paths3d[curr]
    for loc in locs:
        if loc not in seen:
            check = checkTrue(curr, loc)
            if check: return 1
        elif prev != loc: return 1
    return 0

for point in paths3d.keys():
    if point not in seen:
        if(checkTrue((), point)):
            x = 1; break
if x: print("True closed chains")
else: print("No true closed chains")

x = 0
seen = set()

def checkFloor(prev, curr):
    seen.add(curr)
    locs = paths2d[curr]
    for loc in locs:
        if loc not in seen:
            check = checkFloor(curr, loc)
            if check: return 1
        elif prev != loc: return 1
    return 0

for point in paths2d.keys():
    if point not in seen:
        if(checkFloor((), point)):
            x = 1; break
if x: print("Floor closed chains")
else: print("No floor closed chains")