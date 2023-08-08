w, h = tuple(map(int,input().split()))
v, s, t, g, f = set(), [], set(), 0, ""
for a in range(h): f += input()
for a in range(w*h):
    if f[a] == 'T':
        d, m = divmod(a, w)
        if m and f[a-1] != '#': t.add(a-1)
        if m < w-1 and f[a+1] != '#': t.add(a+1)
        if d and f[a-w] != '#': t.add(a-w)
        if d < h-1 and f[a+w] != '#': t.add(a+w)

s.append(f.find('P'))
while s:
    x = s.pop()
    if x in v or f[x] == '#': continue
    else: v.add(x)
    if f[x] == 'G': g += 1
    if x in t: continue
    d, m = divmod(x, w)
    if m > 1 and x-1 not in v: s.append(x-1)
    if m < w-2 and x+1 not in v: s.append(x+1)
    if d > 1 and x-w not in v: s.append(x-w)
    if d < h-2 and x+w not in v: s.append(x+w)
print(g)