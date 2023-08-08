# “Author: Varun Asuri
# It is not ok to post my anonymized solution

from math import inf
h, w = tuple(map(int, input().split())) # read in the input for the height and width 

while h and w: # as long as the input isn't 0 0
    b, x = [list(map(int, [*input()])) for i in range(h)], h*w+2 # define the board 2d array along with the base graph side-length
    g, z, d = [[inf]*x for i in range(x)], [-1 if i == 0 else 0 if i <= w else i-w for i in range(x)], [inf]*x # i define my initial graph, previous array, and array of distances from source
    for i in range(w): g[0][i+1], g[-2-i][-1] = b[0][i], 0 # define the adjacency matrix compared to the ending and beginning

    for i in range(1, w*h+1): 
        r, m = divmod(i-1, w) # find the division and modulus to use for 2d array
        if r: 
            g[i][i-w] = b[r-1][m] # if i can go up note it down
            if m: g[i][i-w-1] = b[r-1][m-1] # if i can go left and up not that down
            if m < w-1: g[i][i-w+1] = b[r-1][m+1] # if i can go right and up not that down
        if r < h-1: 
            g[i][i+w] = b[r+1][m] # if i can go down note it down
            if m: g[i][i+w-1] = b[r+1][m-1] # if i can go left and down not that down
            if m < w-1: g[i][i+w+1] = b[r+1][m+1] # if i can go right and down not that down
        if m: g[i][i-1] = b[r][m-1] # if i can go left note it down
        if m < w-1: g[i][i+1] = b[r][m+1] # if i can go right note it down

    d[0], s = 0, [0]*x # define distance and boolean array for dijkstra
    for i in range(x): 
        u, l = -1, inf # predefine the min and index and unreasonable numbers
        for v in range(x): # for every number there
            if d[v] < l and s[v] == 0: l, u = d[v], v # if i haven't checked it yet and its the smallest one go to it
        s[u] = 1 # add it to the boolean array
        for v in range(x): 
            if s[v] == 0 and d[v] > d[u]+g[u][v]: d[v], z[v] = d[u]+g[u][v], u # try optimizing the rest with this one node

    n, a = z[x-1], [] # 
    while n: a.append(n-1);n = z[n] # use the previous array to find the entire path of destruction
    for e in a: 
        r, m = divmod(e, w) # find the index of the broken box with divmod
        b[r][m] = ' ' # replace the broken box with a space

    for i in range(h): print(''.join(str(e) for e in b[i])) # join all the characters together for the broken block print
    print() # print out the new line

    h, w = tuple(map(int, input().split())) # read in the input before the next while loop iteration