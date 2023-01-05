from math import ceil
p = int(input())
for tp in range(p):
    line = list(map(int, input().split()))
    k, n = line[0], line[1]
    nums = []
    for i in range(ceil(n/10)):
        for num in list(map(int, input().split())):
            nums.append(num)
    sort = sorted(nums)
    count = 0
    for i in range(n):
        if nums[i] == sort[count]: count += 1
    print(k, n - count)