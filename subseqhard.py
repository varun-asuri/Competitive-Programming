for i in range(int(input())): # for each testcase given
    input() # blank line
    input() # we dont need n
    a, t, p = 0, 0, {0:1} # define the 47 sequence count, total sum tracker, and a prefix sums dictionary while holds a default of 0 once for single 47's
    for x in list(map(int, input().split())): # for every element in the list
        t += x # add to the ongoing sum
        a += p.get((t-47), 0) # add to the answer if we found current sum - 47 earlier (this means we had to have found a 47 to get here)
        p[t] = p.get(t, 0) + 1 # add the current sum into the dictionary or add to the count of it found
    print(a) # print the answer