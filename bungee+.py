n, h = int(input()), list(map(int,input().split()))
if n < 3: print(0)
else:
    t, a, d = 0, 0, 10**10
    for b in range(1, n):
        if h[b] < d: d = h[b]
        if h[b] > d: t = max(t, min(h[a], h[b]) - d)            
        if h[b] >= h[a]: a = b; d = 10**10; continue
    print(t)