n = int(input())
while n:
    l1, l2, sortl1, sortl2 = [], [], [], []
    for i in range(n): l1.append(int(input()))
    for i in range(n): l2.append(int(input()))

    matches = {}
    sortl1 = sorted(l1)
    sortl2 = sorted(l2)
    for j in range(n): matches[sortl1[j]] = sortl2[j]

    for elem in l1: print(matches[elem])
    print()

    n = int(input())