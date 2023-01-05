n = int(input())                                #read in the amount of worlds
x = 0                                           #initialize the number of people needed to kill
worlds = (input().split())[::-1]                #make a list of all the world populations and reverse it to make calculation easier
for i in range(n):                              #loop through populations
    worlds[i] = int(worlds[i])                  #convert from string to integer
    if i and worlds[i] > worlds[i-1]:           #if it has more people than the world before it
        x += (worlds[i] - worlds[i-1] + 1)      #add the amount of people necessary to kill in this world to make it less than the previous to the output number
        worlds[i] = worlds[i-1] - 1             #kill
    if worlds[i] < 1:                           #if a world has no people in it
        x = 1                                   #set kill amount to 1 as this is an impossible case then break
        break
print(x)                                        #print out people needed to kill