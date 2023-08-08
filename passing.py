# “Author: Varun Asuri
# It is not ok to post my anonymized solution

from math import inf
from sys import stdin # use stdin to account for eof inputs
l = stdin.readline()

while l:
    a, z = tuple(l.split()) # split to get the starting and ending person
    s = []
    for i in range(int(input())):
        l = set(stdin.readline().split()) # add a group into the list of sets
        s.append(l)
    x = len(s)+1 # find the side-length of the graph

    d, f, p = [[inf]*(x) for i in range(x)], [inf]*(x), [-1]*(x) # create the graph using groups instead of people for speed, distance array, and previous array
    for i, w in enumerate(s):
        for j, y in enumerate(s):
            if w == y: d[i+1][j+1] = 0 # set the distance from a location to itself to 0
            elif w.intersection(y): # if the two-sets have an overlap
                d[i+1][j+1] = len(y)-1 # establish the cost going one way
                d[j+1][i+1] = len(w)-1 # and back as well for both ways
    for i in range(1, x):
        if a in s[i-1]: d[0][i] = len(s[i-1])-1 # i can get to every node that has the starting person so i can begin

    f[0], b = 0, [0]*(x) # establish the boolean array and distance array
    for i in range(x): 
        u, l = -1, inf # set pointer and min at unreasonable numbers
        for v in range(x): 
            if f[v] < l and b[v] == 0: l, u = f[v], v # go through all of them to find the minimum remaining unchecked
        b[u] = 1 # label this one as checked
        for v in range(x): 
            if b[v] == 0 and f[v] > f[u]+d[u][v]: f[v], p[v] = f[u]+d[u][v], u # optimize all other paths with this node

    m, u, w = inf, -1, [] # establish the risk calculation, index of ending, and this array i used for output processing
    for i in range(1, x):
        if z in s[i-1] and f[i] < m: m, u = f[i], i # find out where the ending index has to be based on minimum risk

    if u == -1: print("impossible") # if there is no solution it is impossible
    else:
        r, i = [], u # define path storing array and pointer variable to traverse previous'
        while i != 0: # while i havent gotten back to the start
            r.append(i) # add in this number
            i = p[i] # back track one more
        if len(r) == 0: print("impossible"); break # if i somehow got through with no path exit just in case
        m, c = m-1, () # fix cost to account for last person not adding risk and create the solution tuple
        p = [(1, n,) if n != a else 0 for n in s[r[-1]-1]] # create list of tuples to operate bfs on

        while p:
            x = p.pop() # pop this tuple and process
            if x == 0: continue # if this is the dummy case skip
            if x[-1] == z: c = x; break # if i found a solution break and process
            if len(x) == len(r) + 1: continue # if this length has crossed that of the solution don't bother processing
            y = x[0] # store the number of nodes
            if x[-1] not in s[r[-y-1]-1]: continue # if it isn't in the next node i should be in it isn't part of the solution
            for o in s[r[-y-1]-1]: # go throuhg all the possible connection people after
                if o not in x: # as long as i havent seen then before
                    p.append((x[0]+1,) + x[1:] + (o,)) # add them in and process them next

        c = (m, a,) + c[1:] # combine the path, starting person, and risk to find the right output
        for e in c: print(e, end=' ') # loop and print it out
        print() # extra print line after space ending

    l = stdin.readline() # get the next line before the while loop iteration