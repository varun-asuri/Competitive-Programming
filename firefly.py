import bisect

read = input().split()
width, height = int(read[0]), int(read[1])

stalagmites = []
stalactites = []

for i in range(width):
    length = int(input())
    if i%2: stalactites.append(length)
    else: stalagmites.append(length)
stalagmites.sort()
stalactites.sort()

minhits = width
count = 0
for j in range(height):
    b_left = bisect.bisect_left(stalagmites, j+1)
    b_right = bisect.bisect_right(stalactites, height-j-1)
    hits = len(stalagmites) + len(stalactites) - b_left - b_right
    if hits < minhits:
        minhits = hits
        count = 1
    elif hits == minhits:
        count += 1

print(minhits, count)