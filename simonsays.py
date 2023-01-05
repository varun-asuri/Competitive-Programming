for i in range(int(input())):   #loop through given amount of commands
    s = input()                 #read in command
    if "Simon says " in s:      #if it has simon says...
        print(s[11:])           #then print out rest of line after simon says