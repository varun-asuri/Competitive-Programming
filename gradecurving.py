from math import ceil as c # import the ceiling function for score calculations
r = list(map(int, input().split())) # get x, ylow, yhigh
x, ylow, yhigh = r[0], r[1], r[2] # input them into the variables
nmin, nmax, pos = 0, 0, False # initialize a minimum k, maximum k, and a boolean to check if possible to land between ylow and yhigh
while c(x) < ylow: # while less then ylow
    x = 10 * (x ** 0.5) # apply the curve
    nmin += 1 # add to minimum k
if c(x) <= yhigh: pos = True # if between ylow and yhigh change boolean
if yhigh == 100: nmax = "inf" # if hyhigh is 100 maxmimum k is infinity
else: # if not 100
    nmax = nmin # start maximum k at minimum k to account for movements made already
    while c(10 * (x ** 0.5)) <= yhigh: # if the next value will be within yhigh
        x = 10 * (x ** 0.5) # apply curve to stay within
        nmax += 1 # add to maximum k
if pos: print(nmin, nmax) # if landed between output min k and max k
else: print("impossible") # print impossible if didnt land between