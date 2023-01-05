# “Author: Varun Asuri
# It is not ok to post my anonymized solution

# HELP RECEIVED FROM GEEKS FOR GEEKS: FLOYD WARSHALL

from math import inf # import infinity to use in my graph weights matrix
line = list(map(int, input().split())) # read in n, m, and q into a list
n, m, q = line[0], line[1], line[2] # store them respectively

while n != 0 or m != 0 or q != 0: # while it is a valid test case
    graph = [[inf] * n for i in range(n)] # create my empty graph weights matrix
    for i in range(n): graph[i][i] = 0 # define each self edge to 0

    for i in range(m): # for every edge given
        line = list(map(int, input().split())) # read in the values
        if graph[line[0]][line[1]] > line[2]: graph[line[0]][line[1]] = line[2] # store it in the matrix if it is better than what ive found
    
    for k in range(n): # for every starting node
        for i in range(n): # for every destination node
            for j in range(n): # for every intermediary node
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) # if the intermediary path is better reset the cost to that for this edge
    
    arbnegs = set() # set of all arbitrarily negative pathed nodes
    for i in range(n): # for every node
        if graph[i][i] < 0: arbnegs.add(i) # if it is in a negative cycle add it in to the set

    for i in range(q): # for every query given
        line = list(map(int, input().split())) # read in the query line
        check = True # dummy variable to check for non-negative cycle
        for neg in arbnegs: # for every negative cycle
            if graph[line[0]][neg] != inf and graph[neg][line[1]] != inf: # if the graph goes through it
                print("-Infinity") # print negative infinity
                check = False # change my dummy variable
                break # break from the cycle loop
        if check: # if the dummy variable is still true
            if graph[line[0]][line[1]] != inf: print(graph[line[0]][line[1]]) # check if the path is possible and print it if so
            else: print("Impossible") # else print impossible
    
    line = list(map(int, input().split())) # read the next line input
    n, m, q = line[0], line[1], line[2] # put them into n, m, and q
    print() # put the extra needed print line