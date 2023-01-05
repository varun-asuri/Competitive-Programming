n = int(input()) # store n
arr = list(map(int, input().split())) # store the array given
p, maxes, hi, lo = 0, [], -2147483649, 2147483648 # predefine the pivot count, max for every location, maximum, and minimum
for a in arr: # for every value in the array
    if a > hi: hi = a # if its higher than the maximum change the maximum
    maxes.append(hi) # add the crrent max to store max counts
for i, a in enumerate(arr[::-1]): # for every value in the value reversed
    if a < lo: lo = a # if its lower than the minimum change the minimum
    if lo == maxes[n-i-1]: p += 1 # if the min from the right is the same as the max from the left then this place is a pivot
print(p) # output the pivot count