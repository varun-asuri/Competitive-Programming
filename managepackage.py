import heapq

n = int(input())
while n:
    depend, packs, queue, output = {}, {}, [], []
    for i in range(n):
        case = input().split()
        for x in range(1, len(case)):
            if case[0] in packs: packs[case[0]].add(case[x])
            else: packs[case[0]] = {case[x]}
            if case[x] in depend: depend[case[x]].add(case[0])
            else: depend[case[x]] = {case[0]}
        if len(case) == 1: heapq.heappush(queue, case[0])
    
    count = 0
    while queue:
        case = heapq.heappop(queue)
        output.append(case)
        count += 1
        if case in depend:
            for post in depend[case]:
                packs[post].remove(case)
                if len(packs[post]) == 0:
                    heapq.heappush(queue, post)
    if count < n: print("cannot be ordered")
    else: print('\n'.join(output))

    n = int(input())