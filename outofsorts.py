def binarysearch(given, val):
    low, high = 0, len(given) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if given[mid] == val: return 1
        elif given[mid] > val: high = mid - 1
        else: low = mid + 1
    return 0

read = input().split()
n, m, a, c, x0 = int(read[0]), int(read[1]), int(read[2]), int(read[3]), int(read[4])

seq = []
for i in range(n):
    elem = 0
    if i: elem = (a * seq[i-1] + c) % m
    else: elem = (a * x0 + c) % m
    seq.append(elem)

count = 0
for a in seq:
    x = binarysearch(seq, a)
    if x: count += 1

print(count)