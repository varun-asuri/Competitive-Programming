c = int(input())
for tc in range(c):
    line = list(map(int, input().split()))
    d, n = line[0], line[1]
    nums = list(map(int, input().split()))
    mods, run, ans = [0] * d, 0, 0
    for num in nums:
        run += num
        mods[run % d] += 1
    for mod in mods:
        if mod > 1: ans += (mod*(mod-1)) / 2
    print(int(ans) + mods[0])