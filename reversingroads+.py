from sys import stdin

depart, scc, time, lo, seen, stack, bset = [], set(), [0], [], [], [], []

def dfs(curr, m):
    lo[curr] = time[0]
    seen[curr] = time[0]
    stack.append(curr)
    bset[curr] = 1
    time[0] += 1

    for loc in depart[curr]:
        if seen[loc] == -1:
            dfs(loc, m)
            lo[curr] = min(lo[curr], lo[loc])
        elif bset[loc]:
            lo[curr] = min(lo[curr], seen[loc])

    elem = -1
    if lo[curr] == seen[curr]:
        scc = set()
        while elem != curr:
            elem = stack.pop()
            bset[elem] = 0
            scc.add(elem)
        if len(scc) == m: return m
    return 0

testcase = 1
line = stdin.readline()
while line:
    m, n = tuple(map(int, line.split()))
    points = [m]

    edges, depart = [], [set() for i in range(m)]
    for i in range(n):
        start, finish = tuple(map(int, stdin.readline().split()))
        depart[start].add(finish)
        edges.append( (start, finish) )

    print(f'Case {testcase}: ', end="")
    check, x, seen, lo, stack, bset = 0, 0, [-1]*m, [-1]*m, [], [0]*m
    for i in range(m):
        if seen[i] == -1: x = dfs(i, m)
        if x == m:
            print("valid")
            check = 1
            break

    if not check:
        check = x = 0
        for edge in edges:
            depart[edge[0]].remove(edge[1])
            depart[edge[1]].add(edge[0])

            seen, lo, stack, bset, time[0] = [-1]*m, [-1]*m, [], [0]*m, 0
            for i in range(m):
                if seen[i] == -1: x = dfs(i, m)
                if x == m:
                    print(edge[0], edge[1])
                    check = 1
                    break
            if check: break

            depart[edge[1]].remove(edge[0])
            depart[edge[0]].add(edge[1])

        if not check:
            print("invalid")
    
    testcase += 1
    line = stdin.readline()
