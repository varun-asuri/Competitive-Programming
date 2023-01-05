line = list(map(int, input().split()))
n, m = line[0], line[1]

grid, stack = [], []
for i in range(n):
    line = [*input()]
    grid.append(line)
    for j in range(m):
        if grid[i][j] == 'V': stack.append((i,j))

while stack:
    i, j = stack.pop()
    if i == n-1: continue
    if grid[i+1][j] == '.':
        grid[i+1][j] = 'V'
        stack.append((i+1,j))
    elif grid[i+1][j] == '#':
        if j and grid[i][j-1] == '.':
            grid[i][j-1] = 'V'
            stack.append((i,j-1))
        if j < m-1 and grid[i][j+1] == '.':
            grid[i][j+1] = 'V'
            stack.append((i,j+1))

for line in grid: print(''.join(line))