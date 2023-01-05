# “Author: Varun Asuri
# It is not ok to post my anonymized solution

read = input().split() # read input
stops, capacity = int(read[0]), int(read[1]) # store number of stops and truck capacity

positives = [] # store all locations with letters needed
negatives = [] # store positive and negative locations separately
for i in range(stops): # for every stop
    read = input().split() # read input
    location, letters = int(read[0]), int(read[1]) # parse the location and letter count
    if location < 0: negatives.append( (-location, letters) ) # if its a negative add to negatives
    else: positives.append( (location, letters) ) # else add to positives
positives.sort(reverse=True) # sort the positive locations largest to smallest
negatives.sort(reverse=True) # do same for the negatives

curr = 0 # use to store current location
miles = 0 # total miles travelled
carry = capacity # load up the truck to capacity
loc, count = 0, 0 # use to parse the positives and negatives lists of tuples
for i, pair in enumerate(positives): # for every location in positives
    loc, count = pair # store location and letter count
    miles += abs(loc-curr) # travel there and account for distance
    while count > carry: # while the letter count is more than we can carry
        count -= carry # unload letters
        miles += loc * 2 # travel to origin and back
        carry = capacity # restock
    carry -= count # empty remaining needed letters
    count = 0 # note that location is now done
    curr = loc # update current location for next travel
miles += loc # add miles needed to travel back

curr = 0 # reset current location
carry = capacity # restock truck
for i, pair in enumerate(negatives): # perform the same operation for the negative locations
    loc, count = pair
    miles += abs(loc-curr)
    while count > carry:
        count -= carry
        miles += loc * 2
        carry = capacity
    carry -= count
    count = 0
    curr = loc
if negatives: # if we had negative locations
    miles += loc # add travel distance back

print(miles) # print output